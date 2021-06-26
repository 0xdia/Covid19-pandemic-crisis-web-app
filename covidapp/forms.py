from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email 


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = Password("Password", 
                        validators=[DataRequired(), Length(min=8, max=50)])
    
    autoritaire = BooleanField("Autoritaire")
    submit = SubmitField("Connecter")

