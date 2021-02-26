# forms.py departments

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddDeptForm(FlaskForm):
	student_id = IntegerField("Student Id Number: ", validators=[DataRequired()])
	dept = StringField("Department Name : ", validators=[DataRequired()])
	submit = SubmitField("Add Department")