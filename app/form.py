from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email
from app.models import Usuario


class LoginForm(FlaskForm):
    nombre = StringField('Nombre: ', validators=[DataRequired()])
    apellido = StringField('Apellido: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    edad = StringField('Edad: ', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
    def validate_password(self, password):
        if len(password.data) < 7:
            raise ValidationError('Please use a lenght of 8 characters minimum')
    def validate_edad(self, edad):
        if int(edad.data) < 18:
            raise ValidationError('You must be 18 years old or more')