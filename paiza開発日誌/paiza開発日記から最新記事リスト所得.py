# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:12:31 2019

@author: student
"""

import requests

r = requests.get('https://paiza.hatenablog.com/')


from html.parser import HTMLParser

class TestParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False

    def handle_starttag(self, tag, attribute):
        if tag.lower() == 'a':
            attr = dict(attribute)
            if 'class' in attr:
                if 'recent-entries-title-link' in attr['class']:
                    self.flag = True
                    print(attr['href'])


    def handle_data(self, data):
        if self.flag:
            self.data = data
            self.flag = False
            print(data)


parser = TestParser()
parser.feed(r.text)
parser.close()
