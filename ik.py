import math
from turtle import ondrag
import numpy as np
import matplotlib.pyplot as plt
from Arm import Arm


"""
x_slider = plt.Slider(
ax=plt.subplot(4,2,2),
label='X',
valmin=-20,
valmax=20,
valinit=0,
)
y_slider = plt.Slider(
ax=plt.subplot(4,2,4),
label='Y',
valmin=-20,
valmax=20,
valinit=0,
)
z_slider = plt.Slider(
ax=plt.subplot(4,2,6),
label='Z',
valmin=-90,
valmax=20,
valinit=0,
)

def CreateFig():

    
    x_slider.on_changed(update)
    y_slider.on_changed(update)
    z_slider.on_changed(update)
    plt.subplot(1,2,1).cla()
    plt.subplot(1,2,1)
    plt.axis([-20, 20, -20, 20])
    
    plt.grid(['both'])
    plt.show()

def update(val):
    plt.subplot(1,2,1).cla()
    plt.subplot(1,2,1)
    plt.axis([-20, 20, -20, 20])
    plt.grid(['both'])
    arm = Arm(0,0,5)
    arm.angle = arm.EndFactorAngle(x_slider.val,y_slider.val)
    print(arm.EndFactorAngle(x_slider.val,y_slider.val))
    
    #arm2 = Arm(arm.GetEndX(),arm.GetEndY(),5, y_slider.val,arm)
    #arm3 = Arm(arm2.GetEndX(),arm2.GetEndY(),5, z_slidek.val,arm2)
    arm.show()
    #arm2.show()
    #arm3.show()
    

"""









def on_move(event):


    
    arm = Arm(0,0,5,0)
    new_angle = arm.EndFactorAngle(event.xdata,event.ydata)
    arm.angle = new_angle
    arm2 = Arm(arm.GetEndX(),arm.GetEndY(),5,-20,arm)
    arm3 = Arm(arm2.GetEndX(),arm2.GetEndY(),5,0,arm)

    plt.cla()
    plt.axis([-20, 20, -20, 20])
    plt.grid(['both'])
    
    plt.scatter([arm.x, arm.GetEndX()],[arm.y,arm.GetEndY()])
    plt.scatter([arm2.x, arm2.GetEndX()],[arm2.y,arm2.GetEndY()])
    plt.scatter([arm3.x, arm3.GetEndX()],[arm3.y,arm3.GetEndY()])
    plt.plot([arm.x,arm.GetEndX()],[arm.y,arm.GetEndY()])
    plt.plot([arm2.x, arm2.GetEndX()],[arm2.y,arm2.GetEndY()])
    plt.plot([arm3.x, arm3.GetEndX()],[arm3.y,arm3.GetEndY()])
    plt.draw()



    
    


def CreateFig():
    
    fig, ax = plt.subplots()
    ax.axis([-20, 20, -20, 20])
    ax.grid(['both'])
    cid = fig.canvas.mpl_connect('motion_notify_event', on_move)


    plt.show()

 

    


if __name__ == '__main__':
    CreateFig()
    