from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    return render_template("members/index.html")

# Get All Members
@members_blueprint.route("/members/all")
def all_members():
    members = member_repository.select_all()
    return render_template("members/all.html", members=members)

# Get specific Member
@members_blueprint.route('/members/<id>/show')
def show_member(id):
    member = member_repository.select(id)
    return render_template("members/show.html", member=member)

# Add New Member
# GET '/members/new' --> show html form to create a new member
@members_blueprint.route("/members/new", methods=["GET"])
def new_member():
    return render_template("members/new.html")

# POST '/members' --> handle the POST from the new memebr form
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    membership_num = request.form['membership_num']
    membership_num_check = member_repository.check_membership_num_exists(membership_num)
    print("Found the following: ", membership_num_check)
    if membership_num_check == False:
        member = Member(first_name, last_name, date_of_birth, membership_num)
        member_repository.save(member)
        return redirect('/members')
    else:
        message = "Membership no." + membership_num + " is already in use. Please try again"
        return  render_template("members/new.html", message=message)

# Class Bookings
@members_blueprint.route("/members/<id>/bookings/")
def bookings(id):
    member = member_repository.select(id)
    bookings = member_repository.bookings(member)
    return render_template("members/bookings.html", bookings=bookings, member=member)

# Delete a member from the system
@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")