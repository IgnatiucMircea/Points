import Functions

points=[]
point=Functions.MyPoint()
colors = ['red', 'green', 'blue', 'yellow', 'magenta']
index=0

def Command_list():
    print("Input:  'set' to give values to the last point ")
    print("Input:  'get' to get the values of the last point")
    print("Input:  'get all' to get the values of all the points in the list")
    print("Input:  'point at index' to get the values of the point at the given index")
    print("Input:  'same color' to get the values of the points with the same given color")
    print("Input:  'square' to get the points that are in a given square")
    print("Input:  'min distance' to get the minimum distance between two points")
    print("Input:  'update' to update a point at a given index")
    print("Input:  'delete' to delete a point at a given index")
    print("Input:  'delete square' to delete all points inside a given square")
    print("Input:  'plot' to plot all points in a  chart")
    print("Input:  'help 2' to go to the next page")

def Command_list2():
    print("Input:  'circle' to get all points inside a given circle")
    print("Input:  'rectangle' to get all points inside a given rectangle")
    print("Input:  'max distance' to get the maximum distance between two points")
    print("Input:  'nr color' to get the number of points with the same given color")
    print("Input:  'update color' to update the color of a point given its coordinates")
    print("Input:  'shift x' to shift all points on the x axis")
    print("Input:  'shift y' to shift all points on the y axis")
    print("Input:  'del coord' to delete a point by its coordinates")
    print("Input:  'delete circle' to delete all points inside a given circle")
    print("Input:  'del distance' to delete all points within a certain distance from a given poin")
    print("Input: 'help' to go to the previous page")

def Menu():
    print("\n\n\n\n\n")
    print("Input: 'help' to print command list \n")
    while True:
        try:
            input_1=input("Input >>")
            print(" ")
            if input_1=='exit':
                print("Exitting . . .")
                print(" ")
                break
        
            elif input_1=='help':
                Command_list()
                print(" ")

            elif input_1=='help 2':
                Command_list2()
                print(" ")

            elif input_1=='set':
                point=Functions.MyPoint()
                x=int(input("  Coordonate x: "))
                Functions.MyPoint.set_coord_x(point , x)
                y=int(input("  Coordonate y: "))
                Functions.MyPoint.set_coord_y(point , y)
                color=input("  Color: ")
                while color not in colors:
                    print("  There is no such color")
                    color=input("  color: ")
                Functions.MyPoint.set_color(point , color)
                points.append(point)
                print(" ")

            elif input_1=='get':
                if points==[]:
                    print("  There are no points in the list")
                else:
                    print('  Input:  "x" to print coordonate x\n  Input:  "y" to print coordonate y\n  Input:  "color" to print the color')
                    print('  Input:  "all" to print all\n  Input:  "exit" to go back')
                    while True:
                        input_2=input("  Input >>")
                        if input_2=='exit':
                            break
                        elif input_2=='x':
                            print("  coordonate x is:", Functions.MyPoint.get_coord_x(points[index]))
                        elif input_2=='y':
                            print("  coordonate y is:", Functions.MyPoint.get_coord_y(points[index]))
                        elif input_2=='color':
                            print("  color is:", Functions.MyPoint.get_color(points[index]))
                        elif input_2=='all':
                            print("  ",Functions.MyPoint.__str__(points[index]))
                print(" ")            

            elif input_1=='get all':
                if points==[]:
                    print("  There are no points in the list")
                else:
                    print(" ",*Functions.PointRepository.get_all_points(points),sep='\n')
                print(" ")

            elif input_1=='point at index':    
                point_index=int(input("  Input index: "))
                try:
                    print(" ",Functions.PointRepository.get_poit_at_index(points , point_index))
                except IndexError:
                    print("  Index is out of range")
                print(" ")

            elif input_1=='same color':    
                color=input("  color: ")
                while color not in colors:
                    print("  There is no such color")
                    color=input("  color: ")
                points_with_same_color=Functions.PointRepository.get_points_with_same_color(points,color)
                if points_with_same_color==IndexError:
                    print("  There are no points with this color")
                else:
                    for i in range(len(points_with_same_color)):
                        print(" ",Functions.MyPoint.__str__(points_with_same_color[i]))
                print(" ")

            elif input_1=='square':
                top_left_x=int(input("  top left corner x coordinate: "))
                top_left_y=int(input("  top left corner y coordinate: "))
                length=int(input("  length of the sides: "))
                points_in_square=Functions.PointRepository.square(points,top_left_x,top_left_y,length)
                if points_in_square==IndexError:
                    print("  There are no points in th given square")
                else:
                    print(" ",*points_in_square,sep='\n')
                print(" ")
            
            elif input_1=='min distance':
                if len(points)<2:
                    print("  there are not enough points to calculate a distance \n") 
                else:
                    print(Functions.PointRepository.distance(points,input_1))
                    print(" ")
            
            elif input_1=='update': 
                index1=int(input("  Input index: "))
                x=int(input("  Coordonate x: "))
                y=int(input("  Coordonate y: "))
                color=input("  Color: ")
                while color not in colors:
                    print("  There is no such color")
                    color=input("  color: ")
                try:
                    points[index1]=Functions.PointRepository.update(points,index1,x,y,color)
                    print("  Point updated")
                except IndexError:
                    print("  Index is out of range")
                print(" ")

            elif input_1=='delete':
                index1=int(input("  Input index: "))
                if index1<len(points):
                    points[:]=Functions.PointRepository.delete(points,index1)
                    print("  Point deleted successfully")
                else:
                    print("  index is out of range")
                print(" ")

            elif input_1=='delete square':
                top_left_x=int(input("  top left corner x coordinate: "))
                top_left_y=int(input("  top left corner y coordinate: "))
                length=int(input("  length of the sides: "))
                if Functions.PointRepository.delete_square(points,top_left_x,top_left_y,length)==IndexError:
                    print("  there are no points in the square")
                else:
                    points[:]=Functions.PointRepository.delete_square(points,top_left_x,top_left_y,length)
                    print("  points have been deleted")
                print(" ")

            elif input_1=='plot':
                Functions.PointRepository.plot(points)

            elif input_1=='circle': 
                center_x=int(input("  center x coordinate: "))
                center_y=int(input("  center y coordinate: "))
                radius=int(input("  radius of the circle: "))
                points_in_circle=Functions.PointRepository.in_circle(points,center_x,center_y,radius)
                if points_in_circle==IndexError:
                    print("  there are no points in the circle") 
                else:
                        print(" ",*points_in_circle, sep='\n')
                print(" ")
            
            elif input_1=='rectangle':
                top_left_x=int(input("  top left corner x coordinate: "))
                top_left_y=int(input("  top left corner y coordinate: "))
                length=int(input("  length of the rectangle: "))
                width=int(input("  width of the rectangle: "))
                points_in_rectangle=Functions.PointRepository.rectangle(points,top_left_x,top_left_y,length,width)
                if points_in_rectangle==IndexError:
                    print("  there are no points in the rectangle")
                else:
                    print("  ", *points_in_rectangle, sep='\n')
                print(" ")

            elif input_1=='max distance': 
                if len(points)<2:
                    print("  there are not enough points to calculate a distance \n") 
                else:
                    print(Functions.PointRepository.distance(points,input_1))
                    print(" ")


            elif input_1=='nr color':
                color=input("  color: ")
                while color not in colors:
                    print("  There is no such color")
                    color=input("  color: ")
                index1=Functions.PointRepository.nr_of_points_with_same_color(points,color)
                if index1==0:
                    print("  there are no points with this color")
                else:
                    print("  the number of points with the color",color,"is:",index1)
                print(" ")

            
            elif input_1=='update color':
                x=int(input("  Coordonate x: "))
                y=int(input("  Coordonate y: "))
                color=input("  Color: ")
                while color not in colors:
                    print("  There is no such color")
                    color=input("  color: ")
                if Functions.PointRepository.update_color(points,x,y,color)==IndexError:
                    print("  There is no point at the given coordinates")
                else:
                    print("  Point updated")
                    points[:]=Functions.PointRepository.update_color(points,x,y,color)
                print(" ")
                
            
            elif input_1=='shift x':
                index1=int(input("  Input the amount to shift: "))
                if Functions.PointRepository.shift_x(points,index1)==IndexError:
                    print("  There are no points to shift")
                else:
                    print("  Points shifted")
                    points[:]=Functions.PointRepository.shift_x(points,0)
                print(" ") 


            elif input_1=='shift y':
                index1=int(input("  Input the amount to shift: "))
                if Functions.PointRepository.shift_y(points,index1)==IndexError:
                    print("  There are no points to shift")
                else:
                    print("  Points shifted")
                    points[:]=Functions.PointRepository.shift_y(points,0)
                print(" ")  


            elif input_1=='del coord':
                point_x=int(input("  Input the x coordinate of the point: "))
                point_y=int(input("  Input the y coordinate of the point: "))
                if Functions.PointRepository.del_coord(points,point_x,point_y)==IndexError:
                    print("  There are no points at the given goordinates")
                else:
                    print("  Point has been deleted")
                    points[:]=Functions.PointRepository.del_coord(points,point_x,point_y)
                print(" ") 
            

            elif input_1=='del circle':
                center_x=int(input("  center x coordinate: "))
                center_y=int(input("  center y coordinate: "))
                radius=int(input("  radius of the circle: "))
                if Functions.PointRepository.del_circle(points,center_x,center_y,radius)==IndexError:
                    print("  There are no points in the given circle")
                else:
                    print("  Points have been deleted")
                    points[:]=Functions.PointRepository.del_circle(points,center_x,center_y,radius)
                print(" ")  


            elif input_1=='del distance':
                point_x=int(input("  Input the x coordinate of the point: "))
                point_y=int(input("  Input the y coordinate of the point: "))
                distance=int(input("  Input the distance from the given point: "))
                if Functions.PointRepository.del_distance(points,distance,point_x,point_y)==IndexError:
                    print("  There are no points within the given distance from the point")
                else:
                    print("  Points have been deleted")
                    points[:]=Functions.PointRepository.del_distance(points,distance,point_x,point_y)
                print(" ")  


            else:
                print("Command doesn't exist \n")


        except ValueError:
            print("\n  The input must be an integer! \n")

    """
    Function Menu executes all commands 
    """
