import os
import time

class Car():
    def __init__(self, make, model, color):
        self._make = make
        self._model = model
        self.color = color

    def paint(self, new_color):
        
        if new_color is None:
            raise ValueError
        else:
            self.color = new_color
            print(f'The {self._make} {self._model} is now {self.color}')


