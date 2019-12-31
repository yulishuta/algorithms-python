#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Digraph:
    def __init__(self):
        self.vertex = {}
        self.reverseVertex = {}
        self.edge = {}
        self.marked = {1: False, 2: False,
                       3: False, 4: False, 5: False, 6: False}

    # 深度遍历。获取edg
    def getEdge(self, s):
        self.marked[s] = True

        for w in self.adj(s):
            self.edge[w] = s
            if not self.marked[w]:
                self.getEdge(w)

    def addEdge(self, v1,  v2):
        if v1 in self.vertex:
            self.vertex[v1].append(v2)
        else:
            self.vertex[v1] = [v2]

        if v2 not in self.vertex:
            self.vertex[v2] = []

    def adj(self, v):
        return self.vertex[v]

    def getPoints(self):
        return self.vertex.keys()

    def reverse(self):
        points = self.getPoints()
        reversedGraph = Digraph()
        for p in points:
            edges = self.adj(p)
            for edge in edges:
                reversedGraph.addEdge(edge, p)

        return reversedGraph

    # 这个想法是该图有一个反向图，其实不对。反向图就是一个新的图对象
    # def reverse(self):
    #     # reverse graph
    #     for point in self.vertex:
    #         if point not in self.reverseVertex:
    #             self.reverseVertex[point] = []
    #         for otherPoint in self.vertex[point]:
    #             if otherPoint in self.reverseVertex:
    #                 self.reverseVertex[otherPoint].append(point)
    #             else:
    #                 self.reverseVertex[otherPoint] = [point]


# if __name__ == "__main__":
#     digraph = Digraph()
#     digraph.addEdge(1, 2)
#     digraph.addEdge(1, 3)
#     digraph.addEdge(2, 4)
#     digraph.addEdge(4, 3)
#     print digraph.vertex
#     print '-------我是反转的分割线-----'
#     digraph.reverse()
#     print '-------我是反转的分割线-----'
#     print digraph.reverseVertex
