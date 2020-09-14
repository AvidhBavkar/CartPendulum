# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:06:29 2020

@author: avidh
"""
import time
import pygame

pygame.init()

#initialize 800x600 size screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Animation Test")

running = True
counter = 0;
while (running):
    #dont use infinite loop because that will cause the program to hang
    for event in pygame.event.get():
        #loop through all the events happening right now
        if event.type == pygame.QUIT:
            #if you hit the close button, end the program
            running = False
    screen.fill((0,182,174)) #RGB value
    
    pygame.draw.rect(screen, (255, 255, 255), (400 + counter, 300, 50, 20), 1)
    counter += 0.5
    
    time.sleep(1/120)
    
    pygame.display.update() #update the display
        
pygame.display.quit()
pygame.quit()
    
            