from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm): 
    firstname=StringField('Firstname', validators=[DataRequired()])
    lastname=StringField('Lastname', validators=[DataRequired(message="Please fill your name")])
    email= StringField('email',validators=[DataRequired(), Email()])
    message=TextAreaField('message',validators=[DataRequired()])
    send=SubmitField('send')
