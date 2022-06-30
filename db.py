import psycopg2
import logging


class DatabaseEngine:
    def __init__(self):
        try:
            conn = psycopg2.connect(dbname='cards', user='vlad',
                                    password='vlad',
                                    port='5433')
        except Exception as e:
            logging.error(e)
    def insert_rows(self):



DatabaseEngine()
