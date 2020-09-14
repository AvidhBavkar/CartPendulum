# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:46:03 2020

@author: avidh
"""
import pygame
import time
import math

kScreenWidth  = 800
kScreenHeight = 600

kTrackHeight = kScreenHeight / 2

kMeters2Pixels = 100
kPixels2Meters = 1/kMeters2Pixels

kCartWidth = 1 * kMeters2Pixels
kCartHeight = 0.5 * kMeters2Pixels

kPendulumRadius = int(0.1 * kMeters2Pixels)
kDefaultPendLength = 1 * kMeters2Pixels

kBackgroundColor = (0, 182, 174)
kCartColor = (255,255,255)
kPendColor = (255,255,255)

screen = 0;
pendLength = 0;

def init(pendLength = kDefaultPendLength):
    pygame.init()
    globals()['screen']=pygame.display.set_mode((kScreenWidth, kScreenHeight))
    pygame.display.set_caption("Cart Pendulum Simulator")
    
    globals()['pendLength'] = pendLength

    
def draw(cartX, pendulumTheta):
    screen.fill(kBackgroundColor)
    
    #draw the track
    pygame.draw.rect(screen, (200,200,200), (0, kScreenHeight - kTrackHeight + kCartHeight, kScreenWidth, 10), 0)
    
    #draw the cart
    cartX,cartY = coordsToScreenRel(cartX * kMeters2Pixels, 0)
    pygame.draw.rect(screen, kCartColor, (cartX - kCartWidth/2, cartY, kCartWidth, kCartHeight), 3)
    
    #draw the pendulum
    pendX = int(cartX - math.sin(pendulumTheta) * pendLength)
    pendY = int(cartY - math.cos(pendulumTheta) * pendLength)
    
    pygame.draw.circle(screen, kPendColor, (pendX, pendY), kPendulumRadius, 0)
    
    pygame.display.update()
    
def coordsToScreenRel(x, y):
    return (kScreenWidth / 2) + x, kScreenHeight - kTrackHeight - y

def close():
    pygame.display.quit()
    pygame.quit()

hasClosed = False

def detectedCloseButton():
    for event in pygame.event.get():
        #loop through all the events happening right now
        if event.type == pygame.QUIT:
            globals()['hasClosed'] = True
    return hasClosed
    
    