# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:47:55 2024

@author: replica
"""
import numpy as np
import matplotlib.pyplot as plt
from atom import *
from ABP_density import CIC
from FloodFill import floodfill

def binarization(map_, threshold):
    return list(map(lambda x : list(map(lambda y : 1 if y > threshold else 0, x)), map_))

def draw_map(cmap = 'viridis'):
    plt.figure(dpi=300)
    plt.imshow(map_, cmap)
    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.show()
    
def get_heights(map_):
    heights = [0 for i in range(len(map_[0]))]
    for i in range(len(map_[0])):
        for j in reversed(range(0, len(map_))):
            if map_[j][i] == 1:
                heights[i] = j
                break
    return heights

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

W = []
time = np.arange(0, 1001, 10)
for i in time:
    t = int(i//0.05)
    simulator.load_snapshot('snapshots/ABP/snapshot_%08d.txt'%(t))
    atoms = simulator.world.atoms
    cic = CIC(atoms, 5, width, height)
    map_ = cic.density_map()
    width_ = len(map_[0])
    height_ = len(map_)
    
    for i in range(width_):
        for j in range(50//5):
            map_[j][i] = 1   
    
    draw_map('plasma')
    
    map_ = binarization(map_, 0.8)
    
    draw_map('gray')
    
    clusters = floodfill(map_)
    map_ = [[0 for i in range(width_)] for j in range(height_)]
    for point in max(clusters, key=len):
        i, j = point
        map_[j][i] = 1
    draw_map()
    heights = get_heights(map_)
    #print(heights)
    W.append(np.std(heights))
    
kpz = (0.095)*(width_**0.5) * ((time-160)/width_**1.5)**(1/3)
plt.figure(dpi=300)
plt.plot(time, W, label="KPZ Simulation")
plt.plot(time, kpz, label="Family–Vicsek scaling relation")
plt.legend()
plt.xlabel("time")
plt.ylabel("Standard Deviation of Heights")
plt.show()
    
    
