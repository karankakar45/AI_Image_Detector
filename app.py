from predict import predict_image
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import random

app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = 'secretkey123'

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Upload Folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize Database
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User Model
class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)

# Load User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# First Page → Login
@app.route('/')
def first():
    return redirect(url_for('login'))

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Encrypt Password
        hashed_password = generate_password_hash(password)

        # Create User
        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        # Save To Database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration Successful')

        return redirect(url_for('login'))

    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        # Find User
        user = User.query.filter_by(email=email).first()

        # Check Password
        if user and check_password_hash(user.password, password):

            login_user(user)

            return redirect(url_for('home'))

        else:
            flash('Invalid Email or Password')

    return render_template('login.html')

# Home Route (AI Detector Page)
@app.route('/home')
@login_required
def home():
    return render_template('index.html', name=current_user.username)

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    if not allowed_file(file.filename):
        return jsonify({'error': 'Only jpg/png allowed'})

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    prediction, confidence = predict_image(filepath)

    return jsonify({
        'prediction': str(prediction),
        'confidence': float(confidence)
    })

# Logout Route
@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for('login'))

# Run App
if __name__ == '__main__':

    # Create Database
    with app.app_context():
        db.create_all()

    app.run(debug=True)
