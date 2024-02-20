#!/bin/python3

import sqlite3
from os.path import exists

conx = sqlite3.connect('cache.db')

cur = conx.cursor()

class db_config():
    def create_db():
        if exists('cache.db'):
            print('Database already exists in the working directory.')
        else:
            cur.execute("CREATE TABLE allnews (publication text, headline text, author text, date text, content text, category text)")
            cur.execute("CREATE TABLE politics (publication text, headline text, author text, date text, content text, category text)")
            cur.execute("CREATE TABLE finance (publication text, headline text, author text, date text, content text, category text)")
            cur.execute("CREATE TABLE sports (publication text, headline text, author text, date text, content text, category text)")

            conx.commit()

    def add_story(publication, headline, author, date, content, category):
        cur.execute("INSERT INTO news VALUES (:publication, :headline, :author, :date, :content, :category)", 
                    {'publication': publication, 'headline': headline, 'author': author, 'date': date, 'content': content, 'category': category})

        conx.commit()

db_config.create_db()

conx.close()