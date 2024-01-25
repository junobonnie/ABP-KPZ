# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:35:42 2024

@author: replica
"""

import numpy as np
import matplotlib.pyplot as plt
from atom import *

width = 480
height = 360
    
screen = pg.display.set_mode((width, height))
render = Render(screen, width, height)
clock = pg.time.Clock()
    
black = pg.Color('black')
white = pg.Color('white')
red = pg.Color('red')
green = pg.Color('green')
blue = pg.Color('blue')
        
walls = []
atoms = []
    
gravity = Vector(0, 0)
world = World(0, atoms, walls, gravity)
    
simulator = Simulator(0.01, world, render)

time = np.arange(0, 1001, 1)
for i in time:
    t = int(i//0.05)
    simulator.load_snapshot('snapshots/ABP/snapshot_%08d.txt'%(t))
    atoms = simulator.world.atoms
    
    simulator.draw_background(white) #시뮬레이션 배경화면 그리기
    simulator.draw_grid(100) #격자그리기
    simulator.draw_wall() #벽그리기
    simulator.draw_atom() # 원자 그리기
    pg.display.update()