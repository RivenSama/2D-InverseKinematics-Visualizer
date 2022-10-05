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
        endx = self.x + math.cos(angle) * self.leng
        return endx

    def GetEndY(self):
        angle = self.angle
        endy = self.y + math.sin(angle) * self.leng
        return endy

    def EndFactorAngle(self,x,y):
        if (x is not None) and (y is not None):
            dx =  x - self.x 
            dy = y - self.y
            self.angle = math.atan2(dy,dx)
        else: return 0

    def Drag(self,x,y):
        if (x is not None) and (y is not None):
            self.EndFactorAngle(x,y)
            print(self.angle)
            self.x = x - math.cos(self.angle) * self.leng
            self.y = y - math.sin(self.angle) * self.leng
            if(self.parent):
                self.parent.Drag(self.x,self.y)
            
        

   

        
        