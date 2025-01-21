from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from views.auth import auth_bp
from views.user import user_bp
from views.task import task_bp


# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a secure key in production

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(task_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    app.run(debug=True)
