from flask import Blueprint, render_template, request
from bmi_calculate import BMI_def

bmi_bp = Blueprint('bmi_bp', __name__)

@bmi_bp.route("/BMI", methods=['GET', 'POST'])
def BMI():
    person_bmi = []
    if request.method == 'POST':
        weight = int(request.form.get('weight', 0))
        height = int(request.form.get('height', 0))
        person_bmi = BMI_def(height, weight)

    return render_template('bmi.html', person_bmi=person_bmi)
