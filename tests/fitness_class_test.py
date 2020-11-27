import unittest
from models.fitness_class import FitnessClass

class TestFitnessClass(unittest.TestCase):
    
    def setUp(self):
        self.fitness_class = FitnessClass("Spin", "Cardio", 45)
    
    def test_member_created(self):
        self.assertEqual("Spin", self.fitness_class.title)