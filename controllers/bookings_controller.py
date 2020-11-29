from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings/new")
def booking():
    return render_template("bookings/new.html")

# Class Bookings
@bookings_blueprint.route("/members/<id>/bookings/")
def bookings(id):
    member = member_repository.select(id)
    bookings = member_repository.bookings(member)
    return render_template("members/bookings.html", bookings=bookings, member=member)