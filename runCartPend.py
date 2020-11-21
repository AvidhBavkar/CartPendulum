# -*- coding: utf-8 -*-
"""
Main program to control program flow
"""
import control.pidController as pid
import animation.cartPendAnimator as anim
import sim.cartPendSim as sim

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Cart Pendulum Simulator Program\n")
print("Available Control Methods:\n\t[1]: PID Control\n\t[2]: LQR Control")
controlOption = input("Select a control method: ")

if (int(controlOption) == 1):
    controller = pid.control
    print("PID Control Selected")
else:
    controller = pid.control
    print("Invalid selection, defaulting to PID Control")
    
runAnim = input("\nRun animated simulation? [y/n]: ")

if (runAnim == 'y' or runAnim == 'Y'):
    runAnim = 1
    print("Running Animation")
    anim.init()
    maxTime = 0
else:
    runAnim = 0
    print("Animation will not display")
    maxTime = float(input("Enter time to simulate in seconds"));

kDt = 1/60;
t = 0
theta = 0
cartPos = 0

while((runAnim and not(anim.detectedCloseButton()))or(not(runAnim) and t <= maxTime)):
    sim.update()
    theta = sim.getTheta()
    