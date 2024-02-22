#!/bin/python3

import sqlite3
from os.path import exists

class db_config():

    #create the database
    def create_db():
        if exists('cache.db'):
            print('Database already exists in the working directory.')
        else:
            conx = sqlite3.connect('cache.db')
            cur = conx.cursor()
            
            for cat in ['allnews', 'politics', 'finance', 'sports', 'digest', 'settings']:
                cur.execute(f"CREATE TABLE {cat} (publication text, headline text, author text, date text, content text, category text)")

            conx.commit()
            conx.close()


#modify database entries
class db_mod():
    #add a story entry to the 'allnews' table
    def add_story(publication, headline, author, date, content, category):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute("INSERT INTO allnews VALUES (:publication, :headline, :author, :date, :content, :category)", 
                    {'publication': publication, 'headline': headline, 'author': author, 'date': date, 'content': content, 'category': category})

        conx.commit()
        conx.close()
    
    #add a story to a specific table
    def add_to_table(publication, headline, author, date, content, category, table):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"INSERT INTO {table} VALUES (:publication, :headline, :author, :date, :content, :category)", 
                    {'publication': publication, 'headline': headline, 'author': author, 'date': date, 'content': content, 'category': category})

        conx.commit()
        conx.close()

    #remove a story from allnews
    def rm_from_table(headline):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"DELETE FROM allnews WHERE headline = :headline", {'headline': headline})

        conx.commit()
        conx.close()
    
    def cp_story(headline, table1, table2):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"INSERT INTO {table2} (publication, headline, author, date, content, category)
                    SELECT publication, :headline, author, date, content, category FROM {table1}", {'headline': headline})

        conx.commit()
        conx.close()