from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample todo list
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    del todos[todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
