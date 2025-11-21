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
        # if already logged in, redirect to home
        if session.get("user"):
            return redirect(url_for('main_bp.home'))
        if user:
            session["user"] = username
            flash("Login successful!", "success")
            return redirect(url_for('main_bp.home'))
        else:
            flash("Invalid username or password", "danger")
    return render_template('login.html')    

@login_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logout...... ")
    return redirect(url_for('main_bp.home'))