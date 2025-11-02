from flask import Blueprint, render_template, session, redirect, url_for, request
register_bp = Blueprint('register_bp',__name__)
from db_config import mysql
@register_bp.route('/register',methods=['GET','POST'])
def register():

    if request.method == 'POST':
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        fullname = request.form.get("full_name")
        username = request.form.get("username")
        password = request.form.get("password")
        #database connection
        user_data = (
            email,
            phone_number,
            fullname,
            username,
            password
        )
        sql_query = """
            INSERT INTO user(email,phone_number,fullname,username,password)
            VALUES(%s, %s, %s , %s , %s )

        """
        cur = None
        conn = None
        try:
            conn = mysql.connect
            cur = conn.cursor()
            cur.execute(sql_query, user_data)
            conn.commit()
            print("Database Connection Successfully")
            return redirect(url_for("login_bp.login"))
        except Exception as e:
            print("database connection probleam",e)
        

        

    return render_template('register.html')