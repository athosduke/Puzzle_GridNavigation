import math
import random
import time
from queue import PriorityQueue
import copy

def find_path(start, goal, scene):
    
    if start==goal or scene[start[0]][start[1]] or scene[goal[0]][goal[1]]:
        return None
    
    rows = len(scene)
    cols = len(scene[0])
    
    def grid_successors(pt):
        x = pt[0]
        y = pt[1]
        if x>0 and not scene[x-1][y]:
            yield (x-1,y)
        if x < rows -1 and not scene[x+1][y]:
            yield (x+1,y)
        if y>0 and not scene[x][y-1]:
            yield (x,y-1)
        if y<cols-1 and not scene[x][y+1]:
            yield (x,y+1)
        if x>0 and y>0 and not scene[x-1][y-1]:
            yield (x-1,y-1)
        if x>0 and y<cols-1 and not scene[x-1][y+1]:
            yield (x-1,y+1)
        if x<rows-1 and y>0 and not scene[x+1][y-1]:
            yield (x+1,y-1)
        if x<rows-1 and y<cols-1 and not scene[x+1][y+1]:
            yield (x+1,y+1)

    def euclidean_g(curr, goal):
        return math.sqrt((curr[0]-goal[0])**2 + (curr[1]-goal[1])**2)

    openlist = PriorityQueue()
    path = []
    knownpt = []
    path.append(start)
    knownpt.append(start)
    #                        f            h  path 
    openlist.put((euclidean_g(start,goal),(0,path)))

    while not openlist.empty():
        mytuple = openlist.get()
        depth = mytuple[1][0]
        paths = mytuple[1][1]
        for pt in grid_successors(paths[-1]):
            if pt not in knownpt:
                knownpt.append(pt)
                newpath = copy.copy(paths)
                newpath.append(pt)
                if pt==goal:
                    #print("--- %s seconds ---" % (time.time() - start_time))
                    return newpath
                newh = depth+1
                newf = euclidean_g(pt,goal)+newh
                openlist.put((newf,(newh,newpath)))
    #print("--- %s seconds ---" % (time.time() - start_time))
    return None
