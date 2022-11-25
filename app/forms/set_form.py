from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import Length, DataRequired

class CreateEditSetForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=1, max=75), DataRequired()])
