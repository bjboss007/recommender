from flask import Blueprint, request, render_template, url_for, flash, redirect, session
from flask_login import current_user, login_required

from recommendation import db
from recommendation.models import User, Remedy, Category, Rating, Patient, History, PatientRecom


physician =  Blueprint('physician', __name__, url_prefix="/physician")

@physician.route("/index")
@login_required
def index():
    user_list = []
    histories = History.query.filter_by(status = False).all()
    
    for history in histories:
        user = Patient.query.get(history.patient_id)
        if user != None:
            user_list.append(user)
    return render_template("physician/index.html", histories = user_list)

@physician.route("/users/<int:id>/details", methods = ["GET", "POST"])
@login_required
def show_user_details(id):
    patient = Patient.query.get_or_404(id)
    categories = Category.query.all()
    
    if request.method == "POST":
        data = request.form.lists()
        data_value = {}
        for k,v in data:
            data_value[k] = v[0]
            
        histories  = History.query.all()
        for history in histories:
            if history.patient_id == int(data_value["patient_id"]):
                history.status = True
                db.session.commit()
               
        patient_recomm = PatientRecom(
            physician_id = current_user.physician_id,
            category_id = data_value["category"],
            patient_id = data_value["patient_id"]
        )
        
        db.session.add(patient_recomm)
        db.session.commit()
        
        return redirect(url_for('physician.index'))
        
    return render_template("physician/user_detail.html", category = categories, patient = patient)
