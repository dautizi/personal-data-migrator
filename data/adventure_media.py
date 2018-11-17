'''
Adventure Media Bean
'''
import datetime

class AdventureMedia:

    def __init__(self, id, media_type, media_path, media_url, title, alt, css_class, prg,
                 active, datetime, last_update):

        self.id = id
        self.media_type = media_type
        self.media_path = media_path
        self.media_url = media_url
        self.title = title
        self.alt = alt
        self.css_class = css_class
        self.prg = prg
        self.active = active
        self.datetime = datetime
        self.last_update = last_update

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_media_type(self):
        return self.media_type

    def set_media_type(self, media_type):
        self.media_type = media_type

    def get_media_path(self):
        return self.media_path

    def set_media_path(self, media_path):
        self.media_path = media_path

    def get_media_url(self):
        return self.media_url

    def set_media_url(self, media_url):
        return self.media_url == media_url

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_alt(self):
        return self.alt

    def set_alt(self, alt):
        return self.alt == alt

    def get_css_class(self):
        return self.css_class

    def set_css_class(self, css_class):
        return self.css_class == css_class

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

        ct = datetime.datetime.strptime(self.datetime, "%Y-%m-%d %H:%M:%S")
        isoCt = datetime.datetime.fromtimestamp(ct.timestamp(), None)
        ut = datetime.datetime.strptime(self.last_update, "%Y-%m-%d %H:%M:%S")
        isoUt = datetime.datetime.fromtimestamp(ut.timestamp(), None)

        json = {'mediaType': self.media_type,
                'mediaPath': self.media_path,
                'mediaUrl': self.media_url,
                'title': self.title,
                'alt': self.alt,
                'cssClass': self.css_class,
                'active': active,
                'prg': self.prg,
                'datetime': isoCt,
                'lastUpdate': isoUt}
        return json