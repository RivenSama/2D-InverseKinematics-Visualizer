import math
import numpy as np
import matplotlib.pyplot as plt


class Arm(object):
    def __init__(self,x,y,leng,angle=0,parent=None):
        self.x = x
        self.y = y
        self.leng = leng
        self.angle = angle
        self.parent = parent
 

    def GetEndX(self):
        angle = self.angle
        parent = self.parent
        while(parent):
            angle += parent.angle
            parent = parent.parent
        endx = self.x + math.cos(angle) * self.leng
        return endx

    def GetEndY(self):
        angle = self.angle
        parent = self.parent
        while(parent):
            angle += parent.angle
            parent = parent.parent
        endy = self.y + math.sin(angle) * self.leng
        return endy

    def EndFactorAngle(self,x,y):
        dx =  x - self.x 
        dy = y - self.y
        angle = math.atan2(dy,dx)
        return angle
        

   

        
        