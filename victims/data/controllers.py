from flask import Response, Blueprint, current_app, render_template
import time

# File upload examples
from flask import request, redirect, url_for
import os
import json
import glob
from uuid import uuid4

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

@data.route('/files/upload', methods=["POST"])
def files_upload_request():
    """Handle the upload of a file."""
    form = request.form

    # Create a unique "session ID" for this particular batch of uploads.
    upload_key = str(uuid4())

    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True

    # Target folder for these uploads.
    target = "victims/static/uploads/{}".format(upload_key)

    try:
        os.mkdir(target)
    except:
        if is_ajax:
            return ajax_response(False, "Couldn't create upload directory: {}".format(target))
        else:
            return "Couldn't create upload directory: {}".format(target)


    print("=== Form Data ===")
    for key, value in form.items():
        print( key, "=>", value)

    for upload in request.files.getlist("file"):
        filename = upload.filename.rsplit("/")[0]
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    if is_ajax:
        return ajax_response(True, upload_key)
    else:
        return redirect(url_for("upload_complete", uuid=upload_key))


def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))