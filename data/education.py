'''
Education Bean
'''
import datetime

class Education:

    def __init__(self, id, school, title, description, school_image, school_thumb,
                 period, start_year, end_year, prg, active, creation_time, update_time):

        self.id = id
        self.school = school
        self.title = title
        self.description = description
        self.school_image = school_image
        self.school_thumb = school_thumb
        self.period = period
        self.start_year = start_year
        self.end_year = end_year
        self.prg = prg
        self.active = active
        self.creation_time = creation_time
        self.update_time = update_time

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_school(self):
        return self.school

    def set_school(self, school):
        self.school = school

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        return self.description == description

    def get_school_image(self):
        return self.school_image

    def set_school_image(self, school_image):
        return self.school_image == school_image

    def get_school_thumb(self):
        return self.school_thumb

    def set_school_thumb(self, school_thumb):
        return self.school_thumb == school_thumb

    def get_period(self):
        return self.period

    def set_period(self, period):
        return self.period == period

    def get_start_year(self):
        return self.start_year

    def set_start_year(self, start_year):
        return self.start_year == start_year

    def get_end_year(self):
        return self.end_year

    def set_end_year(self, end_year):
        return self.end_year == end_year

    def get_prg(self):
        return self.prg

    def set_prg(self, prg):
        return self.prg == prg

    def get_active(self):
        return self.active

    def set_active(self, active):
        return self.active == active

    def get_creation_time(self):
        return self.creation_time

    def set_creation_time(self, creation_time):
        return self.creation_time == creation_time

    def get_update_time(self):
        return self.update_time

    def set_update_time(self, update_time):
        return self.update_time == update_time

    def to_json(self):
        active = True if self.active > 0 else False

        ct = datetime.datetime.strptime(self.creation_time, "%Y-%m-%d %H:%M:%S")
        isoCt = datetime.datetime.fromtimestamp(ct.timestamp(), None)
        ut = datetime.datetime.strptime(self.update_time, "%Y-%m-%d %H:%M:%S")
        isoUt = datetime.datetime.fromtimestamp(ut.timestamp(), None)

        json = {'school': self.school,
                'title': self.title,
                'description': self.description,
                'schoolImage': self.school_image,
                'schoolThumb': self.school_thumb,
                'period': self.period,
                'startYear': self.start_year,
                'endYear': self.end_year,
                'active': active,
                'prg': self.prg,
                'datetime': isoCt,
                'lastUpdate': isoUt}
        return json