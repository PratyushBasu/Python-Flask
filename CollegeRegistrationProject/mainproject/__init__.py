# __init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'myPassKey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_CHANGES'] = False

db = SQLAlchemy(app)
Migrate(app, db)


from mainproject.students.views import students_blueprint
from mainproject.departments.views import departments_blueprint

app.register_blueprint(students_blueprint, url_prefix='/students')
app.register_blueprint(departments_blueprint, url_prefix='/departments')

 