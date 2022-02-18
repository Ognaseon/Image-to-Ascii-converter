import cv2 as cv
import numpy as np
import os


class ToAscii:
    def __init__(self, entity, size, detail = 1, kind='image'):   
        self.W, self.H = 2 * size, 1 * size
        self.detail = detail
        self.kind = kind 

        self.sample =  {'#': (230, 256), '%':(204, 230), 'S':(178, 204),'?': (153, 178),'*': (127, 153),'+': (101, 127),';': (75, 101),':': (49, 75),',': (25, 49),'.': (0, 25)}
        self.clear = lambda: os.system('cls')

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
            for row in object:
                for index, pixel in enumerate(row):
                    if index != self.W -1:
                        for key, v in self.sample.items():
                            if pixel in range(*v):
                                print(key, end='')
                    else:
                        print('')

    def to_ascii(self):
        if self.kind == 'image':
            self.photo = self.image_setup(self.photo)
            self.printing_ascii(self.photo)
        else:
            while True:
                self.clear()
                _, frame = self.video.read()
                frame = self.image_setup(frame)
                self.printing_ascii(frame)

    
    def update(self):
        self.to_ascii()

img1 = ToAscii('plik.jpg', 50, 1)
img1.update()