from db.run_sql import run_sql
from models.fitness_class import FitnessClass

def save(fitness_class):
    sql = "INSERT INTO fitness_classes (title, type, duration) VALUES (%s, %s, %s) RETURNING id"
    values = [fitness_class.title, fitness_class.type, fitness_class.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    fitness_class.id = id

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)