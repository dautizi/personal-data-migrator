'''
Adventure Bean
'''
import datetime

class Adventure:

    def __init__(self, id, article_unique_path, title, category, section, tag, keywords, css_class, image, icon,
                 alt_image, article_url, description, adventure_type, static_url, view_type, media_css_class, active,
                 prg, datetime, last_update, adventure_media_ids):

        self.id = id
        self.article_unique_path = article_unique_path
        self.title = title
        self.category = category
        self.section = section
        self.tag = tag
        self.keywords = keywords
        self.css_class = css_class
        self.image = image
        self.icon = icon
        self.alt_image = alt_image
        self.article_url = article_url
        self.description = description
        self.adventure_type = adventure_type
        self.static_url = static_url
        self.view_type = view_type
        self.media_css_class = media_css_class
        self.active = active
        self.prg = prg
        self.datetime = datetime
        self.last_update = last_update
        self.adventure_media_ids = adventure_media_ids

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_article_unique_path(self):
        return self.article_unique_path

    def set_article_unique_path(self, article_unique_path):
        self.article_unique_path = article_unique_path

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_section(self):
        return self.section

    def set_section(self, section):
        self.section = section

    def get_tag(self):
        return self.tag

    def set_tag(self, tag):
        return self.tag == tag

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, keywords):
        return self.keywords == keywords

    def get_css_class(self):
        return self.css_class

    def set_css_class(self, css_class):
        return self.css_class == css_class

    def get_image(self):
        return self.image

    def set_image(self, image):
        return self.image == image

    def get_icon(self):
        return self.icon

    def set_icon(self, icon):
        return self.icon == icon

    def get_alt_image(self):
        return self.alt_image

    def set_alt_image(self, alt_image):
        return self.alt_image == alt_image

    def get_article_url(self):
        return self.article_url

    def set_article_url(self, article_url):
        return self.article_url == article_url

    def get_description(self):
        return self.description

    def set_description(self, description):
        return self.description == description

    def get_adventure_type(self):
        return self.adventure_type

    def set_adventure_type(self, adventure_type):
        return self.adventure_type == adventure_type

    def get_static_url(self):
        return self.static_url

    def set_static_url(self, static_url):
        return self.static_url == static_url

    def get_view_type(self):
        return self.view_type

    def set_view_type(self, view_type):
        return self.view_type == view_type

    def get_media_css_class(self):
        return self.media_css_class

    def set_media_css_class(self, media_css_class):
        return self.media_css_class == media_css_class

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

    def get_adventure_media_ids(self):
        return self.adventure_media_ids

    def set_adventure_media_ids(self, adventure_media_ids):
        return self.adventure_media_ids == adventure_media_ids

    def to_json(self):
        active = True if self.active > 0 else False

        ct = datetime.datetime.strptime(self.datetime, "%Y-%m-%d %H:%M:%S")
        isoCt = datetime.datetime.fromtimestamp(ct.timestamp(), None)
        ut = datetime.datetime.strptime(self.last_update, "%Y-%m-%d %H:%M:%S")
        isoUt = datetime.datetime.fromtimestamp(ut.timestamp(), None)

        json = {'articleUniquePath': self.article_unique_path,
                'title': self.title,
                'category': self.category,
                'section': self.section,
                'tag': self.tag,
                'keywords': self.keywords,
                'cssClass': self.css_class,
                'image': self.image,
                'icon': self.icon,
                'altImage': self.alt_image,
                'articleUrl': self.article_url,
                'description': self.description,
                'adventureType': self.adventure_type,
                'staticUrl': self.static_url,
                'viewType': self.view_type,
                'mediaCssClass': self.media_css_class,
                'active': active,
                'prg': self.prg,
                'datetime': isoCt,
                'lastUpdate': isoUt,
                'adventureMediaIds': self.adventure_media_ids}
        return json