#!/usr/bin/python
# -*- coding: UTF-8 -*-
from digraph import Digraph
marked = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
prePoints = []
postPoints = []
reversePost = []
# 有向图的拓扑排序,要先判断是否有环，这里就假设已经判断过了，只写排序的过程
# 从小到大


def order(graph, current):
    marked[current] = True
    prePoints.append(current)
    for w in graph.adj(current):
        if not marked[w]:
            order(graph, w)
    postPoints.append(current)

# 拓扑排序。


def topoLogical(graph, current):
    marked[current] = True
    for w in graph.adj(current):
        print 'why'
        print 'w is{w}, current is {current}'.format(w=w, current=current)
        if not marked[w]:
            topoLogical(graph, w)

        if (current > w):
            print postPoints
            global postPoints
            postPoints = []
            print '我是分割线'
            print postPoints
    postPoints.append(current)


if __name__ == "__main__":
    print '这是一个有环图'
    secondGraph = Digraph()

    secondGraph.addEdge(1, 3)
    secondGraph.addEdge(1, 5)
    secondGraph.addEdge(3, 2)
    print secondGraph.vertex

    # order(secondGraph, 1)
    topoLogical(secondGraph, 1)
    print postPoints
