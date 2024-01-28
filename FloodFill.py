# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:25:26 2024

@author: replica
"""
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
    from collections import deque
    clusters = []
    check = [i[:] for i in map_]
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    H, W = len(map_), len(map_[0])
    for i in range(H):
        for j in range(W):
            if check[i][j]:
                cluster = [(j, i)]
                candidate = deque([(i, j)])
                check[i][j] = 0
                while candidate:
                    x, y = candidate.popleft()
                    for dx, dy in dir:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and check[nx][ny]:
                            check[nx][ny] = 0
                            candidate.append((nx, ny))
                            cluster.append((ny, nx))
                clusters.append(cluster)
    return clusters

def color_maps(map_, clusters):
    color = 1
    for cluster in clusters:
        color += 1
        for i, j in cluster:
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
    
    
