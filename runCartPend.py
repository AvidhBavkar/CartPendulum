# -*- coding: utf-8 -*-
"""
Main program to control program flow
"""
import control.pidController as pid
import animation.cartPendAnimator as anim
import sim.cartPendSim as sim
import utils.logger as logger
import time

logger.setHeaders(
    ['Time', 'Theta', 'ThetaDot', 'ThetaDDot', \
     'CartPos', 'CartPosDot', 'CartPosDDot'])

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Cart Pendulum Simulator Program\n")
print("Available Control Methods:\n")
print("\t[0]: No Active Control")
print("\t[1]: PID Control")
print("\t[2]: LQR Control")

controlOption = input("Select a control method: ")

def nullController(pendAngle, timestep):
    return 0;

if (int(controlOption) == 0):
    controller = nullController
    controllerName = "NullControl"
    print("Null Controller Selected, will not attempt to control pendulum")
elif (int(controlOption) == 1):
    controller = pid.control
    controllerName = "PID"
    print("PID Control Selected")
else:
    controller = nullController
    controllerName = "NullControl"
    print("Invalid selection, will not attempt to control pendulum")
    
runAnim = input("\nRun animated simulation? [y/n]: ")

if (runAnim == 'y' or runAnim == 'Y'):
    runAnim = 1
    print("Running Animation")
    anim.init()
    maxTime = 0
else:
    runAnim = 0
    print("Animation will not display")
    maxTime = float(input("Enter time to simulate in seconds: "));

kDt = 1/100;
t = 0
theta = 0
cartPos = 0

while((runAnim and not(anim.detectedCloseButton()))or(not(runAnim) and t <= maxTime)):
    sim.updateSim()
    theta = sim.getTheta()
    sim.setForce(controller(theta, kDt))
    if(runAnim):
        anim.draw(sim.x, sim.theta)
        time.sleep(kDt)
        
    logger.log(
        [t, sim.theta, sim.thetaDot, sim.thetaDDot, \
         sim.x, sim.xDot, sim.xDDot])
    t+=kDt
if(runAnim):
    anim.close()
    
logger.publish(controllerName, True)
print("Log File Saved, Ending Program")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
