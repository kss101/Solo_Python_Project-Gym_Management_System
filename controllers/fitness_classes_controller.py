from flask import Blueprint, Flask, redirect, render_template, request

from models.fitness_class import FitnessClass
import repositories.fitness_class_repository as fitness_class_repository


fitness_classes_blueprint = Blueprint("fitness_classes", __name__)

# INDEX
@fitness_classes_blueprint.route("/classes")
def fitness_classes():
    fitness_classes = fitness_class_repository.select_all()
    return render_template("fitness_classes/index.html", fitness_classes=fitness_classes)

# Add New Fitness Class
# GET '/classes/new' --> show html form to create a new fitness class
@fitness_classes_blueprint.route("/classes/new", methods=["GET"])
def new_class():
    return render_template("fitness_classes/new.html")

# POST '/members' --> handle the POST from the new memebr form
@fitness_classes_blueprint.route("/classes", methods=["POST"])
def create_fitness_class():
    title= request.form['title']
    type = request.form['type']
    duration = request.form['duration']
    fitness_class = FitnessClass(title, type, duration)
    fitness_class_repository.save(fitness_class)
    return redirect('/classes')