from flask import Flask, url_for, jsonify, render_template, redirect, request
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
mysql = MySQL()

app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_HOST", "db")
app.config["MYSQL_DATABASE_USER"] = os.getenv("MYSQL_USER", "root")
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_PASSWORD", "secret")
app.config["MYSQL_DATABASE_DB"] = os.getenv("MYSQL_DB", "todos")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_PORT", "3306"))

mysql.init_app(app)

def get_conn_cursor():
    conn = mysql.get_db()
    cur = conn.cursor()
    return conn, cur

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/todos", methods = ['GET'])
def list_todos():

    _, cur = get_conn_cursor()
    cur.execute("SELECT id, title FROM todos ORDER BY id DESC")
    rows = cur.fetchall()
    todos = [{"id": r[0], "title": r[1]} for r in rows]
    return jsonify(todos)

@app.route("/api/todos", methods = ['POST'])
def add_todo():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or request.form.get("title") or "").strip()
    if not title:
        return jsonify({"error": "title is required"}), 400
    
    conn, cur = get_conn_cursor()
    cur.execute("INSERT INTO todos (title) VALUES (%s);", (title,))
    conn.commit()
    return jsonify({'ok': True}), 201

@app.route("/api/todos/<int:todo_id>/delete", methods = ['POST'])
def delete(todo_id):
    
    conn, cur = get_conn_cursor()
    cur.execute("DELETE FROM todos WHERE id = %s;", (todo_id,))
    conn.commit()

    return jsonify({'ok':True}), 200