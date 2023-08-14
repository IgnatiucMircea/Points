import Functions

class tests:
    def __init__(self):
        self.__coord_x=0
        self.__coord_y=0
        self.__color=''
    
    def set_point1(self):
        points=[]
        point1=Functions.MyPoint(1,2,'red')
        point2=Functions.MyPoint(2,3,'blue')
        point3=Functions.MyPoint(1,2,'green')
        points.append(point1)
        points.append(point2)
        points.append(point3)
        return points

    def set_point2(self):
        points=[]
        point1=Functions.MyPoint(1,2,'red')
        point2=Functions.MyPoint(9,9,'red')
        point3=Functions.MyPoint(1,2,'green')
        points.append(point1)
        points.append(point2)
        points.append(point3)
        return points

    def set_point3(self):
        points=[]
        point1=Functions.MyPoint(1,2,'yellow')
        point2=Functions.MyPoint(2,3,'blue')
        point3=Functions.MyPoint(1,2,'magenta')
        points.append(point1)
        points.append(point2)
        points.append(point3)
        return points

    def get_all_points_test(self):
        self=tests.set_point1(self)
        assert Functions.PointRepository.get_all_points(self)=="Point(1,2) of color red\nPoint(2,3) of color blue\nPoint(1,2) of color green"
    
    def run_tests():
        self=[]
        tests.get_all_points_test(self)