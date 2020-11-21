# -*- coding: utf-8 -*-
"""
Cart Pendulum Simulation

Contains non-linear mathematical model of motion for inverted pendulum
on cart.
"""
import math as m

kCartMass = 10
kPendMass = 2
kPendLength = 2
kLocalG = 9.8
kDt = 1 / 60.0

F = 0
Fmax = 10

x = 0
xDot = 0
xDDot = 0

theta = m.radians(1)
thetaDot = 0
thetaDDot = 0

def integrate(timestep = kDt):
    global x, xDot, xDDot, theta, thetaDot, thetaDDot
    
    xDot += xDDot * timestep
    x += xDot * timestep
    
    thetaDot += thetaDDot * timestep
    theta += thetaDot * timestep
    
    #Bounds theta between +180 and -180 to simulate a sensor.
    if(theta > m.pi):
        theta = theta - 2*m.pi;
    elif(theta < -m.pi):
        theta = theta + 2*m.pi;

def calculateXDDot():
    """
    Returns second time derivative of x
    -------
    xDDot : Acceleration along the track of the cart
        x is the position of the cart, increasing as the cart moves right.

    """
    
    """
    Equation:
                l(thetaDDot) - gsin(theta)
        xDDot = --------------------------
                        cos(theta)
    """
    xDDot = (kPendLength * thetaDDot - kLocalG * m.sin(theta)) / m.cos(theta)
    globals()['xDDot'] = xDDot
    return xDDot


def calculateThetaDDot():
    """          
    Returns second time derivative of theta
    -------
    thetaDDot : Angular acceleration of the pendulum
        theta is angle from verticle increasing counter-clockwise

    """
    F  = globals()['F']
    M  = globals()['kCartMass']
    mP = globals()['kPendMass']
    g  = globals()['kLocalG']
    l  = globals()['kPendLength']
    
    """
    Equation:
                           (M+m)gsin(theta)
                        F + ---------------- (-) ml*thetaDot*sin(theta)
                              cos(theta)
            thetaDDot = ------------------------------------------------
                                     (M+m)l
                                  ------------ (+) mlcos(theta)
                                   cos(theta)
    """
    
    #numerator:
    thetaDDot= F + (((M+mP)*g*m.sin(theta)) / m.cos(theta)) - mP*l*m.sin(theta)
    
    #finish by dividing by denominator:
    thetaDDot /= (((M+mP)*l) / m.cos(theta)) + mP*l*m.cos(theta)
    
    globals()['thetaDDot'] = thetaDDot
    return thetaDDot

def updateSim(timestep = kDt):
    integrate(timestep)
    calculateThetaDDot()
    calculateXDDot()

def setForce(forceNewtons):
    global F
    F = min(Fmax, max(-Fmax, forceNewtons))

def getTheta():
    return theta
    
#anim.init()

#while(not anim.detectedCloseButton()):
 #   integrate()
  #  F = min(Fmax, max(-Fmax, pidController(theta)))
   # calculateThetaDDot()
    #calculateXDDot()
    
    
    #print(f"X: {xDDot}\tTheta: {m.degrees(theta)}")
    #anim.draw(x, theta)
    #time.sleep(kDt * 1)
#anim.close()
    
    
    