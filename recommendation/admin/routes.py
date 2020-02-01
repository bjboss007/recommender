from flask import Blueprint, request, url_for, flash, redirect, render_template



admin = Blueprint('admin', __name__, url_prefix="/admin")

@admin("/")
def index():
    return render_template("admin-home.html")

@admin("/add_categories")
def add_category():
    
    return render_template("categories.html")