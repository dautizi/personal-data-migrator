'''
Work Experience Bean
'''
import datetime

class WorkExperience:

    def __init__(self, id, role, company, description, period, company_image, company_thumb,
                 active, prg, creation_time, update_time):

        self.id = id
        self.role = role
        self.company = company
        self.description = description
        self.period = period
        self.company_image = company_image
        self.company_thumb = company_thumb
        self.active = active
        self.prg = prg
        self.creation_time = creation_time
        self.update_time = update_time

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_company(self):
        return self.company

    def set_company(self, company):
        self.company = company

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_description(self):
        return self.description

    def set_description(self, description):
        return self.description == description

    def get_period(self):
        return self.period

    def set_period(self, period):
        return self.period == period

    def get_company_image(self):
        return self.company_image

    def set_company_image(self, company_image):
        return self.company_image == company_image

    def get_company_thumb(self):
        return self.company_thumb

    def set_company_thumb(self, company_thumb):
        return self.company_thumb == company_thumb

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

        json = {'company': self.company,
                'role': self.role,
                'description': self.description,
                'period': self.period,
                'companyImage': self.company_image,
                'companyThumb': self.company_thumb,
                'active': active,
                'prg': self.prg,
                'datetime': isoCt,
                'lastUpdate': isoUt}
        return json