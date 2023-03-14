Ans 6.

class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def __valid_triangle(self):
        return (self.__a + self.__b > self.__c) and \
               (self.__a + self.__c > self.__b) and \
               (self.__b + self.__c > self.__a)
    
    def triangle_type(self):
        if not self.__valid_triangle():
            return "Invalid Triangle"
        elif self.__a == self.__b == self.__c:
            return "Equilateral Triangle"
        elif self.__a == self.__b or self.__b == self.__c or self.__c == self.__a:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
