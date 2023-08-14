from os import error
import matplotlib.pyplot as plt

class MyPoint:
    def __init__(self):
        self.__coord_x=0
        self.__coord_y=0
        self.__color=''

    def get_coord_x(self):
        return self.__coord_x
    def get_coord_y(self):
        return self.__coord_y
    def get_color(self):
        return self.__color
    
    """
    the functions get are used for returning coordinates or colors
    """

    
    def set_coord_x(self,x:int):
        self.__coord_x=x
    def set_coord_y(self,y:int):
        self.__coord_y=y
    def set_color(self,color:str):
        self.__color=color
    
    """
    the functions set are used for changing the coordinates or colors
    """


    def color_index(self,color):
        if self.__color==color:
            return True
    
    """
    the functions color_index is used for checking if a given color is the same as a point's color
    """

    
    def is_in_square(self,x,y,length):     
        if (self.__coord_x>=x and self.__coord_x<=x+length) and (self.__coord_y<=y and self.__coord_y>=y-length):
            return True
        
    def is_in_rectangle(self,x,y,length,width):     
        if (self.__coord_x>=x and self.__coord_x<=x+length) and (self.__coord_y<=y and self.__coord_y>=y-width):
            return True

    def is_in_circle(self,x,y,radius):
        if (self.__coord_x - x)**2 + (self.__coord_y - y)**2 < radius**2:
            return True       

    """
    the functions is_in are checking if the poits are in a square circle or rectangle
    """


    def __str__(self):               
        return 'Point({},{}) of color {}'.format(self.__coord_x, self.__coord_y, self.__color)
    
    """
    the function __str__ is used for printing points
    """


class PointRepository:

    def __init__(self):
        self.__coord_x=0
        self.__coord_y=0
        self.__color=''


    def get_all_points(self):
        all_points=[]
        for i in range(len(self)):
            all_points.append(MyPoint.__str__(self[i]))
        return all_points

    """
    the function get_all_points returns all points
    """


    def get_poit_at_index(self,index):
        return MyPoint.__str__(self[index])

    """
    the function get_poit_at_index returns the point at the given index
    """


    def get_points_with_same_color(self,color):
        points_with_same_color=[]
        index=False
        for i in range(len(self)):
            if MyPoint.color_index(self[i],color)==True:
                index=True
                points_with_same_color.append(self[i])
        if index==False:
            return IndexError
        else:
            return points_with_same_color

    """
    the function get_points_with_same_color returns all the points with the same given color,
    if there aren't any it returns IndexError
    """


    def square(self,top_left_x,top_left_y,length):
        points_in_square=[]
        index=False
        for i in range(len(self)):
            if MyPoint.is_in_square(self[i],top_left_x,top_left_y,length)==True:
                points_in_square.append(MyPoint.__str__(self[i]))
                index=True
        if index==False:
            return IndexError
        else:
            return points_in_square

    """
    the function square returns all points in a given square
    """


    def distance(self,input_1):
        x1=MyPoint.get_coord_x(self[0])    
        x2=MyPoint.get_coord_x(self[1])
        y1=MyPoint.get_coord_y(self[0])
        y2=MyPoint.get_coord_y(self[1])
        min_dist=((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
        max_dist=min_dist
        for i in range(len(self)):
            for j in range(i+1,len(self)):
                x1=MyPoint.get_coord_x(self[i])    
                x2=MyPoint.get_coord_x(self[j])
                y1=MyPoint.get_coord_y(self[i])
                y2=MyPoint.get_coord_y(self[j]) 
                dist=((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
                if dist<min_dist:
                    min_dist=dist
                if dist>max_dist:
                    max_dist=dist
        if input_1=='min distance':
            return min_dist
        elif input_1=='max distance':
            return max_dist
    
    """
    the function distance is used for both minimum and maximum distance returning them
    """


    def update(self,index,x,y,color):
        MyPoint.set_coord_x(self[index],x)
        MyPoint.set_coord_y(self[index],y)
        MyPoint.set_color(self[index],color)
        return self[index]

    """
    the function update replaces old coordinates and color with new given ones
    """


    def delete(self,index):
        new_list=[]
        for i in range(len(self)):
            if i!=index:
                new_list.append(self[i])
        return new_list

    """
    the function delete returns the list without the point at the given index
    """


    def delete_square(self,top_left_x,top_left_y,length):
        new_list=[]
        index=False
        for i in range(len(self)):
            if MyPoint.is_in_square(self[i],top_left_x,top_left_y,length)!=True:
                new_list.append(self[i])
            else:
                index=True
        new_list=[]
        if index==False:
            return IndexError
        else:
            return new_list

    """
    the function delete_square checks for points isinde the given square and deletes them,
    if there aren't any it returns IndexError
    """


    def plot(self):
        x=[]
        y=[]
        color=[]
        for i in range(len(self)):
            x.append(MyPoint.get_coord_x(self[i]))
            y.append(MyPoint.get_coord_y(self[i]))
            color.append(MyPoint.get_coord_x(self[i]))
        plt.scatter(x,y,color)
        plt.show() 

    """
    the function plot plots the points in a chart
    """


    def in_circle(self,center_x,center_y,radius):
        points_in_circle=[]
        index=False
        for i in range(len(self)):
            if MyPoint.is_in_circle(self[i],center_x,center_y,radius)==True:
                points_in_circle.append(self[i])
                index=True
        if index==False:
            return IndexError
        else:
            return points_in_circle

    """
    the function in_circle checks for points that are inside a given circle and returns them,
    if there aren't any it returns IndexError
    """


    def rectangle(self,top_left_x,top_left_y,length,width):
        points_in_rectangle=[]
        index=False
        for i in range(len(self)):
            if MyPoint.is_in_rectangle(self[i],top_left_x,top_left_y,length,width)==True:
                points_in_rectangle.append(self[i])
                index=True
        if index==False:
            return IndexError
        else:
            return points_in_rectangle

    """
    the function rectangle checks for points that are inside a given rectangle and returns them,
    if there aren't any it returns IndexError
    """


    def nr_of_points_with_same_color(self,color):
        index=0
        for i in range(len(self)):
            if MyPoint.color_index(self[i],color)==True:
                index=index+1
        return index

    """
    the function nr_of_points_with_same_color returns the number of points with the same given color
    """
    

    def update_color(self,x,y,color):
        index=False
        for i in range(len(self)):
            if MyPoint.get_coord_x(self[i])==x and MyPoint.get_coord_y(self[i])==y:
                index=True
                MyPoint.set_color(self[i],color)
            if index==True:
                return self
            else:
                return IndexError

    """
    the function update_color updates the color of the point located at the given coordinates,
    if there isn't a point at the given coordinates it returns IndexError
    """


    def shift_x(self,index):
        if len(self)==0:
            return IndexError
        else:
            for i in range(len(self)):
                x=MyPoint.get_coord_x(self[i])
                MyPoint.set_coord_x(self[i],x+index)
            return self

    """
    the function shift_x adds the shifting index to the x coordinate of each point,
    if there are no points it returns IndexError
    """        


    def shift_y(self,index):
        if len(self)==0:
            return IndexError
        else:
            for i in range(len(self)):
                y=MyPoint.get_coord_y(self[i])
                MyPoint.set_coord_y(self[i],y+index)
            return self
    
    """
    the function shift_y adds the shifting index to the y coordinate of each point,
    if there are no points it returns IndexError
    """


    def del_coord(self,x,y):
        new_list=[]
        index=False
        for i in range(len(self)):
            if MyPoint.get_coord_x(self[i])!=x or MyPoint.get_coord_y(self[i])!=y:
                new_list.append(self[i])
            else:
                index=True
        if index==False:
            return IndexError
        else:
            return new_list

    """
    the function del_coord looks for the point with the given coordinates and returns a list without it, 
    if it isn't found it returns an IndexError 
    """


    def del_circle(self,center_x,center_y,radius):
        new_list=[]
        index=False
        for i in range(len(self)):
            if MyPoint.is_in_circle(self[i],center_x,center_y,radius)!=True:
                new_list.append(self[i])
            else:
                index=True
        if index==False:
            return IndexError
        else:
            return new_list
        
    """
    the function del_circle checks if the points are in the circle and returns a list
    without the ones inside, if there are none it returns an IndexError 
    """


    def del_distance(self,distance,x,y):
        new_list=[]
        index=False
        for i in range(len(self)):
            x1=MyPoint.get_coord_x(self[i])    
            y1=MyPoint.get_coord_y(self[i])
            dist=((((x - x1 )**2) + ((y-y1)**2) )**0.5)
            if dist>distance:
                new_list.append(self[i])
            else:
                index=True
        if index==False:
            return IndexError
        else:
            return new_list

    """
    the function del_distance checks the distance between the given point 
    and the points in the list and returns a list without the poits within the distance,
    if there are none it returns an IndexError 
    """
        
