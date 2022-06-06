import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, ERobot, ELink, ETS, PrismaticDH


# link lengths in mm
a1 = float(input("a1 = ")) # for testing,150mm
a2 = float(input("a2 = ")) # for testing,150mm
a3 = float(input("a3 = ")) # for testing,150mm
a4 = float(input("a4 = ")) # for testing,150mm

# link converted to meters
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)
a4 = mm_to_meter(a4)

# link limits converted to meters
lm1 = float(input("lm1 = ")) # 50mm
lm1 = mm_to_meter(lm1)
lm2 = float(input("lm2 = ")) # 50mm
lm2 = mm_to_meter(lm2)
lm3 = float(input("lm3 = ")) # 50mm
lm3 = mm_to_meter(lm3)

# Create Links
CARTESIAN = DHRobot([
    PrismaticDH(0,0,(270/180)*np.pi,a1,qlim=[0,0]),
    PrismaticDH((270/180)*np.pi,0,(270/180)*np.pi,a2,qlim=[0,lm1]),
    PrismaticDH((270/180)*np.pi,0,(90/180)*np.pi,a3,qlim=[0,lm2]),
    PrismaticDH(0,0,0,a4,qlim=[0,lm3])
], name='CARTESIAN')

print('CARTESIAN')


# q paths

#degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi



# q paths
q0 = np.array([0,0,0,0])
q1 = np.array([0,mm_to_meter(float(input("d1 = "))),
                mm_to_meter(float(input("d2 = "))),
                mm_to_meter(float(input("d3 = "))),
                ])
q2 = np.array([0,mm_to_meter(float(input("d1 = "))),
                mm_to_meter(float(input("d2 = "))),
                mm_to_meter(float(input("d3 = "))),
                ])
q3 = np.array([0,mm_to_meter(float(input("d1 = "))),
                mm_to_meter(float(input("d2 = "))),
                mm_to_meter(float(input("d3 = "))),
                ])

# CARTESIAN Commands
tradj1 = rtb.jtraj(q0,q1,50)
tradj2 = rtb.jtraj(q0,q1,50)
tradj3 = rtb.jtraj(q0,q1,50)

CARTESIAN.plot(tradj1.q)
CARTESIAN.plot(tradj2.q)
CARTESIAN.plot(tradj3.q)

CARTESIAN.teach(jointlabels=1)