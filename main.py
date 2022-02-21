import cv2 as cv
import numpy as np
import os

class ToAscii:
    def __init__(self, entity, size, detail = 1, kind='image'):   
        self.W, self.H = 5 * size, 4 * size
        self.detail = detail
        self.kind = kind 

        self.sample =  {(230, 256):'#' , (204, 230): '%', (178, 204):'S', (153, 178):'?',(127, 153):'*', (101, 127):'+', (75, 101):';', (49, 75):':',(25, 49):',', (0, 25):'.'}

        if self.kind == 'image':
            self.photo = cv.imread(entity)
        elif self.kind == 'video':
            self.video= cv.VideoCapture(entity)

    def image_setup(self, object):
            object = cv.resize(object, (self.W, self.H), interpolation=cv.INTER_AREA)
            object = cv.cvtColor(object, cv.COLOR_BGR2GRAY)
            object = object // self.detail * self.detail + self.detail // 2
            return object

    def printing_ascii(self, object):
            keys = tuple(self.sample.keys())
            image_str = ''

            for row in object:
                for pixel in row:
                    left = 0
                    right = len(keys) - 1
                    while left < right:
                        mid = (left + right) // 2

                        if pixel > keys[mid][1]:
                            right = mid

                        else:
                            left = mid + 1

                    image_str += self.sample[keys[left]]

                image_str += '\n'
            
            print(image_str)

    def to_ascii(self):
        if self.kind == 'image':
            self.photo = self.image_setup(self.photo)
            self.printing_ascii(self.photo)
        else:
            while True:
                os.system('cls')
                _, frame = self.video.read()
                frame = self.image_setup(frame)
                self.printing_ascii(frame)
                

    
    def update(self):
            self.to_ascii()

if __name__ == '__main__':
    img1 = ToAscii('Anime gril.jpg', 30, kind='image')
    img1.update()

