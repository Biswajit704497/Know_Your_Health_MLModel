from flask import Blueprint, render_template, session, redirect, url_for
register_bp = Blueprint('register_bp',__name__)

@register_bp.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')