#長方形を表すクラス

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height