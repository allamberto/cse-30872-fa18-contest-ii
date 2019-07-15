#!/usr/bin/env python3

import sys
import math

# Functions

# Main Execution
if __name__ == "__main__":
    for line in sys.stdin:
        X, Y = map(int, line.split())
        numbers = list(range(X, Y + 1))
        hops = 0
        step = 0
        curr = numbers[0]
        target = numbers[-1]
        greatestStep = math.floor(math.sqrt(target - curr))
        if target == curr:
            print("{} -> {} takes {} hops".format(X, Y, 0))
            continue

        while step < greatestStep:
            curr += step
            hops += 1
            step += 1

        while curr < target:
            if target - curr >= ((pow(step, 2) + step) / 2):
                curr += step
            else:
                step -= 1
                curr += step
            hops += 1

        print("{} -> {} takes {} hops".format(X, Y, hops - 1))
