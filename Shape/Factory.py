import numpy as np
import cv2 as cv


class Shape:
    def __init__(self):
        self._area = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def draw(self):
        pass


class Circle(Shape):
    pass


class Square(Shape):
    pass


class Line(Shape):
    pass


class Triangle(Shape):
    pass


class Pentagon(Shape):
    pass


class ShapeFactory:
    def __init__(self, typ, config):
        if typ == 'circle':
            return Circle(config)


config = {'length': 10, "width": 10, "size": 1000, "color": (0, 0, 0), "center" = (10, 10)}
img = np.ones((1000, 1000, 3), dtype=np.uint8) * 255  # BGR - Blue, Green, Red
cv.rectangle(img, (300, 300), (700, 700), color=(0, 255, 0), thickness=-1)
cv.circle(img, (500, 500), 200, color=((255, 0, 0)), thickness=-1)
contours = np.array([(300, 700), (500, 300), (700, 700)])
cv.drawContours(img, [contours], 0, color=(0, 0, 255), thickness=-1)


cv.imshow('image', img)
cv.waitKey(0)
