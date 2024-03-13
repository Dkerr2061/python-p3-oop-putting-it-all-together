#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count  
    @page_count.setter
    def page_count(self, page_count_param):
        if(type(page_count_param) != int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count_param
 
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        