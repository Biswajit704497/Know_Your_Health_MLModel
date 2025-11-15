from flask import Blueprint, render_template
diabetes_bp = Blueprint('diabetes_bp',__name__)

@diabetes_bp.route("/diabetes")
def diabetes():
    
    return render_template("diabetes.html")

