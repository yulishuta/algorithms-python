#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 颜色交替的最短路径

import time
import sys
RED = 0
BLUE = 1
INIT_COLOR = -1


class Solution(object):
    def initEdge(self, arr, color, vetex):
        for edge in arr:
            start = edge[0]
            end = edge[1]

            vetex[start].append((end, color))

    def initGraph(self, n, red_edges, blue_edges):
        vetex = {i: [] for i in range(n)}

        self.initEdge(red_edges, RED, vetex)
        self.initEdge(blue_edges, BLUE, vetex)

        return vetex

    def findMinDistPoint(self, pg, dist):
        minVal = sys.maxint
        result = -1
        for idx, point in enumerate(pg):
            (edgeLength, color) = dist[point]
            if edgeLength < minVal and color != INIT_COLOR:
                minVal = edgeLength
                result = idx

        return idx

    def calcColor(self, startColor, edgeColor):
        if startColor == INIT_COLOR:
            return edgeColor
        else:
            return edgeColor if startColor != edgeColor else INIT_COLOR

    def relax(self, start, graph, dist, pg):
        (startLength, startColor) = dist[start]

        for edge in graph[start]:
            (to, edgeColor) = edge
            (toLength, toColor) = dist[to]

            toColor = self.calcColor(startColor, edgeColor)
            if toLength > startLength + 1:
                if toColor != INIT_COLOR:
                    dist[to] = (startLength + 1, toColor)

                if to not in pg:
                    pg.append(to)

    def dfs(self, graph, dist, pg):

        while(len(pg) != 0):
            nextIdx = self.findMinDistPoint(pg, dist)
            nextPoint = pg[nextIdx]
            # 要去掉init
            pg.pop(nextIdx)

            self.relax(nextPoint, graph, dist, pg)

    def getFinalResult(self, n, dist):
        result = [0 if i == 0 else -1 for i in range(n)]

        for i in range(n):
            (length, color) = dist[i]
            if color != INIT_COLOR:
                result[i] = length

        return result

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        dist = [(n+1, INIT_COLOR) for i in range(n)]
        graph = self.initGraph(n, red_edges, blue_edges)
        pg = []
        dist[0] = (0, INIT_COLOR)
        for edge in graph[0]:
            (to, color) = edge
            dist[to] = (1, color)
            pg.append(to)

        self.dfs(graph, dist, pg)
        return self.getFinalResult(n, dist)


if __name__ == "__main__":
    startTime = time.time()
    n = 5

    red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    blue_edges = [[1, 2], [2, 3], [3, 1]]

    solution = Solution()
    print(solution.shortestAlternatingPaths(n, red_edges, blue_edges))
    # print(solution.findMinHeightTrees(909, grid))

    print('执行时间---%d', time.time() - startTime)
