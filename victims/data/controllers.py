from flask import Response, Blueprint, current_app, render_template
import time

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
