#!/usr/bin/env python3

import collections
import sys

# Functions

# read in graph to default dict
def read_stuff(words):
    marked = set()
    graph = collections.defaultdict(list)
    for j in range(len(words)):
        for i in range(len(words)):
            if str_dist(words[j],  words[i]) and words[i] not in marked:
                graph[words[j]].append(words[i])
                marked.add(words[j])

    # this must keep it in the right order for an edge case
    # the sample test works fine without reversing each
    for key in graph:
        graph[key] = sorted(graph[key], reverse=True)

    return graph


# use the classic algorithm from class to traverse graph
def morph(graph, start):
    frontier = [ (start, start) ]
    visited = collections.defaultdict(str)

    while frontier:
        src, dest = frontier.pop()

        if dest in visited:
            continue

        visited[dest] = src
        for neighbor in graph[dest]:
            frontier.append( (dest, neighbor) )
    return visited


# reconstruct path, self explanatory
def find_path(visited, dest):
    curr = dest
    marked = set()
    path = []

    while curr not in marked:
        path.append(curr)
        marked.add(curr)
        curr = visited[curr]

    # lexicographical order
    return sorted(path)


# find if two words are a morph
def str_dist(first, second):
    cnt = 0

    # same size words
    if len(first) == len(second):
        for i in range(len(first)):
            if first[i] != second[i]:
                cnt += 1
        if cnt == 1:
            return True

    # first is one bigger than second word
    elif len(first) == len(second) + 1:
        for i in range(len(second)):
            if second[i] not in first:
                cnt += 1
        if cnt == 0:
            return True

    # second is one bigger than first word
    elif len(second) == len(first) + 1:
        for i in range(len(first)):
            if first[i] not in second:
                cnt += 1
        if cnt == 0:
            return True

    return False


# Main

if __name__ == '__main__':
    words = []
    for line in sys.stdin:
        words.append(line.rstrip())

    # lexicographical order
    words = sorted(words)
    graph = read_stuff(words)

    # find the longest path
    biggest = []
    for word in words:
        visited = morph(graph, word)
        for dest in list(visited.keys()):
            path = find_path(visited, dest)

            if len(path) > len(biggest):
                biggest = path

    print(len(biggest))
    for item in biggest:
        print(item)
