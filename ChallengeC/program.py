#!/usr/bin/env python3

import sys

INT_MAX = float('inf')

def read_grid(n):
    grid = [[0 for _ in range(n + 1)]]
    for _ in range(n):
        grid.append([0] + list(map(int,sys.stdin.readline().split())))

    return grid

def find_path(grid, n, m):
    table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    prev = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        table[i][1] = grid[i][1]
        if i > 0:
            prev[i][1] = [i, 0]
    for i in range(1, m + 1):
        table[1][i] = grid[1][i] + table[1][i-1]
        if i > 0:
            prev[1][i] = [1,i - 1]

    prev[1][1] = [0, 0]

    for col in range(2, m + 1):
        for row in range(1, n + 1):
            least = [row, col - 1]
            if row == 1:
                if table[n][col - 1] < table[least[0]][least[1]]:
                    least = [n,col - 1]
                if table[row + 1][col - 1] < table[least[0]][least[1]]:
                    least = [row + 1,col - 1]
            elif row == n:
                least = [row - 1, col - 1]
                if table[row][col - 1] < table[least[0]][least[1]]:
                    least = [row,col - 1]
                if table[1][col - 1] < table[least[0]][least[1]]:
                    least = [1,col - 1]
            else:
                least = [row - 1, col - 1]
                if table[row][col - 1] < table[least[0]][least[1]]:
                    least = [row,col - 1]
                if table[row + 1][col - 1] < table[least[0]][least[1]]:
                    least = [row + 1,col - 1]

            prev[row][col] = least

            table[row][col] = grid[row][col] + table[least[0]][least[1]]
        
        table[-1][i] = min((grid[-1][i] + table[1][i-1]), (grid[-1][i] + table[n][i-1]), (grid[-1][i] + table[n-1][i-1]))
        
    curr_min = INT_MAX
    pos = 0
    for i, val in enumerate(table[1:]):
        if val[-1] < curr_min:
            curr_min = val[-1]
            pos = i
    backtrack = [pos+1]
    curr = prev[pos+1][m]
    print(curr_min)

    while curr[0] != 0 or curr[1] != 0:
        if curr[0] == 0 or curr[1] == 0:
            break
        backtrack.append(curr[0])
        curr = prev[curr[0]][curr[1]]
    backtrack.reverse()
    return backtrack

if __name__ == '__main__':

    while True:
        try:
            locs = [int(x) for x in sys.stdin.readline().split()]
        except:
            break

        if not locs or locs[0] == 0 or locs[1] == 0:
            break

        grid = read_grid(locs[0])
        path = find_path(grid, locs[0], locs[1])
        print(' '.join([str(x) for x in path]))
