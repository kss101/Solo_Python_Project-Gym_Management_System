from db.run_sql import run_sql
from models.fitness_class_type import FitnessClassType

def save(fitness_class_type):
    sql = "INSERT INTO fitness_class_types (class_type) VALUES (%s) RETURNING id"
    values = [fitness_class_type.class_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    fitness_class_type.id = id
    return fitness_class_type.id

def select_all():
    class_types = []
    sql = "SELECT * FROM fitness_class_types"
    results = run_sql(sql)
    for result in results:
        class_type = FitnessClassType(result["class_type"], result["id"])
        class_types.append(class_type)
    return class_types

