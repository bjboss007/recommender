
from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import  current_user, login_user, logout_user, login_required
from recommendation.models import User, Question, Remedy, Category
from recommendation.user.forms import LoginForm, RegistrationForm
from recommendation import db, bcrypt
from recommendation.utils import parseData, get_rating, getKey



users = Blueprint('users', __name__)

@users.route('/', methods = ["GET", "POST"])
@users.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        flash(f'You are already logged in ','info')
        return redirect(url_for('users.account'))
    
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember = form.remember.data)
            # if (current_user.email == "admin@gmail.com" and current_user.username == "Admin"):
            #     return redirect(url_for('admin.usersListView'))
            # else:
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash(f'Login Unsuccessful, Please check your email and password ','danger')
    return render_template("login.html", title = 'Login', form=form)


@users.route("/register", methods = ["GET", "POST"])
def register():
    form  = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data,
            sex = form.sex.data,
            date_of_birth = form.date_of_birth.data
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!','success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form = form)



@users.route("/users/account", methods = ["GET", "POST"])
@login_required
def account():
    user = User.query.get_or_404(current_user.id)
    return render_template("account.html", title = "Account page", user = user)

@users.route("/logout", methods = ["GET"])
def logout():
    logout_user()
    return redirect(url_for('users.login'))

@users.route("/question", methods = ["GET","POST"])
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
        return redirect(url_for('users.recommendation',category = category))
    return render_template('question.html', title = 'Question', questions = questions)
    
    
@users.route("/users/<category>/recommendation")
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

    return render_template('recommendation.html', title = "Recommendation page" , remedies = remedies_)

@users.route("/users/rating", methods = ["POST"])
def rating():
    if request.method == "POST":
        data = list(request.form.items())
        print("This is the data: ")
        print(data)
        # for remedy_id, rating in data:
        #     remendy = Remedy.query.get(remedy_id).first()
        #     rating = Rating(rating = rating)
        #     remendy.remendy_rating.append(rating)
        # db.session.commit()
        # return redirect(url_for('users.account'))
    return redirect(url_for('users.account'))
        
    
    
    