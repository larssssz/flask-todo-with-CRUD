from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


# =========================
# ORIGINAL WEB ROUTES
# =========================

@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")

    new_todo = Todo(
        title=title,
        complete=False
    )

    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    todo.complete = not todo.complete

    db.session.commit()

    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("home"))


# =========================
# REST API ROUTES
# =========================

# CREATE TASK
@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({
            "error": "Title is required"
        }), 400

    new_task = Todo(
        title=data["title"],
        complete=False
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "id": new_task.id,
        "title": new_task.title,
        "complete": new_task.complete
    }), 201


# READ ALL TASKS
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = Todo.query.all()

    output = []

    for task in tasks:
        output.append({
            "id": task.id,
            "title": task.title,
            "complete": task.complete
        })

    return jsonify(output), 200


# UPDATE TASK
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task_api(task_id):
    task = Todo.query.get(task_id)

    if not task:
        return jsonify({
            "error": "Task not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data provided"
        }), 400

    task.title = data.get("title", task.title)
    task.complete = data.get("complete", task.complete)

    db.session.commit()

    return jsonify({
        "id": task.id,
        "title": task.title,
        "complete": task.complete
    }), 200


# DELETE TASK
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task_api(task_id):
    task = Todo.query.get(task_id)

    if not task:
        return jsonify({
            "error": "Task not found"
        }), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    }), 200


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)