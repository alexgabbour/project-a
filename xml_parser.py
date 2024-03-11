#!/bin/python3

## pick out the categories
## create a story object (?? dictionnaries could come in handy here) for the db manager to sort into the proper table
## this is the core of the parser only. it'll get uncategorized stories into a database, nicely formatted.
## getStories function will have to be given or determine a publication as an input so it can tag its stories  IN THE FUTURE!
## for v1.0 getStories will just have to differentiate between a few xml files.

import xml.dom.minidom
import hashlib
from random import randint

class parser():
    #generate a set of nicely formatted stories from a specified RSS feed XML file

    def getStories(xmlFile):
        domtree = xml.dom.minidom.parse(xmlFile)
        group = domtree.documentElement
        stories = group.getElementsByTagName('item')

        storyBlock = {}
        id = 0
        for story in stories:
            #check for the existance of tags - replace with nothing if they don't exist

            try:
                h = hashlib.new('md5')
                h.update(story.getElementsByTagName('title')[0].childNodes[0].nodeValue.encode())
                hash = h.hexdigest()
            except IndexError:
                h = hashlib.new('md5')
                h.update(str(randint(0, 0xFFFF)))
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
                cat = story.getElementsByTagName('category')[0].childNodes[0].nodeValue
            except IndexError:
                cat = '*No category*'

            #after each story is parsed, store it in a dictionnary as a tuple for immutability
            storyBlock[id] = (hash, title, author, date, desc, cat)
            id = id + 1
        


        return storyBlock