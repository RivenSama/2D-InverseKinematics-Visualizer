import math
import numpy as np
import matplotlib.pyplot as plt


class Arm(object):                                                  #This class represents a segment of the arm
    def __init__(self,x,y,leng,angle=0,parent=None):
        self.x = x
        self.y = y
        self.leng = leng
        self.angle = angle
        self.parent = parent
 

    def GetEndX(self):
        angle = self.angle
        endx = self.x + math.cos(angle) * self.leng             #This function returns the ending X where the segment points                                                           
        return endx                                             # Used to plot the arm segment and other calculations

    def GetEndY(self):
        angle = self.angle
        endy = self.y + math.sin(angle) * self.leng
        return endy

    def EndFactorAngle(self,x,y):                                #This function returns the angle in radians between the raching point
        if (x is not None) and (y is not None):                  # and your arm segment start coordonates
            dx =  x - self.x 
            dy = y - self.y
            self.angle = math.atan2(dy,dx)
        else: return 0

    def Drag(self,x,y):                                         #This function will put the arms segment to the reach point and drag the parents
        if (x is not None) and (y is not None):                 # this line is used to be sure that the click is done on the figure
            self.EndFactorAngle(x,y)
            self.x = x - math.cos(self.angle) * self.leng
            self.y = y - math.sin(self.angle) * self.leng
            if(self.parent):
                self.parent.Drag(self.x,self.y)
            
        

   

        
        