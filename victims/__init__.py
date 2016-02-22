from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from victims.main.controllers import main
from victims.data.controllers import data
from victims.utils import get_config_folder_path
from victims.config import configure_app

app = Flask(__name__,
            instance_path=get_config_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(data, url_prefix='/data')

configure_app(app)
mngr = Manager(app)
db = SQLAlchemy(app)

from victims.data.models import *