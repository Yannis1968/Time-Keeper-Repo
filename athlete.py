import datetime


class Athlete:
    def __init__(self, bib, name, surname, dob, gender, club, email, nationality, phone):
        self.bib = bib
        self.name = name
        self.surname = surname
        self.dob = dob
        self.gender = gender
        self.club = club
        self.email = email
        self.nationality = nationality
        self.phone = phone

    def get_age(self):
        age = int((datetime.datetime.now()).year) - int(self.dob)
        return age


