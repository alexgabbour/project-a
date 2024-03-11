#!/bin/python3

import db_manager
import xml_parser

##fetch xml file
xml_parser.parser.fetch_rss('https://rss.nytimes.com/services/xml/rss/nyt/US.xml')

##create cache.db database
db_manager.config.create_db()


##get stories from rss feed and store relevant data in the 'storyBlock' dictionnary
storyBlock = xml_parser.parser.getStories('US.xml')

##add story block to allnews table in cache.db
#sub-indices 1 through 5 => hash, title, author, date, desc, cat
for id in storyBlock:
    db_manager.mod.add_story(storyBlock[id][0], storyBlock[id][1], storyBlock[id][2], storyBlock[id][3], storyBlock[id][4], storyBlock[id][5])

##copy each story to the table which corresponds with its category
#create a dictionnary where hashes will be stored as a list alongside their respective category
#loop through each hash for a specific category and use the cp_from_allnews function to store the story with that hash in the correct database table
hashesDict = {'Politics': [],'Finance': [], 'Weather': [],'General': []}

for cat in ['politics', 'finance', 'weather', 'general']:
    hashesDict[cat] = db_manager.query.all_hashes_from_category(cat)

    for hash in hashesDict[cat]:
        db_manager.mod.cp_from_allnews(hash, cat) #hashcat lol











