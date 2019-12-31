#!/usr/bin/python
# -*- coding: UTF-8 -*-

from dGraph import DEdgeWeightGraph
import sys


class DMinPath:
    def __init__(self, weightGraph, s):
        self.graph = weightGraph
        self.start = s
        n = weightGraph.v
        node = range(0, n)

        self.edgeTo = dict.fromkeys(node, None)  # 存储顶点到树的最小边
        self.distTo = dict.fromkeys(node, sys.maxint)  # 存储权重
        self.distTo[s] = 0
        self.pg = []
        self.quene = []
        self.hasTravel = []

        self.onQ = dict.fromkeys(node, False)  # 存储权重
        self.hasNegativeCircle = False  # 是否有负权重的环

    def deleteMinWeight(self):
        minDist = sys.maxint
        deleteIndex = sys.maxint
        for idx, dist in enumerate(self.distTo):
            if (dist < minDist):
                minDist = dist
                deleteIndex = idx
        if deleteIndex != sys.maxint:
            return self.pg.pop(deleteIndex)
        else:
            return None

    def foundEdgeOfPg(self, foundEdge):
        foundIndex = -1
        for idx, edge in enumerate(self.pg):
            if edge.isSame(foundEdge):
                foundIndex = idx
                break
        return foundIndex

    def relax(self, edge):
        start = edge.start()
        end = edge.to()
        print self.distTo
        print start
        print end
        if (self.distTo[start] == sys.maxint):
            return
        if (self.distTo[end] > self.distTo[start] + edge.getWeight()):
            self.distTo[end] = self.distTo[start] + edge.getWeight()
            self.edgeTo[end] = edge
            foundIndex = self.foundEdgeOfPg(edge)
            # 这里有问题。如果pg有这条边，新增。没有更新
            if foundIndex == -1:
                self.pg.append(edge)
            else:
                self.pg[foundIndex] = edge

    def addNextPointByEdge(self, edge):
        nextPoint = edge.to()
        for edge in self.graph.adj(nextPoint):
            self.relax(edge)

    def addNextPoint(self, point):
        for edge in self.graph.adj(point):
            self.relax(edge)

    def dijkstra(self):
        # start
        self.addNextPoint(self.start)

        while(len(self.pg) != 0):
            minEge = self.deleteMinWeight()
            # 加入下一个被选的tag
            self.addNextPointByEdge(minEge)

        self.printFinalTreeEdge()

    def printFinalTreeEdge(self):
        # print pg tree的问题

        print '最小生成🌲-----'

        for key in self.edgeTo:
            edge = self.edgeTo[key]
            if edge:
                v = edge.start()
                w = edge.to()
                print("%s  %s  %s" % (v, w, edge.getWeight()))

        print '最后的数据'
        print self.distTo

    def relax2(self, edge):
        start = edge.start()
        end = edge.to()

        if (self.distTo[end] > self.distTo[start] + edge.getWeight()):
            self.distTo[end] = self.distTo[start] + edge.getWeight()
            self.edgeTo[end] = edge

    def relax3(self, edge):
        start = edge.start()
        end = edge.to()

        if (self.distTo[end] > self.distTo[start] + edge.getWeight()):
            self.distTo[end] = self.distTo[start] + edge.getWeight()
            # 找到的一个条件是如果是同一条边，而且值越来越小，那就说明有环
            if (self.edgeTo[end] and self.edgeTo[end] == edge):
                print '有负权重环'
                self.hasNegativeCircle = True
                return

            self.edgeTo[end] = edge

            if (end not in self.quene):
                self.quene.append(end)
    # 获取最短路径的第二种写法

    def minPathSecond(self):
        topoOrder = self.graph.topoLogical()

        print '当前这颗树的反向排序是'
        topoOrder.reverse()
        print topoOrder

        for p in topoOrder:
            print 'hahah%s', p
            edges = self.graph.adj(p)
            print 'edgs%s', edges
            if (edges == None):
                continue
            for edge in edges:
                self.relax2(edge)

        print self.edgeTo
        print self.printFinalTreeEdge()

    def bellmanFord(self):
        self.quene.append(self.start)
        self.onQ[self.start] = True

        while(len(self.quene) != 0 and not self.hasNegativeCircle):
            nextPoint = self.quene.pop(0)
            self.onQ[nextPoint] = False

            for edge in self.graph.adj(nextPoint):
                other = edge.to()
                self.relax2(edge)
                if (not self.onQ[other]):
                    self.quene.append(other)
                    self.onQ[other] = True

        print '另外一种方法对于有向换来说---'
        self.printFinalTreeEdge()

    # 我写的最短路径的防范
    # 如果dis[s]< dist[t] + weight， 那没有必要再讲s加入队列中
    # 因为1.dist[s] 小，说明已经遍历过了。那么已s开头的其他重点路径已经是最小的，没必要再比较一遍
    def standardBellmanFord(self):
        self.quene.append(self.start)

        while(len(self.quene) != 0):
            nextPoint = self.quene.pop(0)
            for edge in self.graph.adj(nextPoint):
                self.relax3(edge)

        print '另外一种方法对于有向换来说---'
        self.printFinalTreeEdge()

    # 套汇问题，其实就是识别负权重环的问题
    # def arbitrage(self):


if __name__ == "__main__":
    digraph = DEdgeWeightGraph(8, 15)
    # digraph.addEdge(4, 5, 0.35)
    # digraph.addEdge(5, 4, 0.35)
    # digraph.addEdge(4, 7, 0.37)
    # digraph.addEdge(5, 7, 0.28)
    # digraph.addEdge(7, 5, 0.28)
    # digraph.addEdge(5, 1, 0.32)
    # digraph.addEdge(5, 1, 0.32)
    # digraph.addEdge(0, 4, 0.38)
    # digraph.addEdge(0, 2, 0.26)
    # digraph.addEdge(7, 3, 0.39)
    # digraph.addEdge(1, 3, 0.29)
    # digraph.addEdge(2, 7, 0.34)
    # digraph.addEdge(6, 2, 0.4)
    # digraph.addEdge(3, 6, 0.52)
    # digraph.addEdge(6, 0, 0.58)
    # digraph.addEdge(6, 4, 0.93)

    digraph.addEdge(4, 5, 0.35)
    # digraph.addEdge(5, 4, 0.35)
    digraph.addEdge(4, 5, -0.4)
    digraph.addEdge(4, 7, 0.37)
    digraph.addEdge(5, 7, 0.28)
    digraph.addEdge(7, 5, 0.28)
    digraph.addEdge(5, 1, 0.32)
    digraph.addEdge(0, 4, 0.38)
    digraph.addEdge(0, 2, 0.26)
    digraph.addEdge(7, 3, 0.39)
    digraph.addEdge(1, 3, 0.29)
    digraph.addEdge(2, 7, 0.34)
    digraph.addEdge(6, 2, -1.2)
    digraph.addEdge(3, 6, 0.52)
    digraph.addEdge(6, 0, -1.4)
    digraph.addEdge(6, 4, -1.25)

    # digraph = DEdgeWeightGraph(8, 13)
    # digraph.addEdge(5, 4, 0.35)
    # digraph.addEdge(4, 7, 0.37)
    # digraph.addEdge(5, 7, 0.28)
    # digraph.addEdge(5, 1, 0.32)
    # digraph.addEdge(4, 0, 0.38)
    # digraph.addEdge(0, 2, 0.26)
    # digraph.addEdge(3, 7, 0.39)
    # digraph.addEdge(1, 3, 0.29)
    # digraph.addEdge(7, 2, 0.34)
    # digraph.addEdge(6, 2, 0.4)
    # digraph.addEdge(3, 6, 0.52)
    # digraph.addEdge(6, 0, 0.58)
    # digraph.addEdge(6, 4, 0.93)

    dmin = DMinPath(digraph, 0)
    # dmin.dijkstra()
    # dmin.bellmanFord()
    dmin.standardBellmanFord()
    # dmin.minPathSecond()
