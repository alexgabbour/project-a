#!/bin/python3

import sqlite3
from os.path import exists

class config():

    #create the database
    def create_db():
        if exists('cache.db'):
            print('Database already exists in the working directory.')
        else:
            conx = sqlite3.connect('cache.db')
            cur = conx.cursor()
            
            for cat in ['allnews', 'politics', 'finance', 'weather', 'general', 'digest']:
                cur.execute(f"CREATE TABLE {cat} (hash real, title text, author text, date text, desc text, cat text)")

            conx.commit()
            conx.close()


#modify database entries
class mod():
    #add a story entry to the 'allnews' table
    def add_story(hash, title, author, date, desc, cat):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute("INSERT INTO allnews VALUES (:hash, :title, :author, :date, :desc, :cat)", 
                    {'hash': hash, 'title': title, 'author': author, 'date': date, 'desc': desc, 'cat': cat})

        conx.commit()
        conx.close()
    
    #add a story to a specific table - should only be used for testing
    def add_to_table(table, hash, title, author, date, desc, cat):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"INSERT INTO {table} VALUES (:hash, :title, :author, :date, :desc, :cat)", 
                    {'hash': hash, 'title': title, 'author': author, 'date': date, 'desc': desc, 'cat': cat})

        conx.commit()
        conx.close()

    #remove a story from allnews
    def rm_from_table(hash):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"DELETE FROM allnews WHERE hash = :hash", {'hash': hash})

        conx.commit()
        conx.close()
    
    def cp_story(hash, table1, table2):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"INSERT INTO {table2} (hash, title, author, date, desc, cat) SELECT :hash, title, author, date, desc, cat FROM {table1}", {'hash': hash})

        conx.commit()
        conx.close()

    def cp_from_allnews(hash, destTable):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()
        cur.execute(f"INSERT INTO {destTable} (hash, title, author, date, desc, cat) SELECT * FROM allnews WHERE hash = :hash", {'hash': hash})

        conx.commit()
        conx.close()

class query():

    def all_hashes_from_category(category):
        conx = sqlite3.connect('cache.db')
        cur = conx.cursor()

        cur.execute(f"SELECT hash FROM allnews WHERE cat = :cat", {'cat': category})
        hashesTuples = cur.fetchall()
        hashes = []
        for i in range(len(hashesTuples)):
            hashes.append(hashesTuples[i][0])

        conx.commit()
        conx.close()
        
        return hashes