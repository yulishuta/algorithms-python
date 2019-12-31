#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 除法运算
import math


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


# 数据不一样的地方
class EdgeWeightGraph:
    def __init__(self, points, weights):
        self.vertex = {}
        self.edges = []

        for idx, point in enumerate(points):
            self.addEdge(point[0], point[1],  weights[idx])
            self.addEdge(point[1], point[0], 1/float(weights[idx]))

            # self.addEdge(point[0], point[1],  math.log(weights[idx]))
            # self.addEdge(point[1], point[0], -math.log(weights[idx]))

    def addEdge(self, v, w, weight):
        edge = DWeightEdge(v, w, weight)
        self.edges.append(edge)
        if v in self.vertex:
            self.vertex[v].append(edge)
        else:
            self.vertex[v] = [edge]

    def adj(self, v):
        return self.vertex[v]

    def edges(self):
        return self.edges

    def points(self):
        return self.vertex.keys()


class Solution(object):
    def calcResult(self, edgeList):
        sum1 = 1
        for edge in edgeList:
            sum1 = sum1 * edge.getWeight()

        return sum1

    def dfs(self, graph, start, end, calcResult, marked):
        # 对有向图进行遍历
        self.marked[start] = True
        finalResult = -1

        if start == end:
            # 如果end 和 to相等。
            return self.calcResult(calcResult)
        for edge in graph.adj(start):
            calcResult.append(edge)
            to = edge.to()

            if not self.marked[to]:
                finalResult = self.dfs(graph, to, end, calcResult, marked)

            if finalResult != -1:
                return finalResult

            calcResult.remove(edge)

        return finalResult

    def getResult(self, graph, start, end):
        calcResult = []
        points = graph.points()
        self.marked = dict.fromkeys(points, False)

        temp = self.dfs(graph, start, end, calcResult, self.marked)

        return temp

    def checkValiate(self, graph, start, end):
        allPoints = graph.points()
        if start not in allPoints or end not in allPoints:
            return -1.0

        if start == end:
            return 1

        return None

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        result = []
        graph = EdgeWeightGraph(equations, values)

        for query in queries:
            validate = self.checkValiate(graph, query[0], query[1])
            if (validate == None):
                itemResult = self.getResult(graph, query[0], query[1])
                itemResult
                result.append(itemResult)
            else:
                result.append(validate)

        return result


if __name__ == "__main__":
    solution = Solution()

    equations = [['a', 'b'], ['b', 'c']]
    values = [2, 3]
    queries = [['a', 'c'], ['c', 'a'], ['x', 'x']]

    print solution.calcEquation(equations, values, queries)
