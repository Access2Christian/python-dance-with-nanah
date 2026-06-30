import os
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "nanah_python_dance_strong_finish"

# 1. DATABASE SETUP
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'miva_nexus.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'tbl_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # Profile Data collected from Dashboard
    full_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    course = db.Column(db.String(100))
    skills = db.Column(db.String(200))
    story = db.Column(db.Text) # This is the "Line" or story

# Static Legends to keep the directory looking full
LEGENDS = [
    {"username": "chidubem", "name": "Chidubem", "age": 24, "course": "Backend Eng", "skills": "Python, Flask, SQL", "story": "The first to dance with Python in Enugu."},
    {"username": "aisha", "name": "Aisha", "age": 22, "course": "Data Science", "skills": "Pandas, Stats", "story": "Visualizing the rhythm of the North."}
]

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uname = request.form.get('username')
        pwd = request.form.get('password')
        if User.query.filter_by(username=uname).first():
            flash("Username already taken!", "warning")
            return redirect(url_for('signup'))
        
        hashed = generate_password_hash(pwd, method='pbkdf2:sha256')
        new_user = User(username=uname, password=hashed)
        db.session.add(new_user)
        db.session.commit()
        
        # Auto-login after registration
        session['user'] = uname
        flash("Registration Successful! Welcome to your Dashboard.", "success")
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        uname = request.form.get('username')
        pwd = request.form.get('password')
        user = User.query.filter_by(username=uname).first()
        if user and check_password_hash(user.password, pwd):
            session['user'] = uname
            return redirect(url_for('home'))
        flash("Invalid Credentials", "danger")
    return render_template('signin.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session: return redirect(url_for('signin'))
    user = User.query.filter_by(username=session['user']).first()

    if request.method == 'POST':
        user.full_name = request.form.get('full_name')
        user.age = request.form.get('age')
        user.course = request.form.get('course')
        user.skills = request.form.get('skills')
        user.story = request.form.get('story')
        db.session.commit()
        flash("Your profile is live! Shaking the directory now.", "success")
        return redirect(url_for('profile'))

    return render_template('home.html', user=user)

@app.route('/profile')
def profile():
    # Only show recruits who have completed their details
    recruits = User.query.filter(User.full_name != None).all()
    return render_template('profile.html', legends=LEGENDS, recruits=recruits)

@app.route('/student/<username>')
def student(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template('student.html', s=user, is_db=True)
    
    for l in LEGENDS:
        if l['username'] == username:
            return render_template('student.html', s=l, is_db=False)
            
    return "Partner not found", 404

@app.route('/services')
def services(): return render_template('services.html')

@app.route('/about')
def about(): return render_template('about.html')

@app.route('/contact')
def contact(): return render_template('contact.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)