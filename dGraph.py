#!/usr/bin/python
# -*- coding: UTF-8 -*-


from dWeightEdge import DWeightEdge


class DEdgeWeightGraph:
    def __init__(self, v, e):
        node = range(0, v)
        self.vertex = dict.fromkeys(node, None)
        self.edges = []
        self.v = v  # 顶点数
        self.e = e  # 边数
        self.topoOrder = []

    def addEdge(self, v, w, weight):
        edge = DWeightEdge(v, w, weight)
        v1 = edge.start()
        self.edges.append(edge)
        if self.vertex[v1] != None:
            self.vertex[v1].append(edge)
        else:
            self.vertex[v1] = [edge]

    def adj(self, v):
        return self.vertex[v]

    def edges(self):
        return self.edges

    # 这种以边为核心的图，不会有获得顶点的操作。。
    def getPoints(self):
        return self.vertex.keys()

    def topoMain(self, v):
        if (self.adj(v) == None):
            self.topoOrder.append(v)
            return
        for edge in self.adj(v):
            to = edge.to()
            if (to not in self.topoOrder):
                self.topoMain(to)

        self.topoOrder.append(v)

    def topoLogical(self):
        print self.vertex
        for edge in self.edges:
            start = edge.start()

            if (start not in self.topoOrder):
                self.topoMain(start)

        print 'final oreder'
        print self.topoOrder
        return self.topoOrder
