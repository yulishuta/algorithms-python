#!/usr/bin/python
# -*- coding: UTF-8 -*-

from digraph import Digraph
from diGraphOrder import DigraphOrder

marked = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
count = 1
countOfPoint = {}


class SCC:
    def __init__(self):
        self.edge = {}

    def getAllPath(self, graph, start):
        graph.getEdge(start)
        self.edge = graph.edge

    def getReverseGraph(self, grap):
        for pointer in grap.getPoints():
            if not marked[pointer]:
                self.reverseGraphItem(pointer)

    def reverseGraphItem(self, graph, s):
        marked[s] = True

        # for w in graph.adj(s):

    # 错误的算法。edge的问题
    def strongConnected(self, v, w):
         # 查看v和w是否是强联通分类
        # 如果从v出发，能否找到w
        start = v
        while(self.edge[start] != w and self.edge[start]):
            start = self.edge[start]

        if (start == w):
            print 'v->w yes'
        else:
            print 'v->w no'
        start = w

        while(self.edge[start] != v and self.edge[start]):
            start = self.edge[start]

        if (start == v):
            print 'w-> yes'
        else:
            print 'w-> no'

    def reverseOrder(self, graph, s, orderReverse):
        marked[s] = True

        for edgePoint in graph.adj(s):
            if (not marked[edgePoint]):
                self.reverseOrder(graph, edgePoint, orderReverse)
        orderReverse.append(s)

    def getReverseOrderOfReverse(self, graph):
        reversedGraph = graph.reverse()

        print 'reversedGraph'
        print reversedGraph.getPoints()
        orderReverse = []
        points = graph.getPoints()
        for point in points:
            if (not marked[point]):
                self.reverseOrder(reversedGraph, point, orderReverse)
        orderReverse.reverse()
        print 'orderReverseReverset'
        print orderReverse
        return orderReverse

    def initMarked(self):
        for key in marked:
            marked[key] = False

    def dfs(self, G, s):
        marked[s] = True
        countOfPoint[s] = count
        for v in G.adj(s):
            if (not marked[v]):
                self.dfs(G, v)
    # 正确的算法
    def rightStrongConnected(self, graph):

        # 获取该反向图的逆向排序
        digraphOrder = DigraphOrder(6, graph.reverse())
        reversePost = digraphOrder.getReversePostOrder()
        self.initMarked()

        points = graph.getPoints()
        for p in reversePost:
            if(not marked[p]):
                self.dfs(graph, p)
            global count
            count = count+1
        print '获取count'
        print count

        print '获取count path'
        print countOfPoint


if __name__ == "__main__":
    secondGraph = Digraph()

    secondGraph.addEdge(1, 2)
    secondGraph.addEdge(1, 5)
    secondGraph.addEdge(3, 1)
    secondGraph.addEdge(3, 4)
    secondGraph.addEdge(4, 3)
    secondGraph.addEdge(4, 6)
    secondGraph.addEdge(5, 3)
    secondGraph.addEdge(5, 4)
    secondGraph.addEdge(6, 5)

    # print '获取edge...'

    # scc = SCC()
    # scc.getAllPath(secondGraph, 1)

    # print '获取Path...'
    # print secondGraph.edge
    # scc.strongConnected(1, 5)

    scc = SCC()
    print scc.rightStrongConnected(secondGraph)
