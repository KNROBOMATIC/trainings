import numpy as np
import cv2 as cv


class Shape:
    def __init__(self):
        self._area = None
        self._length = None
        self._width = None
        self._size = None
        self._color = None
        self._center = None

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
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, tuple):
            self._color = value

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        if isinstance(value, tuple):
            self._center = value

    def draw(self):
        self.image = np.ones((self.size, self.size, 3), dtype = np.uint8)
        return self.image


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
