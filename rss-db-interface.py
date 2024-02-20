#!/bin/python3

import sqlite3

conx = sqlite3.connect('cache.db')

cur = conx.cursor()

class db_config():
    def init_db():
        cur.execute("CREATE TABLE news (publication text, headline text, author text, date text, content text)")

        conx.commit()

    def add_story(publication, headline, author, date, content):
        cur.execute("INSERT INTO news VALUES (:publication, :headline, :author, :date,:content)", 
                    {'publication': publication, 'headline': headline, 'author': author, 'date': date, 'content': content})

        conx.commit()

#db_config.add_story('Washington Post', 'Trump running again?', 'Billy Bob', '4 June, 2020', 'Well it\'s happening again. Who could have seen this coming')

conx.close()