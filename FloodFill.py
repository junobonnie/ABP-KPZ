# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:25:26 2024

@author: replica
"""
import copy

def datas(map_):
    height, width = len(map_), len(map_[0])
    result = []
    for j in range(height):
        for i in range(width):
            if map_[j][i] == 1:
                result.append((i, j))
    return result

def next_candidates(map_, cluster, candidates, point):
    height, width = len(map_), len(map_[0])
    i, j = point
    result = []
    dxdys = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in dxdys:
        if not (i+dx == -1 or i+dx == width or j+dy == -1 or j+dy == height):
            if map_[j+dy][i+dx] == 1 and not (i+dx, j+dy) in cluster+candidates:
                result.append((i+dx, j+dy))
    return result

def floodfill(map_):
    datas_ = datas(map_)
    clusters = []
    while datas_:
        cluster = []
        candidates = [datas_[0]]
        while candidates:
           candidate = candidates.pop()
           candidates.extend(next_candidates(map_, cluster, candidates, candidate))
           cluster.append(candidate)
           datas_.remove(candidate)
        clusters.append(cluster)
    return clusters

def color_maps(map_, clusters):
    color = 1
    for cluster in clusters:
        color += 1
        for point in cluster:
            i, j = point
            map_[j][i] = color
    
if __name__=="__main__":
    import random as r
    height, width = 100, 100
    map_ = [[r.randint(0, 1) for i in range(width)] for j in range(height)]
    
    import matplotlib.pyplot as plt
    plt.figure(dpi=300)
    plt.imshow(map_, cmap='rainbow')
    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.show()
    
    clusters = floodfill(map_)
    color_maps(map_, clusters)
    plt.figure(dpi=300)
    plt.imshow(map_, cmap='rainbow')
    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.show()
    
    