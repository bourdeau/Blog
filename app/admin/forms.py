from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', widget=TextArea())
    submit = SubmitField('Submit')
