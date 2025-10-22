from flask import Blueprint, render_template, session, redirect,url_for, request, flash
from db_config import mysql
login_bp = Blueprint('login_bp',__name__)

@login_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cur = mysql.connect.cursor()
        cur.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            session["user_id"] = username
            print("Login successful!", "success")
            return "wellcome"
        else:
            print("Invalid username or password", "danger")
    return render_template('login.html')    