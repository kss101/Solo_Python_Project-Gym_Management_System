from flask import Blueprint, Flask, redirect, render_template, request

from models.fitness_class import FitnessClass
import repositories.fitness_class_repository as fitness_class_repository

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)

# INDEX
@fitness_classes_blueprint.route("/classes")
def fitness_classes():
    return render_template("fitness_classes/index.html")


# View ALL Fitness Classes
@fitness_classes_blueprint.route("/classes/all")
def all_fitness_classes():
    fitness_classes = fitness_class_repository.select_all()
    return render_template("fitness_classes/all.html", fitness_classes=fitness_classes)


# View specific Fitness Class
@fitness_classes_blueprint.route('/classes/<id>/show')
def show_fitness_class(id):
    fitness_class = fitness_class_repository.select(id)
    return render_template("fitness_classes/show.html", fitness_class=fitness_class)


# Add New Fitness Class
# GET '/classes/new' --> show html form to create a new fitness class
@fitness_classes_blueprint.route("/classes/new", methods=["GET"])
def new_class():
    return render_template("fitness_classes/new.html")


# POST '/classes' --> handle the POST from the new fitness class form
@fitness_classes_blueprint.route("/classes", methods=["POST"])
def create_fitness_class():
    title= request.form['title']
    type = request.form['type']
    duration = request.form['duration']
    discription = request.form['discription']
    fitness_class = FitnessClass(title, type, duration, discription)
    fitness_class_repository.save(fitness_class)
    return redirect('/classes')


# EDIT
@fitness_classes_blueprint.route("/classes/<id>/edit")
def edit_fitness_class(id):
    fitness_class = fitness_class_repository.select(id)
    return render_template('fitness_classes/edit.html', fitness_class=fitness_class)


# UPDATE Fitness Class
@fitness_classes_blueprint.route("/classes/<id>", methods=["POST"])
def update__fitness_class(id):
    title = request.form['title']
    type = request.form['type']
    duration = request.form['duration']
    discription = request.form['discription']
    fitness_class = FitnessClass(title, type, duration, discription, id)
    fitness_class_repository.update(fitness_class)
    return render_template("/fitness_classes/show.html", fitness_class=fitness_class)


# DELETE a Fitness Class from the system
@fitness_classes_blueprint.route("/classes/<id>/delete", methods=["POST"])
def delete_fitness_class(id):
    fitness_class_repository.delete(id)
    return redirect("/classes/all")