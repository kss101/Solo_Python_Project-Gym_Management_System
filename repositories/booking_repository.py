from db.run_sql import run_sql
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

def save(booking):
    sql = "INSERT INTO fitness_class_member_bookings (member_id, fitness_class_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member_id, booking.fitness_class_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id
    return booking

def select(id):
    sql = "SELECT * FROM fitness_class_member_bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        booking = Booking(result['member_id'], result['fitness_class_id'], result['id'] )
    return booking

def delete_all():
    sql = "DELETE FROM fitness_class_member_bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fitness_class_member_bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def get_fitness_class_bookings(fitness_class):
    members= []
    bookings = []

    sql = "SELECT fitness_class_member_bookings.id AS booking_id, members.* FROM members INNER JOIN fitness_class_member_bookings ON fitness_class_member_bookings.member_id = member.id WHERE fitness_class.id = %s"
    values = [fitness_class.id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row['title'], row['type'], row['duration'], row['id'] )
        members.append(member)
        bookings.append(row['booking_id'])

    return (members, bookings)