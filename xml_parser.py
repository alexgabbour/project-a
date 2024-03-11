#!/bin/python3

## pick out the categories
## create a story object (?? dictionnaries could come in handy here) for the db manager to sort into the proper table
## this is the core of the parser only. it'll get uncategorized stories into a database, nicely formatted.
## getStories function will have to be given or determine a publication as an input so it can tag its stories  IN THE FUTURE!
## for v1.0 getStories will just have to differentiate between a few xml files.

import xml.dom.minidom
import hashlib
from random import randint
import subprocess as sp



class parser():
    #fetch rss xml file from nytimes.com and save it to the working directory
    def fetch_rss(url):
        sp.run(['wget', url])
    
    
    #generate a set of nicely formatted stories from a specified RSS feed XML file and return the dictionnary 'storyBlock'
    def getStories(xmlFile):
        domtree = xml.dom.minidom.parse(xmlFile)
        group = domtree.documentElement
        stories = group.getElementsByTagName('item')

        storyBlock = {}
        id = 0
        for story in stories:
            #parses story info from xml tags and stores value into variables - replace with nothing if they don't exist

            try:
                h = hashlib.new('md5')
                h.update(story.getElementsByTagName('title')[0].childNodes[0].nodeValue.encode()) #the hash of each story is the md5 hash of the title
                hash = h.hexdigest()
            except IndexError:
                h = hashlib.new('md5')
                h.update(str(randint(0, 0xFFFF))) #if there is an index error we replace the title with a random number between 0 and FFFF and hashing that instead
                hash = h.hexdigest()


            try:
                title = story.getElementsByTagName('title')[0].childNodes[0].nodeValue
            except IndexError:
                title = '*No title*'


            try:
                date = story.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
            except IndexError:
                date = '*No date*'


            try:
                author = story.getElementsByTagName('dc:creator')[0].childNodes[0].nodeValue
            except IndexError:
                author = '*No author*'

                
            try:
                desc = story.getElementsByTagName('media:description')[0].childNodes[0].nodeValue
            except IndexError:
                desc = '*No description*'


            try:
                catList = []
                numCats = len(story.getElementsByTagName('category'))
                for i in range(numCats):
                    catList.append(story.getElementsByTagName('category')[i].childNodes[0].nodeValue)
                
                #this if block classifies many categories into the few used in the database
                if 'United States Politics and Government' and 'Presidential Election of 2024' in catList:
                    cat = 'politics'
                    pass                
                elif 'Weather' in catList:
                    cat = 'weather'
                    pass
                elif 'Federal Budget (US)' or 'United States Economy' in catList:
                    cat = 'finance'
                    pass
                else:
                    cat = 'general'
            except IndexError:                
                cat = '*No category*' #if there are no categories associated with the story we print this

            #after each story is parsed it is stored in a dictionary as a tuple for immutability
            storyBlock[id] = (hash, title, author, date, desc, cat)
            id = id + 1
        

        
        return storyBlock












#parser.getStories('US.xml') #uncomment line for testing