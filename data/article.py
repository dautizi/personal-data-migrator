'''
Article Bean
'''


class Article:

    def __init__(self, id, detail_path, url, header, image, thumb, title, summary, body, author,
                 active, prg, datetime, last_update, images):

        self.id = id
        self.detail_path = detail_path
        self.url = url
        self.header = header
        self.image = image
        self.thumb = thumb
        self.title = title
        self.summary = summary
        self.body = body
        self.author = author
        self.active = active
        self.prg = prg
        self.datetime = datetime
        self.last_update = last_update
        self.images = images

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_detail_path(self):
        return self.detail_path

    def set_detail_path(self, detail_path):
        self.detail_path = detail_path

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_image(self):
        return self.image

    def set_image(self, image):
        return self.image == image

    def get_thumb(self):
        return self.thumb

    def set_thumb(self, thumb):
        self.thumb = thumb

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_summary(self):
        return self.summary

    def set_summary(self, summary):
        return self.summary == summary

    def get_body(self):
        return self.body

    def set_body(self, body):
        return self.body == body

    def get_author(self):
        return self.author

    def set_author(self, author):
        return self.author == author

    def get_active(self):
        return self.active

    def set_active(self, active):
        return self.active == active

    def get_prg(self):
        return self.prg

    def set_prg(self, prg):
        return self.prg == prg

    def get_datetime(self):
        return self.datetime

    def set_datetime(self, datetime):
        return self.datetime == datetime

    def get_last_update(self):
        return self.last_update

    def set_last_update(self, last_update):
        return self.last_update == last_update

    def get_images(self):
        return self.images

    def set_images(self, images):
        return self.images == images