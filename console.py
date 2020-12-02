import pdb

from models.member import Member
import repositories.member_repository as member_repository
from models.fitness_class import FitnessClass
import repositories.fitness_class_repository as fitness_class_repository
from models.booking import Booking
import repositories.booking_repository as booking_repository
from models.fitness_class_type import FitnessClassType
import repositories.fitness_class_type_repository as type_repository


member_repository.delete_all()
fitness_class_repository.delete_all()

member_1 = Member("Bob", "Anders", "1980-01-10", 1, "Standard")
member_repository.save(member_1)

member_2 = Member("Clare", "Bower", "1985-02-15", 2, "Standard")
member_repository.save(member_2)

member_3 = Member("Jim", "Adler", "1970-05-20", 3, "Premium")
member_repository.save(member_3)

member_4 = Member("Mark", "Bishop", "1990-10-19", 4, "Premium")
member_repository.save(member_4)

class_1 = FitnessClass("Yoga", "Conditioning", 45, "A spiritual discipline which includes breath control, meditation, and the adoption of specific postures to aid health and relaxation.")
fitness_class_repository.save(class_1)

class_2 = FitnessClass("Lunchtime Pilates", "Conditioning", 30, "A shorter version of our popular exercise class which helps build strength from the inside out, rebalancing the body and bringing it into alignment. mins.")
fitness_class_repository.save(class_2)

class_3 = FitnessClass("Pilates", "Conditioning", 60, "A popular exercise class which helps build strength from the inside out, rebalancing the body and bringing it into alignment. Pilates helps to reshape your body, which will become leaner and more toned as a result of undertaking this class. It will also improve your posture, achieving the perfect balance between strength and flexibility. mins.")
fitness_class_repository.save(class_3)

class_4 = FitnessClass("BODYATTACK™", "HIIT", 55, "BODYATTACK™ is an intense sports inspired cardio workout aimed at building both your strength and stamina. It is an energetic interval training session which combines aerobic movements with strength and stabilization exercises.")
fitness_class_repository.save(class_4)

class_5 = FitnessClass("KettleBells", "Gym Floor", 40, "A full body instructor-led workout using kettlebells to tone and condition your body")
fitness_class_repository.save(class_5)

class_6 = FitnessClass("Legs, Bums & Tums", "Conditioning", 30, "A popular group exercise class which targets the legs, bum and tum area to shape and tone the body")
fitness_class_repository.save(class_6)

class_type_1 = FitnessClassType("Cardio")
type_repository.save(class_type_1)
class_type_2 = FitnessClassType("Gym Floor")
type_repository.save(class_type_2)
class_type_3 = FitnessClassType("H.I.I.T.")
type_repository.save(class_type_3)
class_type_4 = FitnessClassType("L.I.I.T.")
type_repository.save(class_type_4)
class_type_5 = FitnessClassType("Conditioning")
type_repository.save(class_type_5)

booking_1 = Booking(1,1)
booking_repository.save(booking_1)

pdb.set_trace()