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
    # guardo en una lista las tareas sacadas de la base de datos sqlite en la tabla task
    
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    return render_template('todolist.html', tasks=tasks)


@app.route('/addtask', methods=['POST', 'GET'])
def addtask():
    if request.method == 'POST':
        try:
            task = request.form['task']
            description = request.form['description']
            connect.execute("INSERT INTO task (task, description) VALUES ('{}', '{}')".format(task, description))
            connect.commit()
            
            return redirect(url_for('todolist'))
        
        except:
            return "Error al agregar la tarea"
    
    else:
        return render_template('add_task.html')


if __name__ == "__main__":
    connect.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, task TEXT, description TEXT)")
    app.run(debug=True)

