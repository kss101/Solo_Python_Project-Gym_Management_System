from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)
#INDEX
@bookings_blueprint.route("/bookings")
def booking():
    return render_template("bookings/index.html")

# View a Member's Fitness Class Bookings
@bookings_blueprint.route("/members/<id>/bookings/")
def bookings(id):
    member = member_repository.select(id)
    fitness_classes = member_repository.bookings(member)[0]
    bookings = member_repository.bookings(member)[1]
    return render_template("/members/bookings.html", bookings=bookings, fitness_classes=fitness_classes, member=member)

# Add New Fitness Class Booking
# GET '/bookings/new' --> show html form to create a new booking
@bookings_blueprint.route("/bookings/<id>/new", methods=["GET"])
def new_booking(id):
    member = member_repository.select(id)
    fitness_classes = fitness_class_repository.select_all()
    return render_template("bookings/new.html", member=member, fitness_classes=fitness_classes)

# POST '/bookings' --> handle the POST from the new bookings form
@bookings_blueprint.route("/members/<id>/bookings/", methods=["POST"])
def create_bookins(id):
    member = member_repository.select(id)
    print("Class Id is: ", request.form['fitness_class'])
    fitness_class_id = request.form['fitness_class']
    booking = Booking(member.id, fitness_class_id)
    booking_repository.save(booking)
    bookings = member_repository.bookings(member)
    fitness_classes = member_repository.bookings(member)[0]
    # return render_template("/members/bookings.html", bookings=bookings, member=member)
    return render_template("/members/bookings.html", bookings=bookings, fitness_classes=fitness_classes, member=member)


# Delete a Member's Fitness Class booking from the system
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_member(id):
    print("ID is ", id)
    booking_repository.delete(id)
    return redirect("/members")