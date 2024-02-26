#!/bin/python3

## pick out the categories
## create a story object (??) for the db manager to sort into the proper table

import xml.dom.minidom

class parser():
    #generate a set of nicely formatted stories from a specified RSS feed XML file
    def getStories(xmlFile):
        domtree = xml.dom.minidom.parse(xmlFile)
        group = domtree.documentElement
        stories = group.getElementsByTagName('item')

        for story in stories:
            #check for the existance of tags - replace with nothing if they don't exist

            try:
                title = story.getElementsByTagName('title')[0].childNodes[0].nodeValue
            except Exception:
                author = '*No title*'

            try:
                date = story.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
            except Exception:
                author = '*No date*'

            try:
                author = story.getElementsByTagName('dc:creator')[0].childNodes[0].nodeValue
            except Exception:
                author = '*No author*'
                
            try:
                desc = story.getElementsByTagName('media:description')[0].childNodes[0].nodeValue
            except Exception:
                desc = '*No description*'

            #take the variable names and print them to the terminal - these values will be sent to the databases in the end
            print(f"--- {title} ---\n Author: {author}\n Date: {date}\n Description: {desc}\n")

parser.getStories('US.xml')