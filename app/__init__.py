from flask import Flask,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail,Message
from flask_bootstrap    import Bootstrap
from flask_moment import Moment
from flask_babel import Babel,_,lazy_gettext as _l
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
# app.config['SECRET_KEY']='dai3hoahudhiuahduiah'

app.config.from_object(Config)
# app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans_CN'
db = SQLAlchemy(app)
migrate=Migrate(app,db)
login = LoginManager(app)
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')





import logging
from logging.handlers import SMTPHandler

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'],
            subject='Microblog Failure',
            credentials=auth,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler(
        'logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')


@babel.localeselector
def get_locale():
    lan = request.accept_languages.best_match(app.config['LANGUAGES'])
    # print(lan)
    return lan
    # return 'zh_Hans_CN'


from app import routes,models,errors