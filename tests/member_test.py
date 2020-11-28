import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member("Kurt", "Steffan", "1973-05-27", 1)
    
    def test_member_created(self):
        self.assertEqual("Kurt", self.member.first_name)

    def test_member_full_name(self):
        self.assertEqual("Kurt Steffan", self.member.full_name(self.member.first_name, self.member.last_name))