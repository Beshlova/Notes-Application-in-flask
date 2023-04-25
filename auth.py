from flask import Blueprint, render_template,flash,redirect,url_for
from .forms import RegistrationForm,LoginForm,RequestResetForm,ResetPasswordForm
from .models import User
from flask_bcrypt import generate_password_hash, check_password_hash
from . import db, login_manager,bcrypt,mail
from flask_login import login_user, logout_user, current_user
import re


auth = Blueprint('auth', __name__)

#Complexity standards for username and password fields
username_regex = r"^(?=.{2,50}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$"
password_regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])(?=.*[a-zA-Z]).{8,}$'


#Keeps track of the user in session by grabbing the id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#The page for user authentication(registration form)
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            flash('Passwords must match!', category='error')
        elif User.query.filter_by(username=username).first():
            flash('An account with that username already exists!', category='error')
        elif User.query.filter_by(email=email).first():
            flash('An account with that email already exists!', category='error')
        elif not re.match(password_regex, password):
            flash('Password must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character!', 
                  category='error')
        elif not re.match(username_regex,username):
            flash("The username must be at least 2 characters long,must not start with an underscore or a period,must not contain consecutive underscores or periods!",
                  category='error')
        else:
            hashed_password = bcrypt.generate_password_hash(
                password).decode('utf-8')
            user = User(username=username, email=email,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form, user=current_user)

#The page for user verification(login page)
@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if  form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, form.password.data):
               login_user(user)
               flash('Logged in!', category='success')
               return redirect(url_for('views.home'))
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('User by that email does not exist.You may want to follow the sign up link below to register!',
                   category='error')

    return render_template('login.html', form=form, user=current_user)


#The route for logging out the user
@auth.route('/logout')
def logout():
   logout_user()
   flash('You have been logged out!',category='info')
   return redirect(url_for('auth.login'))
