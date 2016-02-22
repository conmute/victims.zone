from flask import Response, Blueprint, current_app, render_template
import time

# File upload examples
from flask import request, redirect, url_for
import os
import json
import glob

from datetime import datetime


def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))

data = Blueprint('data', __name__)

@data.route('/get/all.kml')
def getall():
    content = current_app.config.get('MODE') + ' | '+ time.ctime()
    response = Response(render_template('data/main.kml', content=content))
    response.headers["Content-Type"] = "application/vnd.google-earth.kml+xml"
    return response

@data.route('/add/single')
def add_single():
    return render_template('add/single.jade')

@data.route('/add/summary')
def add_summary():
    return render_template('add/summary.jade')

@data.route('/add/record', methods=["POST"])
def add_record():

    from victims.data.models import User, Tag, Category, Record

    db = current_app.db

    form = request.form
    dateformat = '%m/%d/%Y'

    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True


    tag_list = []
    for tag_text in form.getlist('tags'):
        tag = db.session.query(Tag).filter_by(name = tag_text).first()
        if tag:
            tag_list.append(tag)
        else:
            try:
                tag = Tag(
                    name = tag_text
                )
                db.session.add(tag)
                db.session.flush()
                tag_list.append(tag)
                db.session.commit()
            except:
                if is_ajax:
                    return ajax_response(False, "Couldn't add a tag: {}".format(tag_text))
                else:
                    return "Couldn't add a tag: {}".format(tag_text)


    category_instance = None
    category = db.session.query(Category).filter_by(name = form.get('category')).first()
    if category:
        category_instance = category
    else:
        try:
            category = Category(
                name = form.get('category')
            )
            db.session.add(category)
            db.session.flush()
            category_instance = category
            db.session.commit()
        except:
            if is_ajax:
                return ajax_response(False, "Couldn't add a category: {}".format(form.get('category')))
            else:
                return "Couldn't add a category: {}".format(form.get('category'))


    record_id = None

    if form.get('type') == 'summary':
        map_data = json.loads(form.get('polygon'))
        date = form.get('date_range').split(' - ')
    else:
        location = form.get('location').split(', ')
        map_data = dict(lat = location[0], lng = location[0])
        date = datetime.strptime(form.get('date'), dateformat)

    user = User(id = 0, name = 'Demo user')

    record = Record(
        name = form.get('name'),
        description = form.get('description'),
        date_from = datetime.strptime(date[0], dateformat) if form.get('type') == 'summary' else date,
        date_to = datetime.strptime(date[1], dateformat) if form.get('type') == 'summary' else date,
        map_data = map_data,
        category = category_instance,
        tags = tag_list,
        type = form.get('type'),
        author = user # No authors implemented yet
    )

    return "record: {}".format(record)

    try:
        db.session.add(record)
        db.session.flush()
        record_id = record.id
        db.session.commit()
    except:
        if is_ajax:
            return ajax_response(False, "Couldn't add a record: {}".format(form))
        else:
            return "Couldn't add a record: {}".format(form)


    # Target folder for these uploads.
    target = "victims/static/uploads/{}".format(record_id)

    try:
        os.mkdir(target)
    except:
        if is_ajax:
            return ajax_response(False, "Couldn't create upload directory: {}".format(target))
        else:
            return "Couldn't create upload directory: {}".format(target)

    for upload in request.files.getlist("file"):
        filename = upload.filename.rsplit("/")[0]
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    if is_ajax:
        return ajax_response(True, record_id)
    else:
        return redirect(url_for("data.add_record", id=record_id))

@data.route('/record/<id>')
def show_record(id):
    return render_template('add/single.jade')


# File upload examples

@data.route('/upload_form')
def files_index():
    return render_template("add/files_form.jade")

@data.route('/files/<uuid>')
def files_list(uuid):
    # Get their files.
    root = "victims/static/uploads/{}".format(uuid)
    if not os.path.isdir(root):
        return "Error: UUID not found!"

    files = []
    for file in glob.glob("{}/*.*".format(root)):
        fname = file.split(os.sep)[-1]
        files.append(fname)

    return render_template("add/files.jade",
        uuid=uuid,
        files=files,
    )


