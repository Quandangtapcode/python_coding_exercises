from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

# get all tasks
@app.route("/api/tasks", methods = ["GET"])
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks ORDER BY deadline")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)   
 
# add task
@app.route("/api/tasks", methods = ["POST"])
def add_task():
    data = request.json
    title = data.get("title")
    deadline = data.get("deadline")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks(title, deadline, status) VALUES (%s, %s, 0)", (title, deadline))
    conn.commit()
    conn.close()
    return jsonify({"message": "Added task"})

# update task
@app.route("/api/tasks/<int:task_id>", methods = ["PUT"])
def update_task(task_id):
    data = request.json
    title = data.get("title")
    deadline = data.get("deadline")
    status = data.get("status")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tasks SET title = %s, deadline = %s, status = %s WHERE id = %s """, (title, deadline,status, task_id))
    
    conn.commit()
    conn.close()
    return jsonify({"message": "Updated task"})

# check task is done
@app.route("/api/tasks/<int:task_id>/complete", methods = ["PUT"])
def check_task_status(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = TRUE WHERE id = %s ", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "The mark was completed."})

# delete task by id
@app.route("/api/tasks/<int:task_id>", methods = ["DELETE"])
def delete_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted task"})

# delete all tasks
@app.route("/api/tasks", methods = ["DELETE"])
def delete_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks")
    cursor.execute("ALTER TABLE tasks AUTO_INCREMENT = 1")
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted all tasks"})

if __name__ == '__main__':
    app.run(debug=True)
    
 
    