#!/usr/bin/python
# -*- coding: UTF-8 -*-
from digraph import Digraph
marked = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
tracked = []


def directDFS(graph, s):
    marked[s] = True

    for w in graph.adj(s):
        if not marked[w]:
            tracked.append(w)
            directDFS(graph, w)


def isVRearch(s):
    return s in tracked


global hasCirle
# 图是否有环
hasCirle = False

circleStack = []


def isGraphHasCircle(graph, current, start):
    if hasCirle:
        return
    marked[current] = True
    circleStack.append(current)
    for w in graph.adj(current):
        print 'current cirlce :'
        print circleStack
        if (w in circleStack):
            global hasCirle
            hasCirle = True
            return
        if not marked[w]:
            isGraphHasCircle(graph, w, start)
    if not hasCirle:
        circleStack.pop()


def startCheckCirle(graph):
    marked[1] = True
    circleStack.append(1)
    for w in graph.adj(1):
        if not marked[w]:
            isGraphHasCircle(graph, w, 1)
    print hasCirle


if __name__ == "__main__":
    # newGraph = Digraph()

    # newGraph.addEdge(1, 2)
    # newGraph.addEdge(1, 3)
    # newGraph.addEdge(2, 4)
    # newGraph.addEdge(4, 3)

    # # directDFS(newGraph, 3)
    # startCheckCirle(newGraph)

    # print hasCirle

    print '这是一个有环图'
    secondGraph = Digraph()

    # secondGraph.addEdge(1, 2)
    # secondGraph.addEdge(2, 1)
    # secondGraph.addEdge(2, 4)
    # secondGraph.addEdge(4, 3)
    # secondGraph.addEdge(3, 1)

    secondGraph.addEdge(1, 2)
    secondGraph.addEdge(1, 5)
    secondGraph.addEdge(3, 1)
    secondGraph.addEdge(3, 4)
    secondGraph.addEdge(4, 3)
    secondGraph.addEdge(4, 6)
    secondGraph.addEdge(5, 3)
    secondGraph.addEdge(5, 4)
    secondGraph.addEdge(6, 5)
    print secondGraph.vertex
    startCheckCirle(secondGraph)

    print circleStack
