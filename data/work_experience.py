'''
Work Experience Bean
'''


class WorkExperience:

    def __init__(self, id, company, role, description, period, company_image, company_thumb, start_year, end_year):

        self.id = id
        self.company = company
        self.role = role
        self.description = description
        self.period = period
        self.company_image = company_image
        self.company_thumb = company_thumb
        self.start_year = start_year
        self.end_year = end_year

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

    def get_start_year(self):
        return self.start_year

    def set_start_year(self, start_year):
        return self.start_year == start_year

    def get_end_year(self):
        return self.end_year

    def set_end_year(self, end_year):
        return self.end_year == end_year

    def to_json(self):
        active = True if self.active > 0 else False

        json = {'company': self.company,
                'role': self.role,
                'description': self.description,
                'period': self.period,
                'companyImage': self.company_image,
                'companyThumb': self.company_thumb,
                'startYear': self.start_year,
                'endYear': self.end_year,
                'active': active,
                'prg': self.prg,
                'datetime': self.datetime,
                'lastUpdate': self.last_update}
        return json