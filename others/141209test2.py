import numpy as np
class test1:
    def setData(self,angle):
        self.angle=angle
    def sanjiaoqi(self):
        converter=self.angle/180.0*np.pi
        return np.sin(converter)

x=test1()
x.setData(90)
print x.sanjiaoqi()       
