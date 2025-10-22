from flask import Flask
from db_config import mysql,init_db 
from routes.main_routes import main_bp
from routes.bmi_routes import bmi_bp
from routes.heart_routes import heart_bp
from routes.login_routes import login_bp
import os

app = Flask(__name__)
app.secret_key = "asasacddf1f2d15f4d5f5d4f55454212143@d4s5d4as" 

init_db(app)
# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(heart_bp)
app.register_blueprint(bmi_bp)
app.register_blueprint(login_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
