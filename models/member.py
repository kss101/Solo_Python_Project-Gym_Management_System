class Member:
    def __init__(self, first_name, last_name, date_of_birth, membership_num, membership_type, is_active=True, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.membership_num  = membership_num
        self.membership_type = membership_type
        self.is_active = is_active
        self.id = id

    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name
