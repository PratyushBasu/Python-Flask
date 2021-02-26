# forms.py students

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddStudentForm(FlaskForm):
	name = StringField("Name of the student: ", validators=[DataRequired()])
	submit = SubmitField("Add Student")

class DelStudentForm(FlaskForm):
	id = IntegerField("Student ID: ")
	submit = SubmitField("Remove Student")