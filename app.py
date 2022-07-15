import flask
import os
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import ( render_template, 
                    request, 
                    redirect, 
                    url_for)

app = flask.Flask(__name__,
                  template_folder='static/templates',
                  static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
connect = sqlite3.connect('taks.db', check_same_thread=False)

@app.route('/')
def index():
    return redirect("/todolist")

@app.route('/todolist')
def todolist():
    """ busco todas las tareas en la base de datos

    Returns:
        render_template: renderiza la pagina todolist.html
    """
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    return render_template('todolist.html', tasks=tasks)


@app.route('/addtask', methods=['POST', 'GET'])
def addtask():
    """ agrega una tarea a la base de datos

    Returns:
        render_template: renderiza la pagina todolist.html
    """
    if request.method == 'POST':
        try:
            task = request.form['task']
            description = request.form['description']
            connect.execute("INSERT INTO task (task, description) VALUES ('{}', '{}')".format(task, description))
            connect.commit()
            
            return redirect(url_for('todolist'))
        
        except:
            return "Error trying to add task"
    
    else:
        return render_template('add_task.html')

@app.route('/delete/<int:id>')
def delete(id):
    connect.execute("DELETE FROM task WHERE id = {}".format(id))
    connect.commit()
    return redirect(url_for('todolist'))

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    if request.method == 'POST':
        try:
            task = request.form['task']
            description = request.form['description']
            connect.execute("UPDATE task SET task = '{}', description = '{}' WHERE id = {}".format(task, description, id))
            connect.commit()
            return redirect(url_for('todolist'))
        except:
            return "Error trying to edit task"
    else:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM task WHERE id = {}".format(id))
        task = cursor.fetchone()
        return render_template('edit_task.html', task=task)


if __name__ == "__main__":
    connect.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, task TEXT, description TEXT)")
    app.run(debug=True)

