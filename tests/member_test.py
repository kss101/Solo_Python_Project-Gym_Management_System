import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member("Kurt", "Steffan", "27/05/1973", 1)
    
    def test_member_created(self):
        self.assertEqual("Kurt", self.member.first_name)