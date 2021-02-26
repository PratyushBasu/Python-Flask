# models.py

#set up db inside __init__.py under CollegeRegistrationProject folder
from mainproject import  db


class Students(db.Model):

	__tablename__ = 'students'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	department = db.relationship('Departments', backref='students', uselist=False)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		if not self.department:
			return f'Student ID: {self.id}; Name: {self.name}; Department: Not enrolled yet'
		else:
			return f'Student ID: {self.id}; Name: {self.name}; Department: {self.department}'


class Departments(db.Model):

	__tablename__ = 'departments'

	id = db.Column(db.Integer, primary_key=True)	
	name = db.Column(db.Text)
	student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
	

	def __init__(self, student_id, name):
		self.student_id = student_id
		self.name = name

	def __repr__(self):
		return f'Department Name: {self.name}'