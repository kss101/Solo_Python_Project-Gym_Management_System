from flask import Blueprint, Flask, redirect, render_template, request

from models.fitness_class import FitnessClass
import repositories.fitness_class_repository as fitness_class_repository

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)

# INDEX
@fitness_classes_blueprint.route("/classes")
def fitness_classes():
    fitness_classes = fitness_class_repository.select_all()
    return render_template("fitness_classes/index.html", fitness_classes=fitness_classes)