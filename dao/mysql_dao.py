'''
    MySQLDAO Singleton Util
    @author:   Daniele Autizi
    @version:  1.0
    @since:    01-05-2018
'''

import mysql.connector
from sshtunnel import SSHTunnelForwarder
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
from settings import CONFIGURATION


def offset_calculator(limit, page):
    offset = page * limit
    return offset


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MySQLDAO(Singleton):

    def __init__(self):
        """
        Init MySQL connection
        """
        self._connect()
        return

    def _connect(self):
        """
        Creates connection
        """
        self.connection = mysql.connector.connect(host=CONFIGURATION['sourceDB']['host'],
                                                  user=CONFIGURATION['sourceDB']['username'],
                                                  password=CONFIGURATION['sourceDB']['password'],
                                                  database=CONFIGURATION['sourceDB']['dbname'])
        return

    def _ssh_tunnelling(self):
        """
        SSH Tunnelling
        """
        with SSHTunnelForwarder(
                (CONFIGURATION['sourceDB']['ssh']['host'], 22),
                ssh_username=CONFIGURATION['sourceDB']['ssh']['username'],
                ssh_password=CONFIGURATION['sourceDB']['ssh']['password'],
                remote_bind_address=(CONFIGURATION['sourceDB']['ssh']['host'], 3306)
        ) as tunnel:
            connection = self.connection


    def _commit(self):
        """
        Transaction commit
        """
        self.connection.commit()

    def _rollback(self):
        """
        Transaction rollback
        """
        self.connection.rollback()

    def _get_cursor(self):
        """
        Pings connection and returns cursor 
        """
        try:
            self.connection.ping()
        except:
            self._connect()
        return self.connection.cursor()

    def get_row(self, query):
        """
        Fetchs one row
        """
        cursor = self._get_cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        return row

    def get_rows(self, query):
        """
        Fetchs all rows
        """
        cursor = self._get_cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def execute(self, query):
        """
        Executes query for update, delete
        """
        cursor = self._get_cursor()
        cursor.execute(query)
        cursor.close()
        return

    def insert(self, query):
        """
        Executes query for insert
        """
        cursor = self._get_cursor()
        try:
            cursor.execute(query)
            self._commit()
        except:
            self._rollback()
        cursor.close()
        return
