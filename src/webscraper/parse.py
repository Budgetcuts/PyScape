import requests
import json

class Parse:
    def __init__(self, page):
        self.page = requests.get(page)
        self.content = self.page.content

    def changePage(self, page):
        self.page = requests.get(page)
        self.content = self.page.content

    def store(self, content):
        myList = []
        for word in content:
            print(word)
        print(myList)

    def parse(self):
        #main wrapper function for the Parse class, should take an input and parse through relevant data points
        content = self.content
        print(content)
        print(self.page.text)
        #self.store(content)
