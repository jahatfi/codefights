import sys
import copy

#Code for company challenge: Ascend Problem #3

#Returns in order: the next point, the updated height, the updated width
#Note that height OR width gets updated, but not both
def getNextPoint(point, height, width, direction):
    #print("\n\ngetNextPoint(), ",point, type(point))
    print(direction)
    sys.stdout.flush()
    if direction == "left":
        return (point[0]-width, point[1], height, width-1)
    if direction == "right":
        return (int(point[0]) + width, point[1],height, width-1)
    if direction == "up":
        return (point[0], point[1] - height, height-1, width)
    else:
        return (point[0], point[1] + height, height-1, width)

def rectangularSpiral(firstPoint, secondPoint):
    print(firstPoint, type(firstPoint))
    directions = ["right", "down", "left", "up"]
    dirIndx = ""
    width = abs(firstPoint[0] - secondPoint[0])
    height = abs(firstPoint[1]-secondPoint[1])
    
    #In the case that the points lie on a line, the rectangle has no area, and no spiral.Ellipsis
    #Simply return the points given
    if (height == 0) or (width == 0): return (firstPoint, secondPoint)
    
    #Otherwise, the first point to return is the first point given
    points = [copy.deepcopy(firstPoint)]
    point = copy.deepcopy(firstPoint)
    
    #Set the direction index
    #The first point is to the left of the second
    if(firstPoint[0] < secondPoint[0]):
        #The first point is above the second
        if(firstPoint[1] < secondPoint[1]):
            dirIndx = 0
        #The first point is below the second
        else: dirIndx = 3 
            
    #The first point is to the right of the second
    #
    #The first point is above the second
    elif(firstPoint[1] < secondPoint[1]):
        dirIndx = 1
    #The first point is below the second
    else:  dirIndx = 2
    #print(directions[dirIndx])
    
    print("Height: {}, Width: {}, Dir: {}".format(height, width, directions[dirIndx]))
    
    #Get the second point (first point not given). 
    #Must be done manually because this first step does NOT decrement the height/width
    if (height > 0 ) and (width > 0):
        point[0], point[1], _, _ = getNextPoint(point, height, width, directions[dirIndx])
        print("Second Point:", point)
        print("Height: {}, Width: {}, Dir: {}".format(height, width, directions[dirIndx]))  
        dirIndx = (dirIndx + 1)%4
        points.append(copy.deepcopy(point))      
    
    #Now get all other points
    while (height > 0 ) or (width > 0):
        point[0], point[1], height, width = getNextPoint(point, height, width, directions[dirIndx])
        if (height < 0) or (width < 0 ):
            print("Terminating.")
            break
        print("Point:", point)
        print("Height: {}, Width: {}, Dir: {}".format(height, width, directions[dirIndx]))  
        
        dirIndx = (dirIndx + 1)%4
        points.append(copy.deepcopy(point))
        
    print(points)
    return points
