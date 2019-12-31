#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 判断一个图是否是有环


class DWeightEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def start(self):
        return self.v

    def to(self):
        return self.w

    def getWeight(self):
        return self.weight


class Graph(object):
    def __init__(self, p,  points):
        self.p = p
        self.e = len(points)
        node = range(0, p)
        self.edges = dict.fromkeys(node, None)
        self.marked = dict.fromkeys(node, False)
        self.stacked = dict.fromkeys(node, False)
        self.hasCircle = False

        for q in points:
            if len(q) == 2:
                ekey = q[0]
                if self.edges[ekey]:
                    self.edges[ekey].append(q[1])
                else:
                    self.edges[ekey] = [q[1]]

    def dfs(self, v):
        self.marked[v] = True
        self.stacked[v] = True

        if self.edges[v] == None:
            self.stacked[v] = False
            return
        for p in self.edges[v]:
            if (not self.marked[p]):
                self.dfs(p)
            else:
                if self.stacked[p]:
                    self.hasCircle = True
                    return

        self.stacked[v] = False

    def isHasCircyle(self):
        for p in self.edges:
            if not self.marked[p]:
                self.dfs(p)

        return self.hasCircle


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    graph = Graph(numCourses, prerequisites)
    graph.isHasCircyle()
    print graph.hasCircle
