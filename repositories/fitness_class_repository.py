from db.run_sql import run_sql
from models.fitness_class import FitnessClass

def save(fitness_class):
    sql = "INSERT INTO fitness_classes (title, type, duration, discription) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [fitness_class.title, fitness_class.type, fitness_class.duration, fitness_class.discription]
    results = run_sql(sql, values)
    id = results[0]['id']
    fitness_class.id = id
    return fitness_class

def select_all():
    fitness_classes = []
    sql = "SELECT * FROM fitness_classes"
    results = run_sql(sql)
    for result in results:
        fitness_class = FitnessClass(result["title"], result["type"], result["duration"], result['discription'],result["id"])
        fitness_classes.append(fitness_class)
    return fitness_classes

def select(id):
    fitness_class = None
    sql = "SELECT * FROM fitness_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        fitness_class = FitnessClass(result['title'], result['type'], result['duration'], result['discription'], result['id'] )
    return fitness_class

def update(fitness_class):
    sql = "UPDATE fitness_classes SET (title, type, duration, discription = (%s, %s, %s, %s) WHERE id = %s"
    values = [fitness_class.title, fitness_class.type, fitness_class.duration, fitness_class.discription, fitness_class.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fitness_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)