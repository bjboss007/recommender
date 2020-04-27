from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import  current_user, login_user, logout_user

from recommendation import db, bcrypt
from recommendation.user.forms import LoginForm
from recommendation.models import User, Physician, Patient

main = Blueprint('main', __name__)



@main.route('/', methods = ["GET", "POST"])
@main.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        flash(f'You are already logged in ','info')
        return redirect(url_for('users.account'))
    
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            
            if next_page  :
                return redirect(next_page) 
            else:
                if (current_user.email == "admin@admin.com" and current_user.user_type == "admin"):
                    return redirect(url_for('admin.index'))
                elif(current_user.user_type == "physician"):
                    return redirect(url_for('physician.index'))
                else:
                    patient = Patient.query.get_or_404(current_user.patient_id)
                    if patient.score != None:
                        return redirect(url_for('users.account'))
                    else:
                        return redirect(url_for('users.question'))
        else:
            flash(f'Login Unsuccessful, Please check your email and password ','danger')
    return render_template("login.html", title = 'Login', form=form)


@main.route("/logout", methods = ["GET"])
def logout():
    logout_user()
    return redirect(url_for('main.login'))
