#TODO: convert the calculated shading point pairs into reachable points for
#the robotic arm
import numpy as np
import cv2

class mappedPointOptimizer:
    
    def __init__(self, gridWidth, gridHeight, maxHeight, maxWidth):
       self.horizontalGrid = maxHeight / gridHeight
       self.verticalGrid = maxWidth / gridWidth
       self.gridWidth = gridWidth
       self.gridHeight = gridHeight
    
    def midpoint(self, point1, point2):
        return ((point1[0] + point2[0])/2, (point1[1] + point2[1])/2)
     
    def divideByGrids(self, points):
        grid = [[] for j in range(self.horizontalGrid) for i in range(self.verticalGrid)]
        newPoints = []
        
        for i, gridRow in enumerate(range(self.verticalGrid)):
            for j, gridCol in enumerate(range(self.horizontalGrid, self.gridWidth)):
                #cut into segments according horizontally
                for line in points:
                    if line[0] <= gridCol and line[1] >= gridCol:
                       newPoints.append((line[0],self.midpoint(line[0],line[1])))
        for j, gridCol in enumerate(range(self.horizontalGrid)):
            for i, gridRow in enumerate(range(self.verticalGrid, self.gridHeight)):
                #cut into segments vertically
                for line in newPoints:
                     if line[0] <= gridRow and line[1] >= gridRow:
                       grid[i][j].append((line[0],self.midpoint(line[0],line[1])))
                       
        return grid
    def sortPoint(self, points):
        for point in points:
            pass
        