#create class linea

#*length, slope, start, end: Instance attributes, two of them being points (so a   line is composed at least of two points).
#* compute_length(): should return the line´s length
#* compute_slope(): should return the slope of the line from tje horizontal in deg.
#* compute_horizontal_cross(): should return if exists the intersection with x-axis
#* compute_vertical_cross(): should return if exists the intersection with y-axis



class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def compute_distance(self, point: "Point"):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
    
    def __str__(self):
        return f"({self.x},{self.y})"

class Line:
    def __init__(self, start: "Point", end: "Point"):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
    
    def compute_length(self)-> float:
        return self.start.compute_distance(self.end)

    def compute_slope(self)-> float:
        if self.end.x != self.start.x:     
            delta_y = self.end.y - self.start.y
            delta_x = self.end.x - self.start.x
            return delta_y / delta_x
        else:
            return None
    
    def compute_horinzontal_cross(self)->bool:
        a: bool = self.start.y <= 0 
        b: bool = self.end.y <= 0
        if  (a or b) and not (a and b) :
            return True
        return False
    
    def compute_vertical_cross(self)->bool:
        a: bool = self.start.x <= 0 
        b: bool = self.end.x <= 0
        if  (a or b) and not (a and b) :
            return True
        return False
    
#    def discretize_line(self, n: int):        #! en revision
#        discretized = []
#        if self.slope == None:
#            m = 0
#        else:
#            m = self.slope
#        delta_x = (self.end.x - self.start.x) / n
#        a = 0
#        for i in range(n):
#            x = self.start.x + a
#            y = m * (x - self.start.x) + self.start.y 
#            discretized.append(Point(x, y))
#            a += self.start.x + delta_x
#        return discretized
        
class Rectangle4Lines:
    def __init__(self, left_side: "Line", top_side: "Line", right_side: "Line" , bottom_side: "Line"):
        
        self.left_side = Line(start = Point(left_side.start.x, top_side.start.y), end = Point(left_side.start.x, bottom_side.start.y))
        
        self.top_side = Line(start = Point(left_side.start.x, top_side.start.y), end = Point(right_side.start.x, top_side.start.y))
        
        self.rigth_side = Line(start = Point(right_side.start.x, top_side.start.y), end = Point(right_side.start.x, bottom_side.start.y))
        
        self.bottom_side = Line(start = Point(left_side.start.x, bottom_side.start.y), end = Point(right_side.start.x, bottom_side.start.y))

        self.width = self.top_side.compute_length()
        self.height = self.left_side.compute_length()
        self.pointc = Point(x = (self.bottom_side.start.x + self.width / 2), y = (self.left_side.end.x + self.height / 2))
        
    def compute_area(self)-> float:
        return self.width * self.height
    
    def compute_perimeter(self)-> float:
        return (2 * self.width) + (2 * self.height)

    def computer_interference_point(self, pointint : "Point")-> bool:
        a : float = self.width/2
        b : float = self.height/2
        return self.pointc.x - a < pointint.x < self.pointc.x + a and self.pointc.y - b < pointint.y < self.pointc.y + b 
    
#* Programa principal
linea_1 = Line(start = Point(4,7),end = Point(4,2))
linea_2 = Line(start = Point(4,7),end = Point(7,7))
linea_3 = Line(start = Point(7,7),end = Point(7,2))
linea_4 = Line(start = Point(4,2),end = Point(7,2))

linea_5 = Line(start = Point(0,1),end = Point(0,4))

rectangulo= Rectangle4Lines(linea_1, linea_2, linea_3, linea_4)

print(rectangulo.width, rectangulo.height)
print(rectangulo.compute_area(), rectangulo.compute_perimeter())

