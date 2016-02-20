from victims import app
from victims.config import configure_app
from flask.ext.script import Manager

configure_app(app)
mngr = Manager(app)

if __name__ == '__main__':
    mngr.run()