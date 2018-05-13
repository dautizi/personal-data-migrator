'''
Skill Bean
'''


class Skill:

    def __init__(self, id, group_name, title, progress, percentage, years, since, image_url, prg,
                 active, datetime, last_update):

        self.id = id
        self.group_name = group_name
        self.title = title
        self.progress = progress
        self.percentage = percentage
        self.years = years
        self.since = since
        self.image_url = image_url
        self.prg = prg
        self.active = active
        self.datetime = datetime
        self.last_update = last_update

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_group_name(self):
        return self.group_name

    def set_group_name(self, group_name):
        self.group_name = group_name

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_progress(self):
        return self.progress

    def set_progress(self, progress):
        return self.progress == progress

    def get_percentage(self):
        return self.percentage

    def set_percentage(self, percentage):
        return self.percentage == percentage

    def get_years(self):
        return self.years

    def set_years(self, years):
        return self.years == years

    def get_since(self):
        return self.since

    def set_since(self, since):
        return self.since == since

    def get_image_url(self):
        return self.image_url

    def set_image_url(self, image_url):
        return self.image_url == image_url

    def get_prg(self):
        return self.prg

    def set_prg(self, prg):
        return self.prg == prg

    def get_active(self):
        return self.active

    def set_active(self, active):
        return self.active == active

    def get_datetime(self):
        return self.datetime

    def set_datetime(self, datetime):
        return self.datetime == datetime

    def get_last_update(self):
        return self.last_update

    def set_last_update(self, last_update):
        return self.last_update == last_update

    def to_json(self):
        active = True if self.active > 0 else False

        json = {'groupName': self.group_name,
                'title': self.title,
                'progress': self.progress,
                'percentage': self.percentage,
                'years': self.years,
                'since': self.since,
                'imageUrl': self.image_url,
                'active': active,
                'prg': self.prg,
                'datetime': self.datetime,
                'lastUpdate': self.last_update}
        return json