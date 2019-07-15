#!/usr/bin/env python3

import sys

# Functions

# Main Execution
if __name__ == "__main__":
    for line in sys.stdin:
        tacos = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
        sum = 0
        for x, i in enumerate(tacos):
            sum += pow(2, x) * i;
        print(sum)
