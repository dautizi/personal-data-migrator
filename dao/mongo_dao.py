'''
    MongoDBDAO Singleton Util
    @author:   Daniele Autizi
    @version:  1.0
    @since:    11-05-2018
'''

import logging
from pymongo import MongoClient
from random import randint
# https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

from settings import CONFIGURATION


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MongoDAO(Singleton):

    def __init__(self):
        self.logger = logging.getLogger('mongodb.migration.mongo_dao')

        """
        Init MongoDB client
        """
        self.client = MongoClient(host=CONFIGURATION['destinationDB']['host'],
                                  port=CONFIGURATION['destinationDB']['port'])
        self.database = self.client[CONFIGURATION['destinationDB']['dbname']]
        return

    def insert(self, collection, json_data):
        self.logger = logging.getLogger('mongodb.migration.mongo_dao.insert_one')
        self.logger.info('Insert %s into %s' % (json_data, collection))

        """
        Executes query for insert
        """
        result = None
        collection_instance = self.database[collection]

        try:
            result = collection_instance.insert_one(json_data)
            self.logger.info('Insertion result: ' % result)
        except Exception as exc:
            self.logger.error('Error in insertion for data: ' % json_data)
            self.logger.error(exc)

        return result