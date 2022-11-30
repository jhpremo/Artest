from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import Length, DataRequired

class CreateEditCompForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=1, max=75), DataRequired()])
    work_1_title = StringField('Work 1 Title', validators=[Length(min=1, max=75), DataRequired()])
    work_1_artist = StringField('Work 1 Artist', validators=[Length(min=1, max=75), DataRequired()])
    work_1_image_url = StringField('Work 1 Image Url', validators=[DataRequired(), Length(min=1, max=2048)])
    work_1_display_date = StringField('Work 1 Display Date', validators=[Length(min=1, max=50), DataRequired()])
    work_2_title = StringField('Work 2 Title', validators=[Length(min=1, max=75), DataRequired()])
    work_2_artist = StringField('Work 2 Artist', validators=[Length(min=1, max=75), DataRequired()])
    work_2_image_url = StringField('Work 2 Image Url', validators=[DataRequired(), Length(min=1, max=2048)])
    work_2_display_date = StringField('Work 2 Display Date', validators=[Length(min=1, max=50), DataRequired()])
    comparison_text = StringField('Comparison text', validators=[Length(min=0, max=3000)])
