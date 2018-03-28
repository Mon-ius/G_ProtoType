from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,\
                    BooleanField
from wtforms.validators import DataRequired,ValidationError,\
                    Email,EqualTo
from app.models import User
from flask_babel import _, lazy_gettext as _l


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    passwd = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    passwd = PasswordField(_l('Password'), validators=[DataRequired()])
    passwd2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('passwd')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    passwd = PasswordField(_l('Password'), validators=[DataRequired()])
    passwd2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('passwd')])
    submit = SubmitField(_l('Request Password Reset'))
