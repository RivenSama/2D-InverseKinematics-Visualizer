import math
from turtle import onclick, ondrag
import numpy as np
import matplotlib.pyplot as plt
from Arm import Arm
from ArmLinker import ArmLinker

armLinker = ArmLinker(0,0)
armLinker.AddArm(10)
armLinker.AddArm(5)
armLinker.AddArm(2)


def onclick(event):
        


    plt.cla()

    plt.axis([-20, 20, -20, 20])
    plt.grid(['both'])
    
    

    armLinker.Reach(event.xdata,event.ydata)
    for i in armLinker.armSeg:
        
        plt.scatter([i.x, i.GetEndX()],[i.y,i.GetEndY()])
        plt.plot([i.x, i.GetEndX()],[i.y,i.GetEndY()])

    plt.draw()



    


def CreateFig():
    
    fig, ax = plt.subplots()
    ax.axis([-20, 20, -20, 20])
    ax.grid(['both'])

    #cid = fig.canvas.mpl_connect('motion_notify_event', on_move)
    cid = fig.canvas.mpl_connect('button_press_event', onclick)


    plt.show()

 

    


if __name__ == '__main__':
    CreateFig()
    