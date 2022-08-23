from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class AddJournalForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(), Length(min=1, max=50)])
    content = TextAreaField(label="Content", validators=[DataRequired(), Length(min=1, max=1000)])
    is_private = BooleanField(label="Keep Private")
    is_anonymous = BooleanField(label="Share Anonymously")
    submit = SubmitField(label="Add This")


class EditJournalForm(AddJournalForm):
    submit = SubmitField(label="Save Changes")
