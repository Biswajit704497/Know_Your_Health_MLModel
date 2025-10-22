# import joblib
# # {'age': '43', 'gender': '1', 'cholesterol': '22', 'highBloodPressure': '223', 'lowBloodPressure': '33', 'heartRate': '221', 'diabetes': '1', 'familyHistory': '1', 'smoking': '1', 'alcoholConsumption': '1', 'exerciseHours': '2323', 'diet': '0', 'previousHeartProblems': '1', 'medicationUse': '1', 'stressLevel': '3232', 'bmi': '32', 'physicalActivityDays': '322', 'sleepHours': '111'}

# model = joblib.load('../models/HeartPred.joblib')
# def heart_def(data):
#     return model.predict(data)


# #main
# if __name__ == '__main__':

#     print(heart_def([[1,4,4,4,4,8,1,4,4,4,4,8,8,1,4,4,4,4]]))

import os
import joblib

# Get path of this file's directory (models/)
BASE_DIR = os.path.dirname(__file__)

# Full path to your model file
MODEL_PATH = os.path.join(BASE_DIR, 'HeartPred.joblib')

# Load the model
model = joblib.load(MODEL_PATH)

def heart_def(data):
    return model.predict(data)

# For local test
if __name__ == "__main__":
    print(heart_def([[1, 4, 4, 4, 8, 1, 4, 4, 4, 8, 8, 1, 4, 4, 4, 4, 4, 4]]))
