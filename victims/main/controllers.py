from flask import Blueprint, current_app, render_template
import time

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    content = current_app.config.get('MODE') + ' | '+ time.ctime()
    return render_template('home.htm', content=content)