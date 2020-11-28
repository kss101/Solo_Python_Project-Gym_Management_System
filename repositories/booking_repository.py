from db.run_sql import run_sql
from models.booking import Booking

def save(booking):
    sql = "INSERT INTO fitness_class_member_bookings (member_id, fitness_class_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member_id, booking.fitness_class_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id
    return booking

def delete_all():
    sql = "DELETE FROM fitness_class_member_bookings"
    run_sql(sql)