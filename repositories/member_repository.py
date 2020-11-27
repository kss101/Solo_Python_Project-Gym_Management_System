from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, date_of_birth, membership_num) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.date_of_birth, member.membership_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)