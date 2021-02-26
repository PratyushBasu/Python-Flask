# views.py students

from flask import Blueprint, render_template, redirect, url_for
from mainproject import db
from mainproject.models import Students
from mainproject.students.forms import AddStudentForm, DelStudentForm


students_blueprint = Blueprint('students', __name__, 
									template_folder='templates/students')


@students_blueprint.route('/add-student', methods=['GET', 'POST'])
def add_student():
	form = AddStudentForm()

	if form.validate_on_submit():	
	# it's good to add a logic for null value sumission by the user
		name = form.name.data
		new_student = Students(name)
		db.session.add(new_student)
		db.session.commit()

		return redirect(url_for('students.view_students'))

	return render_template('addstudents.html', form=form)


@students_blueprint.route('/view-students')
def view_students():
	students_list = Students.query.all()

	return render_template('liststudents.html', students_list=students_list)


@students_blueprint.route('/delete-student', methods=['GET', 'POST'])
def del_student():
	# it's good to add a logic for null value sumission by the user
	form = DelStudentForm()

	if form.validate_on_submit():
		try:
			id = form.id.data
			student = Students.query.get(id)
			db.session.delete(student)
			db.session.commit()

			return redirect(url_for('students.view_students'))

		except:
			return redirect(url_for('students.view_students'))
	
	else:
		return render_template('delstudents.html', form=form)
