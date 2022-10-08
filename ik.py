import math
from turtle import update
from matplotlib.widgets import TextBox
import numpy as np
import matplotlib.pyplot as plt
from Arm import Arm
from ArmLinker import ArmLinker

armLinker = ArmLinker(0,0)


def AddArmToLinker(x):
    armLinker.AddArm(x)

def DrawArm():
    for i in armLinker.armSeg:
        print(math.degrees(i.angle))
        plt.scatter([i.x, i.GetEndX()],[i.y,i.GetEndY()])
        plt.plot([i.x, i.GetEndX()],[i.y,i.GetEndY()])


def onclick(event):

    armLinker.Reach(event.xdata,event.ydata)
    DrawCanvas()
    DrawArm()
    plt.draw()
    
    
def DrawCanvas(x=20,y=20):
    plt.cla()
    plt.axis([-x, x, -y, y])
    print('x:: ',x)
    plt.grid(['both'])


def CreateFig():
    fig, ax = plt.subplots(figsize=(8,8))

    DrawCanvas()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    DrawArm()
    plt.show()
    


if __name__ == '__main__':
    AddArmToLinker(5)
    AddArmToLinker(5)
    AddArmToLinker(5)
    CreateFig()




    
