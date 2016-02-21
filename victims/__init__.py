from flask import Flask
from victims.main.controllers import main
from victims.utils import get_config_folder_path

app = Flask(__name__,
            instance_path=get_config_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

app.register_blueprint(main, url_prefix='/')