from Arm import Arm


from Arm import Arm
class ArmLinker:
    def __init__(self, x, y,endArm=None, armSegments=[]):
            self.x = x
            self.y = y
            self.armSeg = armSegments
            self.endArm = endArm
    
    def AddArm(self,leng):
        arm = Arm(0,0,leng)
        if self.endArm is not None:
            arm.x = self.endArm.GetEndX()
            arm.y = self.endArm.GetEndY()
            arm.parent = self.endArm
        else: 
            arm.x = self.x
            arm.y = self.y
        self.armSeg.append(arm)
        self.endArm = arm
        
    def Drag(self,x,y):
        if self.endArm != None:
            self.endArm.Drag(x,y);
       
    def Reach(self,x,y):
        for i in range(100):
            self.Drag(x,y)
            self.Update()

    def Update(self):
            for i in range (len(self.armSeg)):
                arm = self.armSeg[i]
                if(arm.parent):
                    arm.x = arm.parent.GetEndX()
                    arm.y = arm.parent.GetEndY()
                else: 
                    arm.x = self.x
                    arm.y = self.y