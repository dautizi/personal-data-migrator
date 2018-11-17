import logging
import datetime

from settings import CONFIGURATION
from dao.mysql_dao import *
from dao.mongo_dao import *
from data.adventure import Adventure
from data.adventure_media import AdventureMedia
from data.blog import Blog
from data.education import Education
from data.skill import Skill
from data.work_experience import WorkExperience


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

        # Education
        self.migrate_educations()

        # Skills
        self.migrate_skills()

        # Work Experiences
        self.migrate_work_experiences()


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


    def migrate_educations(self):
        educations = []

        # Query all educations from db source
        get_educations_query = "SELECT id, school, title, description, school_image, school_thumb, period, " \
                               "start_year, end_year, prg, active, creation_time, update_time " \
                               "FROM education "

        self.logger = logging.getLogger('mongodb.migration.get_educations')
        self.logger.info('Query to execute: %s' % get_educations_query)
        print(get_educations_query)

        rows = self.mysql_dao.get_rows(get_educations_query)
        for row in rows:
            if row is not None:
                self.logger.info('Education found - '
                                 'id: %s, '                 # row[0]
                                 'school: %s, '             # row[1]
                                 'title: %s, '              # row[2]
                                 'description: %s, '        # row[3]
                                 'school_image: %s, '       # row[4]
                                 'school_thumb: %s, '       # row[5]
                                 'period: %s, '             # row[6]
                                 'start_year: %s, '         # row[7]
                                 'end_year: %s, '           # row[8]
                                 'prg: %s, '                # row[9]
                                 'active: %s, '             # row[10]
                                 'creation_time: %s, '      # row[11]
                                 'update_time: %s, '        # row[12]
                                 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                    row[8], row[9], row[10], row[11], row[12]))

                print('EDUCATION --> %s' % row[1])

                # Create a new Education instance
                education = Education(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                      row[9], row[10], row[11], row[12])

                # Store Education into mongoDB
                json_education = education.to_json()
                stored = self.mongo_dao.insert(CONFIGURATION['destinationDB']['collections']['education'],
                                               json_education)
                self.logger.info('  stored: %s' % stored)
                print('education stored --> %s' % stored)

                educations.append(education)

        return educations


    def migrate_skills(self):
        skills = []

        # Query all educations from db source
        get_skills_query = "SELECT id, group_name, title, progress, percentage, years, since, " \
                           "image_url, prg, active, creation_time, update_time " \
                           "FROM skill "

        self.logger = logging.getLogger('mongodb.migration.get_skills')
        self.logger.info('Query to execute: %s' % get_skills_query)

        rows = self.mysql_dao.get_rows(get_skills_query)
        for row in rows:
            if row is not None:
                self.logger.info('Skill found - '
                                 'id: %s, '             # row[0]
                                 'group_name: %s, '     # row[1]
                                 'title: %s, '          # row[2]
                                 'progress: %s, '       # row[3]
                                 'percentage: %s, '     # row[4]
                                 'years: %s, '          # row[5]
                                 'since: %s, '          # row[6]
                                 'image_url: %s, '      # row[7]
                                 'active: %s, '         # row[8]
                                 'prg: %s, '            # row[9]
                                 'creation_time: %s, '  # row[10]
                                 'update_time: %s, '    # row[11]
                                 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                    row[7], row[8], row[9], row[10], row[11]))

                print('SKILL --> %s' % row[1])

                # Create a new Education instance
                skill = Skill(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                              row[9], row[10], row[11])

                # Store Skill into mongoDB
                json_skill = skill.to_json()
                stored = self.mongo_dao.insert(CONFIGURATION['destinationDB']['collections']['skill'],
                                               json_skill)
                self.logger.info('  stored: %s' % stored)
                print('skill stored --> %s' % stored)

                skills.append(skill)

        return skills


    def migrate_work_experiences(self):
        work_experiences = []

        # Query all educations from db source
        get_work_experiences_query = "SELECT id, role, company, description, period, company_image, " \
                                     "company_thumb, active, prg, creation_time, update_time " \
                                     "FROM work_experience "

        self.logger = logging.getLogger('mongodb.migration.get_work_experiences')
        self.logger.info('Query to execute: %s' % get_work_experiences_query)

        rows = self.mysql_dao.get_rows(get_work_experiences_query)
        for row in rows:
            if row is not None:
                self.logger.info('WorkExperience found - '
                                 'id: %s, '             # row[0]
                                 'role: %s, '           # row[1]
                                 'company: %s, '        # row[2]
                                 'description: %s, '    # row[3]
                                 'period: %s, '         # row[4]
                                 'company_image: %s, '  # row[5]
                                 'company_thumb: %s, '  # row[6]
                                 'active: %s, '         # row[7]
                                 'prg: %s, '            # row[8]
                                 'creation_time: %s, '  # row[9]
                                 'update_time: %s, '    # row[10]
                                 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                    row[7], row[8], row[9], row[10]))

                print('WORK EXPERIENCE --> %s' % row[1])

                # Create a new Education instance
                work_experience = WorkExperience(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                                 row[7], row[8], row[9], row[10])

                # Store Work Experience into mongoDB
                json_work_experience = work_experience.to_json()
                stored = self.mongo_dao.insert(CONFIGURATION['destinationDB']['collections']['work_experience'],
                                               json_work_experience)
                self.logger.info('  stored: %s' % stored)
                print('work_experience stored --> %s' % stored)

                work_experiences.append(work_experience)

        return work_experiences


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