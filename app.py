from flask import Flask
from routes.main_routes import main_bp
from routes.bmi_routes import bmi_bp
from routes.heart_routes import heart_bp
import os

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(heart_bp)
app.register_blueprint(bmi_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
