from flask_moment import Moment
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, _, lazy_gettext as _l

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()

# Moment,Migrate,Mail,Message,LoginManager,Bootstrap,SQLAlchemy,Babel