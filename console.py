import pdb

from models.member import Member
import repositories.member_repository as member_repository
from models.fitness_class import FitnessClass
import repositories.fitness_class_repository as fitness_class_repository
from models.booking import Booking
import repositories.booking_repository as booking_repository


member_repository.delete_all()
fitness_class_repository.delete_all()

member_1 = Member("Kurt", "Steffan", "1973-05-27", 1)
member_repository.save(member_1)

class_1 = FitnessClass("Spin", "Cardio", 45)
fitness_class_repository.save(class_1)

booking_1 = Booking(1,1)
booking_repository.save(booking_1)

pdb.set_trace()