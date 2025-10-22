from flask import Blueprint, render_template, request
from models.heart_model import heart_def

heart_bp = Blueprint('heart_bp', __name__)

@heart_bp.route("/heart_attack", methods=['GET', 'POST'])
def heart_attack():
    result = None  

    if request.method == 'POST':
        age = int(request.form.get('age', 0))
        gender = int(request.form.get('gender', 0))
        cholesterol = int(request.form.get('cholesterol', 0))
        highBloodPressure = int(request.form.get('highBloodPressure', 0))
        lowBloodPressure = int(request.form.get('lowBloodPressure', 0))
        heartRate = int(request.form.get('heartRate', 0))
        diabetes = int(request.form.get('diabetes', 0))
        familyHistory = int(request.form.get('familyHistory', 0))
        smoking = int(request.form.get('smoking', 0))
        alcoholConsumption = int(request.form.get('alcoholConsumption', 0))
        exerciseHours = int(request.form.get('exerciseHours', 0))
        diet = int(request.form.get('diet', 0))
        previousHeartProblems = int(request.form.get('previousHeartProblems', 0))
        medicationUse = int(request.form.get('medicationUse', 0))
        stressLevel = int(request.form.get('stressLevel', 0))
        bmi = float(request.form.get('bmi', 0))
        physicalActivityDays = int(request.form.get('physicalActivityDays', 0))
        sleepHours = int(request.form.get('sleepHours', 0))

        heart_rate_data_list = [[
            age, gender, cholesterol, highBloodPressure, lowBloodPressure,
            heartRate, diabetes, familyHistory, smoking, alcoholConsumption,
            exerciseHours, diet, previousHeartProblems, medicationUse,
            stressLevel, bmi, physicalActivityDays, sleepHours
        ]]

        result = heart_def(heart_rate_data_list)

    return render_template("heart.html", result=result)
