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
            
            for cat in ['allnews', 'politics', 'finance', 'sports', 'digest']:
                cur.execute(f"CREATE TABLE {cat} (title text, author text, date text, desc text)")

            conx.commit()
            conx.close()


#modify database entries
class db_mod():
    #add a story entry to the 'allnews' table
    def add_story(title, author, date, desc):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute("INSERT INTO allnews VALUES (:title, :author, :date, :desc)", 
                    {'title': title, 'author': author, 'date': date, 'desc': desc})

        conx.commit()
        conx.close()
    
    #add a story to a specific table
    def add_to_table(title, author, date, desc, table):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"INSERT INTO {table} VALUES (:title, :author, :date, :desc)", 
                    {'title': title, 'author': author, 'date': date, 'desc': desc})

        conx.commit()
        conx.close()

    #remove a story from allnews
    def rm_from_table(title):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"DELETE FROM allnews WHERE title = :title", {'title': title})

        conx.commit()
        conx.close()
    
    def cp_story(title, table1, table2):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"INSERT INTO {table2} (headline, author, date, desc) SELECT :title, author, date, desc FROM {table1}", {'title': title})

        conx.commit()
        conx.close()

db_config.create_db()