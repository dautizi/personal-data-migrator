import logging
import datetime

from settings import CONFIGURATION
from dao.mysql_dao import *
from dao.mongo_dao import *
from data.adventure import Adventure
from data.adventure_media import AdventureMedia
from data.blog import Blog

class MongoDBMigrationTool:

    def __init__(self, mysql_dao, mongo_dao):
        # Create logger
        self.logger = logging.getLogger('mongodb.migration')
        self.mysql_dao = mysql_dao
        self.mongo_dao = mongo_dao

    def run(self):
        # Adventures + Adventure Media
        self.migrate_adventures()

        # Blogs
        self.migrate_blogs()

    def get_now(self):
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

    def migrate_adventures(self):
        adventures = []

        # Query all adventures from db source
        get_adventures_query = "SELECT id, title, category, section, tag, keywords, css_class, " \
                               "image, icona, alt_image, article_url, static_url, description, " \
                               "adventure_type, view_type, media_css_class, datetime, prg, active " \
                               "FROM adventure "

        self.logger = logging.getLogger('mongodb.migration.get_adventures')
        self.logger.info('Query to execute: %s' % get_adventures_query)

        rows = self.mysql_dao.get_rows(get_adventures_query)
        for row in rows:
            if row is not None:
                self.logger.info('Adventure found - '
                                 'id: %s, '                 # row[0]
                                 'title: %s, '              # row[1]
                                 'category: %s, '           # row[2]
                                 'section: %s, '            # row[3]
                                 'tag: %s, '                # row[4]
                                 'keywords: %s, '           # row[5]
                                 'css_class: %s, '          # row[6]
                                 'image: %s, '              # row[7]
                                 'icona: %s, '              # row[8]
                                 'alt_image: %s, '          # row[9]
                                 'article_url: %s, '        # row[10]
                                 'static_url: %s, '         # row[11]
                                 'description: %s, '        # row[12]
                                 'adventure_type: %s, '     # row[13]
                                 'view_type: %s, '          # row[14]
                                 'media_css_class: %s, '    # row[15]
                                 'datetime: %s, '           # row[16]
                                 'prg: %s, '                # row[17]
                                 'active: %s'               # row[18]
                                 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                    row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]))

                print('ADV --> %s' % row[1])

                # Get all adventure media by id_adventure
                id_adventure = row[0]
                adventure_media_list = self.get_adventure_media_by_id_adventure(id_adventure)
                adventure_media_ids = self.get_adventure_media_ids_from_list(adventure_media_list)

                # Create a new Adventure instance
                adventure = Adventure(row[0], '', row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                      row[9], row[10], row[12], row[13], row[11], row[14], row[15], row[18], row[17],
                                      row[16], row[16], adventure_media_ids)

                # Store Adventure into mongoDB
                json_adventure = adventure.to_json()
                stored = self.mongo_dao.insert(CONFIGURATION['destinationDB']['collections']['adventure'],
                                               json_adventure)
                self.logger.info('  stored: %s' % stored)
                print('adventure stored --> %s' % stored)

                adventures.append(adventure)

        return adventures

    def get_adventure_media(self):
        adventure_media_list = []

        # Query all adventures from db source
        get_adventure_media_query = "SELECT id, id_adventure, media_type, media_path, media_url, title, alt, " \
                                    "css_class, prg, active " \
                                    "FROM adventure_media "

        self.logger = logging.getLogger('mongodb.migration.get_adventure_media')
        self.logger.info('Query to execute: %s' % get_adventure_media_query)

        rows = self.mysql_dao.get_rows(get_adventure_media_query)
        for row in rows:
            if row is not None:
                self.logger.info('AdventureMedia found - '
                                 'id: %s, '             # row[0]
                                 'id_adventure: %s, '   # row[1]
                                 'media_type: %s, '     # row[2]
                                 'media_path: %s, '     # row[3]
                                 'media_url: %s, '      # row[4]
                                 'title: %s, '          # row[5]
                                 'alt: %s, '            # row[6]
                                 'css_class: %s, '      # row[7]
                                 'prg: %s, '            # row[8]
                                 'active: %s, '         # row[9]
                                 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

                now_datetime = self.get_now()
                adventure_media = AdventureMedia(row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                                 row[9], now_datetime, now_datetime)

                adventure_media_list.append(adventure_media)

        return adventure_media_list

    def get_adventure_media_by_id_adventure(self, id_adventure):
        adventure_media_list = []

        # Query all adventures from db source
        get_adventure_media_query = "SELECT id, id_adventure, media_type, media_path, media_url, title, alt, " \
                                    "css_class, prg, active " \
                                    "FROM adventure_media " \
                                    "WHERE id_adventure='%s'" % id_adventure

        self.logger = logging.getLogger('mongodb.migration.get_adventure_media_by_id_adventure')
        self.logger.info('Query to execute: %s' % get_adventure_media_query)

        rows = self.mysql_dao.get_rows(get_adventure_media_query)
        for row in rows:
            if row is not None:
                self.logger.info('AdventureMedia found - '
                                 'id: %s, '             # row[0]
                                 'id_adventure: %s, '   # row[1]
                                 'media_type: %s, '     # row[2]
                                 'media_path: %s, '     # row[3]
                                 'media_url: %s, '      # row[4]
                                 'title: %s, '          # row[5]
                                 'alt: %s, '            # row[6]
                                 'css_class: %s, '      # row[7]
                                 'prg: %s, '            # row[8]
                                 'active: %s, '         # row[9]
                                 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

                now_datetime = self.get_now()
                adventure_media = AdventureMedia(row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                                 row[9], now_datetime, now_datetime)

                # Store all adventure media into mongoDB
                json_adventure_media = adventure_media.to_json()
                stored = self.mongo_dao.insert(CONFIGURATION['destinationDB']['collections']['adventure_media'],
                                               json_adventure_media)
                self.logger.info('  stored: %s' % stored)

                adventure_media_list.append(stored)

        return adventure_media_list

    def get_adventure_media_ids_from_list(self, adventure_media_list):
        adventure_media_ids = []
        for adventure_media in adventure_media_list:
            adventure_media_ids.append(adventure_media.inserted_id)

        return adventure_media_ids


    def migrate_blogs(self):
        blogs = []

        # Query all blogs from db source
        get_blogs_query = "SELECT id, title, category, section, tag, keywords, css_class, image, " \
                          "icona, alt_image, article_url, static_url, description, blog_type, view_type, " \
                          "media_css_class, creation_time, update_time, prg, active " \
                          "FROM blog "

        self.logger = logging.getLogger('mongodb.migration.get_blogs')
        self.logger.info('Query to execute: %s' % get_blogs_query)

        rows = self.mysql_dao.get_rows(get_blogs_query)
        for row in rows:
            if row is not None:
                self.logger.info('Blog found - '
                                 'id: %s, '                 # row[0]
                                 'title: %s, '              # row[1]
                                 'category: %s, '           # row[2]
                                 'section: %s, '            # row[3]
                                 'tag: %s, '                # row[4]
                                 'keywords: %s, '           # row[5]
                                 'css_class: %s, '          # row[6]
                                 'image: %s, '              # row[7]
                                 'icona: %s, '              # row[8]
                                 'alt_image: %s, '          # row[9]
                                 'article_url: %s, '        # row[10]
                                 'static_url: %s, '         # row[11]
                                 'description: %s, '        # row[12]
                                 'blog_type: %s, '          # row[13]
                                 'view_type: %s, '          # row[14]
                                 'media_css_class: %s, '    # row[15]
                                 'creation_time: %s, '      # row[16]
                                 'update_time: %s, '        # row[17]
                                 'prg: %s, '                # row[18]
                                 'active: %s'               # row[19]
                                 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                    row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                                    row[15], row[16], row[17], row[18], row[19]))

                print('BLOG --> %s' % row[1])

                # Create a new Blog instance
                blog = Blog(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                            row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])

                # Store Blog into mongoDB
                json_blog = blog.to_json()
                stored = self.mongo_dao.insert(CONFIGURATION['destinationDB']['collections']['blog'],
                                               json_blog)
                self.logger.info('  stored: %s' % stored)
                print('blog stored --> %s' % stored)

                blogs.append(blog)

        return blogs

if __name__ == "__main__":
    # HOW TO CALL
    # 1. get source MySqlDAO INSTANCE
    mysql_dao = MySQLDAO()

    # 2. get source MongoDBDAO INSTANCE
    mongo_dao = MongoDAO()

    print("######### MIGRATION [BEGIN] #########")
    migrationTool = MongoDBMigrationTool(mysql_dao, mongo_dao)
    migrationTool.run()
    print("######### MIGRATION [END] #########")