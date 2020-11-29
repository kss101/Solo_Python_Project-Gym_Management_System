from flask import Blueprint, Flask, redirect, render_template, request

from controllers.members_controller import members_blueprint
from controllers.fitness_classes_controller import fitness_classes_blueprint
from controllers.bookings_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(fitness_classes_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()