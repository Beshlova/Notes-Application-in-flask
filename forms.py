from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    EmailField,
    PasswordField,
    SubmitField,
    TextAreaField
)
from wtforms.validators import(
    InputRequired,
    Email,
    Length
)

#The registration-form class
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(),
                Length(min=2, max=50)])
    email = EmailField('Email',validators=[InputRequired(),
            Length(min=6,max=50),Email()])
    password = PasswordField('Password',validators=[InputRequired(),
               Length(min=8,max=80)])
    confirm_password = PasswordField('Password(confirm)',
                                     validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('Sign Up')

#The login-form class
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(),
                        Length(min=6, max=50), Email()])
    password = PasswordField('Password',validators=[InputRequired(),
               Length(min=8,max=80)])
    submit = SubmitField('Login')

#The create-notes form class
class CreateNotesForm(FlaskForm):
    title = StringField('Title',validators=[InputRequired(),
                                            Length(min=5,max=80)])
    content = TextAreaField(validators=[InputRequired(),
                                      Length(min=5,max=800)])
    submit = SubmitField('Create Notes')

#The update-notes form class
class UpdateNotesForm(FlaskForm):
    title = StringField('Title',validators=[InputRequired(),
                                            Length(min=5,max=80)])
    content = TextAreaField(validators=[InputRequired(),
                                      Length(min=5,max=800)])
    submit = SubmitField('Save Changes')

#The reset-password form class
class RequestResetForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(),
                        Length(min=6, max=50), Email()])
    submit = SubmitField('Request Password Reset')

#The reset-with-token form class
class ResetPasswordForm(FlaskForm):
    new_password = PasswordField('New Password', validators=[InputRequired(),
                                                     Length(min=8, max=80)])
    confirm_new_password = PasswordField('New Password(Confirm)', validators=[InputRequired(),
                                                     Length(min=8, max=80)])
    submit = SubmitField('Reset Password')

