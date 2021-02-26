# views.py departments

from flask import Blueprint, render_template, redirect, url_for
from mainproject import db
from mainproject.models import Departments
from mainproject.departments.forms import AddDeptForm


departments_blueprint = Blueprint('departments', __name__, 
									template_folder='templates/departments')


@departments_blueprint.route('/add-department', methods=['GET', 'POST'])
def add_department():

	form = AddDeptForm()

	if form.validate_on_submit():
		student_id = form.student_id.data
		department_name = form.dept.data

		new_department = Departments(student_id, department_name)
		db.session.add(new_department)
		db.session.commit()

		return redirect(url_for('students.view_students'))

	return render_template('adddepartment.html', form=form)