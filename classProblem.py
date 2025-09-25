# Big Class Problem Set

class Shape:
    def __init__(self, c):
        self.color = str(c)
    
    def get_color(self):
        return self.color
    
    def get_area(self):
        return float # python doesn't enforce return datatypes, this is the best i could think of? pl lmk if you were looking for a different solution.
    
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side
    
    def get_area(self):
        return float(self.side)**2
    

