from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Post')

