# -*- coding: utf-8 -*-
"""
Proportional-Integral-Derivative Controller
"""
import math as m

#Constants
kP = 200;
kI = 100;
kD = 20;
kIZone = m.radians(20)

thetaAccum = 0
theta = 0
thetaDot = 0

def control(pendAngle, timestep):
    global theta, thetaDot, thetaAccum, kIZone
    
    thetaDot = (pendAngle - theta) / timestep
    theta = pendAngle;
    thetaAccum = thetaAccum + (theta * timestep)
    
    if (abs(thetaAccum) > kIZone):
        thetaAccum = 0
    
    return kP * -theta + kI * -thetaAccum + kD * -thetaDot
    