#!/usr/bin/env python3

import sys
import heapq
import collections as col

Graph = col.namedtuple('Graph', 'labels edges')

def create_paths(adj, n):
    vals = {}
    for v in adj:
        if v[0] not in vals.keys():
            vals[v[0]] = []
        if v[1] not in vals.keys():
            vals[v[1]] = []
        vals[v[0]].append(v[1])
        vals[v[1]].append(v[0])

    return vals

def find_paths(vals):
    start = list(vals.keys())[0]
    start = vals[start][0]
    loop = True
    paths = {}
    poss = []

    while loop:
        frontier = [(0, start, start)]
        visited = {}

        while frontier:
            cost, fr, to = heapq.heappop(frontier)

            if to in visited:
                continue

            visited[to] = fr

            for neighbor in vals[to]:
                heapq.heappush(frontier, (cost + 1, to, neighbor)) #pushes neighbors from the adjacency list

        paths.update(visited)
        poss.append(visited)

        loop = False
        for i in list(vals.keys()):
            if i not in list(paths.keys()):
                loop = True
                start = i
                break

    return poss

if __name__ == '__main__':
    inputs = [line.rstrip().split() for line in sys.stdin]
    
    count = 1
    while inputs:
        adj = []
        poss = []
        verts = int(inputs.pop(0)[0])
        edges = int(inputs.pop(0)[0])
        for _ in range(edges):
            adj.append([int(x) for x in inputs.pop(0)])
        
        vals = create_paths(adj, verts)

        paths = find_paths(vals)

        for p in paths:
            k = [int(x) for x in p.keys()]
            k.sort()
            poss.append(k)
        for n in range(1, verts+1):
            found = False
            for p in poss:
                if n in p:
                    found = True
            if not found:
                poss.append([n])
        poss.sort(key=lambda x: x[0])
        if len(poss) == 1:
            print("Graph {} has 1 group:".format(count))
        else:
            print("Graph {} has {} groups:".format(count, len(poss)))
        for key in poss:
            key = [str(n) for n in key]

            print(' '.join(key))
        count += 1
