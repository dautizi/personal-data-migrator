'''
Image Bean
'''


class Image:

    def __init__(self, id, title, url, type, prg, active):

        self.id = id
        self.title = title
        self.url = url
        self.type = type
        self.prg = prg
        self.active = active

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_url(self):
        return self.url

    def set_url(self, url):
        return self.url == url

    def get_type(self):
        return self.type

    def set_type(self, type):
        return self.type == type

    def get_prg(self):
        return self.prg

    def set_prg(self, prg):
        return self.prg == prg

    def get_active(self):
        return self.active

    def set_active(self, active):
        return self.active == active