import numpy as np
import os
import csv

class ControlMapping:
    def __init__(self,depth, maxWidth, maxHeight):
        self.depth = depth
        self.a1 = 20
        self.a2 = 20
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        
        #cellWidth is dependent length of the wrist
        #so essentially
        self.cellWidth = 15
        self.cellHeight = 15
        
    def map_point_to_grid(self, point):
        col_index = int(point.x / self.cellWidth)
        row_index = int(point.y / self.cellHeight)
        
        grid_x = (col_index + 0.5) * self.cellWidth
        grid_y = (row_index + 0.5) * self.cellHeight

        offset_x = point.x - grid_x
        offset_y = point.y - grid_y
        return (grid_x, grid_y, offset_x, offset_y)
    
    def dataStream(self, points):
        #packet(arm1 angle, arm2 angle, x-axis movment, x-axis offset, y-axis offset)
        gridpoints = []
        stream = []
        for point in points:
            gridpoints.append(self.map_point_to_grid(point))
        for point in gridpoints:
            angle = self.solveIK(self.a1, self.a2, self.depth, point[1])
            packet = (angle[0], angle[1], point[0], point[2],point[3])
            stream.append(packet)
        return stream
    
    def writeToCSV(self, stream):
        for packet in stream:
            angle0, angle1,  = (angle[0], angle[1], point[0], point[2],point[3])
    def solveIK(a1,a2,x,y):
        #a1 = length of first segment of arm
        #a2 = length of second segment of arm
        #x = x coordinate of target(depth)
        #y = y coordinate of target(height)
        
        #2 solutions
        #second link higher
        q2 = np.arccos((x**2 + y**2 - a1**2 - a2**2)/(2*a1*a2))
        q1 = np.arctan2(y,x) - np.arctan2(a2*np.sin(q2),a1+a2*np.cos(q2))
        #first link higher
        q2 = -np.arccos((x**2 + y**2 - a1**2 - a2**2)/(2*a1*a2))
        q1 = np.arctan2(y,x) + np.arctan2(a2*np.sin(q2),a1+a2*np.cos(q2))
        #q1 = angle of first segment of arm
        #q2 = angle of second segment of arm
        return (q1, q2)