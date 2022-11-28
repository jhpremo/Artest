from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import Length, DataRequired, URL

class CreateEditCardForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=1, max=75), DataRequired()])
    artist = StringField('Artist', validators=[Length(min=1, max=75), DataRequired()])
    image_url = StringField('Image Url', validators=[DataRequired(), Length(min=1, max=2048)])
    display_date = StringField('Display Date', validators=[Length(min=1, max=50), DataRequired()])
    notes = StringField('Notes', validators=[Length(min=0, max=1000)])
