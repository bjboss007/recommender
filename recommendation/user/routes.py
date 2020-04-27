
from flask import Blueprint, render_template, url_for, flash, redirect, request,session
from flask_login import  current_user, login_user, logout_user, login_required

from recommendation import db, bcrypt
from recommendation.utils import parseData, get_rating, getKey
from recommendation.models import User, Question, Remedy, Category, Rating, Patient, History, PatientRecom, Physician
from recommendation.user.forms import LoginForm, RegistrationForm



users = Blueprint('users', __name__)



@users.route("/register", methods = ["GET", "POST"])
def register():
    form  = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,
            user_type = "regular"
        )
        patient = Patient(
            email = form.email.data,
            names = form.names.data,
            sex = form.sex.data,
            date_of_birth = form.date_of_birth.data
        )
        patient.user = user
        db.session.add(patient)
        db.session.commit()
        flash(f'Your account has been created!','success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form = form)



@users.route("/users/account", methods = ["GET", "POST"])
@login_required
def account():
    # user = User.query.get_or_404(current_user.id)
    patient = Patient.query.get_or_404(current_user.patient_id)
    print(patient)
    status = patient.history.status
    return render_template("account.html", title = "Account page", user = patient, status = status)



@users.route("/question", methods = ["GET","POST"])
@login_required
def question():
    import random
    questions = Question.query.all()
    random.shuffle(questions)
    incoming = {}
    if request.method == "POST":
        count = 0
        for i,j in request.form.lists():
            incoming[i] = j[0]
        print(incoming)
        for question in questions:
            for i in incoming.keys():
                if question.id == int(i):
                    if incoming[i] == question.answer:
                        count+=1      
        category = parseData(count)
        history = History()
        patient = Patient.query.get_or_404(current_user.patient_id)
        patient.score = count
        history.patient_id = current_user.patient_id
        db.session.add(history)
        db.session.commit()
        flash(f'You response has been submitted, check your dashboard after 2hours ','info')
        return redirect(url_for('users.account'))
    return render_template('question.html', title = 'Question', questions = questions)
    
    
@users.route("/users/<category>/recommendation")
@login_required
def recommendation(category):
    remedies_ = None 
    category = Category.query.filter_by(name = category).first()
    remedies = category.remedies
    rated_remedies = {}
    for remedy in remedies:
        rated_remedies[remedy.title] = [x.rating for x in remedy.remedy_ratings]
    
    length = max([len(j) for j in list(rated_remedies.values())])
    if length < 5:
        remedies_ = remedies
    else:
        maxi, maximum = get_rating(rated_remedies)
        key = getKey(maxi, maximum)
        remedy = Remedy.query.filter_by(title = key).first()
        remedies_ = remedy
    return render_template('recommendation.html', title = "Recommendation page" , remedies = remedies_, category = category)

@users.route("/users/rating", methods = ["POST"])
def rating():
    if request.method == "POST":
        data = list(request.form.items())
        print("This is the data: ")
        print(data)
        for physician_id, rating in data:
            if rating == '':
                continue
            physician = Physician.query.get(int(physician_id))
            rating = Rating(rating = int(rating))
            print(rating.rating)
            physician.physician_ratings.append(rating)
        db.session.commit()
        return redirect(url_for('users.account'))
    return redirect(url_for('users.account'))


@users.route("/users/recommendation")
def show_recommendation():
    patient_recomm = PatientRecom.query.filter_by(patient_id = current_user.patient_id).first()
    
    physician = Physician.query.get_or_404(patient_recomm.physician_id)
    category = Category.query.get_or_404(patient_recomm.category_id)
    remedies = category.remedies
    
    return render_template("recommendation_.html", physician = physician, remedies = remedies, category = category)
    
    
    