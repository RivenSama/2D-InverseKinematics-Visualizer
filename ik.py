import math
from turtle import onclick, ondrag
import numpy as np
import matplotlib.pyplot as plt
from Arm import Arm
from ArmLinker import ArmLinker

armLinker = ArmLinker(0,0)
x = 50
y = 50

def AddArmToLinker(x):
    armLinker.AddArm(10)

def DrawArm():
    for i in armLinker.armSeg:
        plt.scatter([i.x, i.GetEndX()],[i.y,i.GetEndY()])
        plt.plot([i.x, i.GetEndX()],[i.y,i.GetEndY()])



def onclick(event):
    armLinker.Reach(event.xdata,event.ydata)
    DrawCanvas()
    DrawArm()
    plt.draw()
    
    



def DrawCanvas():
    plt.cla()
    plt.axis([-x, x, -y, y])
    plt.grid(['both'])
    
    


def CreateFig():
    
    fig, ax = plt.subplots()
    DrawCanvas()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    DrawArm()
    plt.show()

 

    


if __name__ == '__main__':
    AddArmToLinker(5)
    AddArmToLinker(5)
    AddArmToLinker(5)
    CreateFig()
    