#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 地图问题（陆地和海洋）


class Graph:
    def __init__(self, v):
        self.vertex = {}
        self.v = v
        node = range(v)
        self.isSea = dict.fromkeys(node, False)

    def addPoint(self, v, w, isSea):
        if v in self.vertex:
            self.vertex[v].append(w)
        else:
            self.isSea[v] = isSea
            self.vertex[v] = [w]

    def adj(self, v):
        return self.vertex[v]

    def getPoints(self):
        return self.vertex.keys()

    def checkIsSea(self, v):
        return self.isSea[v]


class Solution(object):
    def __init__(self):
        self.graph = None
        self.length = 0
        self.v = 0
        self.marked = None
        self.myQuene = []

    def initSolution(self, grid):
        self.length = len(grid)
        self.v = self.length * self.length
        node = range(self.v)
        self.marked = dict.fromkeys(node, False)

    def generateGraph(self, grid):
        length = len(grid)
        v = length * length
        graph = Graph(v)

        for i in range(v):
            x = i / length
            y = i % length
            isSea = grid[x][y] == 0
            if x+1 < length:
                graph.addPoint(i, i+length, isSea)
            if x-1 >= 0:
                graph.addPoint(i, i-length, isSea)
            if y+1 < length:
                graph.addPoint(i, i+1, isSea)
            if y-1 >= 0:
                graph.addPoint(i, i-1, isSea)
        return graph

    def getAllSeaLand(self, grid):
        length = len(grid)
        v = length * length

        seaReuslt = []

        for i in range(v):
            x = i / length
            y = i % length
            if grid[x][y] == 0:
                seaReuslt.append(i)

        return seaReuslt

    def getXY(self, i):
        result = {
            'x': i / self.length,
            'y': i % self.length
        }
        return result

    def calcPath(self, currentPoint, end):
        xy1 = self.getXY(currentPoint)
        xy2 = self.getXY(end)

        return abs(xy2['x'] - xy1['x']) + abs(xy2['y'] - xy1['y'])

    # 利用广度优先遍历，获取第一个到大陆的距离
    def getMinPathToLand(self, graph):
        if len(self.myQuene) == 0:
            return None

        start = self.myQuene.pop(0)
        self.marked[start] = True

        if not graph.checkIsSea(start):
            return start

        for v in graph.adj(start):
            # 如果是大陆开始计算距离
            if not self.marked[v]:
                if not v in self.myQuene:
                    self.myQuene.append(v)

        return self.getMinPathToLand(graph)

    def checkOnlyOneType(self, allSeaLand, grid):
        seaLandLen = len(allSeaLand)

        return seaLandLen == 0 or seaLandLen == self.v

    def initMarked(self):
        for idx in self.marked:
            self.marked[idx] = False

    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        allSeaLand = self.getAllSeaLand(grid)
        self.initSolution(grid)
        if (self.checkOnlyOneType(allSeaLand, grid)):
            return -1

        graph = self.generateGraph(grid)
        maxPath = -1
        minPoint = None

        for point in allSeaLand:
            self.initMarked()
            self.myQuene = []
            self.myQuene.append(point)
            resultPoint = self.getMinPathToLand(graph)

            if resultPoint != None:
                path = self.calcPath(point, resultPoint)
                if path > maxPath:
                    maxPath = path
                    minPoint = point
        return maxPath


if __name__ == "__main__":
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    solution = Solution()

    print solution.maxDistance(grid)
