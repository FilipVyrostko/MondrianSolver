"""Class representing rectangle object in the Mondrian's Rectangles puzzle"""
class Rectangle:
    # x, y coordinates of the corner defining the position of the rectangle
    x: int = None
    y: int = None
    # width and height of the rectangle
    w: int = None
    h: int = None
    # area of the rectangle
    area: int = None

    def __init__(self, x: int, y: int, w: int, h: int):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.area = w * h

    def __sub__(self, other):
        return self.area - other.area

    def __str__(self):
        return f"Rectangle at >> ({self.x}, {self.y})\n" \
               f"Width >> {self.w}\n" \
               f"Height >> {self.h}\n" \
               f"Area >> {self.area}\n"

    def get_dims(self):
        return (self.w, self.h)
