from flask import Blueprint, request, url_for, flash, redirect, render_template

from flask_login import login_required, current_user

from recommendation.models import Physician, User, Category, Patient
from recommendation import db
from .forms import RegistrationForm



admin = Blueprint('admin', __name__, url_prefix="/admin")

@admin.route("/index")
@login_required
def index():
    physicians = Physician.query.all()
    return render_template("admin/admin-home.html", physicians = physicians)

@admin.route("/admin/physicians/add", methods = ["GET", "POST"])
@login_required
def add_physician():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,
            user_type = "physician"
        )
        
        physician = Physician(
            names = form.names.data,
            email = form.email.data
        )
        physician.user = user
        
        db.session.add(physician)
        db.session.commit()
        flash(f'Physician successfully created', 'success')
        
        return redirect(url_for('admin.index'))
        
    return render_template("admin/physician-form.html", form = form)


@admin.route("/add_categories")
def add_category():
    return render_template("categories.html")