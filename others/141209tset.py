import numpy as np
class test1:
    def setAngle(self,angle):
        self.angle=angle
    def sanjiaoqi(self):
        converter=self.angle/180.0*np.pi
        return np.sin(converter)

x=test1()
x.setAngle(45)
print x.sanjiaoqi()                