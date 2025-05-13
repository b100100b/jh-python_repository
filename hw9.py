class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x}, {self.__y})')

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def get(self):
        tue = (self.__x, self.__y)
        return tue

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__lt = Point(x1, y1)
        self.__rb = Point(x2, y2)

    def show(self):
        x1, y1 = self.__lt.get()
        x2, y2 = self.__rb.get()
        print(f'좌측 상단 꼭지점이 ({x1}, {y1})이고 우측 하단 꼭지점이 ({x2}, {y2})인 사각형입니다.')

    def getWidth(self):
        x1, y1 = self.__lt.get()
        x2, y2 = self.__rb.get()
        return (x2 - x1)

    def getHeight(self):
        x1, y1 = self.__lt.get()
        x2, y2 = self.__rb.get()
        return (y2 - y1)

    def getArea(self):
        x1, y1 = self.__lt.get()
        x2, y2 = self.__rb.get()
        return ((x2 - x1) * (y2 - y1))

    def getPerimeter(self):
        x1, y1 = self.__lt.get()
        x2, y2 = self.__rb.get()
        return ((2 * (x2 - x1)) + (2 * (y2 - y1)))

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')    
        
