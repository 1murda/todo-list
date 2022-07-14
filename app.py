import flask
import os
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import ( render_template, 
                    request, 
                    redirect, 
                    url_for)

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

connect = sqlite3.connect('taks.db', check_same_thread=False)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return redirect("/todolist")

@app.route('/todolist')
def todolist():
    # context = {'tasks': Task.query.all()}
    return render_template('todolist.html', context)


if __name__ == "__main__":
    app.run(debug=True)

