#!/usr/bin/env python3



class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size_param):
        if(type(size_param) != int):
            print('size must be an integer')
        else:
            self._size = size_param

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")
        



