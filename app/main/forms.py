from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class TicketsForm(FlaskForm):
    title = TextAreaField(' title',validators = [Required()])
    description = TextAreaField(' discription',validators = [Required()])
    submit = SubmitField('submit')

