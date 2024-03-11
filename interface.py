#!/bin/python3

import db_manager
import xml_parser

#create cache.db database
db_manager.db_config.create_db()


#get stories from rss feed and store relevant data in the 'storyBlock' dictionnary
storyBlock = xml_parser.parser.getStories('US.xml')

#add story block to allnews table in cache.db
#indices 1 through 5 are here to represent each column
for id in storyBlock:
    db_manager.db_mod.add_story(storyBlock[id][0], storyBlock[id][1], storyBlock[id][2], storyBlock[id][3], storyBlock[id][4], storyBlock[id][5])













