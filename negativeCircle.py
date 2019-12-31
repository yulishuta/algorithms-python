#!/usr/bin/python
# -*- coding: UTF-8 -*-

from dGraph import DEdgeWeightGraph
import sys


class NegativeCircle:
    def __init__(self, graph):
        self.graph = graph
        n = graph.v

        node = range(0, n)

        self.marked = dict.fromkeys(node, False)
        self.stacked = dict.fromkeys(node, False)
        self.edges = []
        self.result = []
        self.path = dict.fromkeys(node, None)

    def start(self, point):

        self.marked[point] = True
        self.stacked[point] = True
        for edge in self.graph.adj(point):
            to = edge.to()
            self.path[point] = edge

            if not self.marked[to]:
                self.start(to)
            else:
                # circle的其他用法
                if self.stacked[to]:
                    # 判断是否为负权重
                    sumCount = 0

                    startIndex = -1
                    loopEdge = self.path[to]
                    while(loopEdge and loopEdge.to() != to):
                        sumCount = sumCount + loopEdge.getWeight()
                        self.result.append(loopEdge)

                        loopEdge = self.path[loopEdge.to()]

                    if (loopEdge.to() == to):
                        sumCount = sumCount + loopEdge.getWeight()
                        self.result.append(loopEdge)
                        if sumCount < 0:
                            print '找到负权重环'

                            self.printFinalTreeEdge(self.result)
                    else:
                        self.result = []

        self.stacked[point] = False

    def printFinalTreeEdge(self, edgeTo):
        # print pg tree的问题

        print '最小生成🌲-----'

        for edge in edgeTo:
            if edge:
                v = edge.start()
                w = edge.to()
                print("%s  %s  %s" % (v, w, edge.getWeight()))


if __name__ == "__main__":
    digraph = DEdgeWeightGraph(8, 15)

    digraph.addEdge(4, 5, 0.35)
    digraph.addEdge(5, 4, -0.4)
    digraph.addEdge(4, 7, 0.37)
    digraph.addEdge(5, 7, 0.28)
    digraph.addEdge(7, 5, -0.37)
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

    dCircle = NegativeCircle(digraph)
    dCircle.start(0)
