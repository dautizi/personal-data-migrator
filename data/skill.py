'''
Skill Bean
'''
import datetime

class Skill:

    def __init__(self, id, group_name, title, progress, percentage, years, since, image_url,
                 active, prg, creation_time, update_time):

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
        self.creation_time = creation_time
        self.update_time = update_time

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

    def get_creation_time(self):
        return self.creation_time

    def set_creation_time(self, creation_time):
        return self.creation_time == creation_time

    def get_last_update(self):
        return self.update_time

    def set_update_time(self, update_time):
        return self.update_time == update_time

    def to_json(self):
        active = True if self.active > 0 else False

        ct = datetime.datetime.strptime(self.creation_time, "%Y-%m-%d %H:%M:%S")
        isoCt = datetime.datetime.fromtimestamp(ct.timestamp(), None)
        ut = datetime.datetime.strptime(self.update_time, "%Y-%m-%d %H:%M:%S")
        isoUt = datetime.datetime.fromtimestamp(ut.timestamp(), None)
        st = datetime.datetime.strptime(self.since, "%Y-%m-%d %H:%M:%S")
        isoSt = datetime.datetime.fromtimestamp(st.timestamp(), None)

        json = {'groupName': self.group_name,
                'title': self.title,
                'progress': self.progress,
                'percentage': self.percentage,
                'years': self.years,
                'since': isoSt,
                'imageUrl': self.image_url,
                'active': active,
                'prg': self.prg,
                'datetime': isoCt,
                'lastUpdate': isoUt}
        return json