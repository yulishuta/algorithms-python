#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 颜色交替的最短路径v2

# 新的正确的代码啊

import time
from collections import deque
RED = 0
BLUE = 1


class Solution(object):
    def initEdge(self, arr, color, vetex, traveled):
        for edge in arr:
            start = edge[0]
            end = edge[1]

            # 子环放在最后面
            if start == end and start == 0:
                continue
            vetex[start].append((end, color))
            uniqueKey = self.getUniqueKey((start, end, color))
            traveled[uniqueKey] = False

    def getUniqueKey(self, edge):
        (start, end, color) = edge
        return str(start) + str(end) + str(color)

    def initGraph(self, n, red_edges, blue_edges):
        vetex = {i: deque() for i in range(n)}
        travel = {}

        self.initEdge(red_edges, RED, vetex, travel)
        self.initEdge(blue_edges, BLUE, vetex, travel)

        return (vetex, travel)

    def ifInStack(self, pg, edgeUniqueKey):
        currentUnique = [self.getUniqueKey(originEdge) for originEdge in pg]
        return edgeUniqueKey in currentUnique

    def handleInitStart(self, graph, pg):
        # 对于初始的点，策略是这样的
        # 自环最后加入，某个终点只加一个点

        pg.append((0, 0, RED))
        pg.append((0, 0, BLUE))

    def isColorMatch(self, startColor, toColor):
        return startColor != toColor

    def dfs(self, graph, dist, travel, pg):
        self.handleInitStart(graph, pg)
        while(len(pg)):
            nextEdge = pg.popleft()
            (originStart, step, startColor) = nextEdge
            print(pg)
            print(nextEdge)
            dist[originStart] = min(dist[originStart], step)

            for edge in graph[originStart]:
                (to, nextColor) = edge
                edgeUniqueKey = self.getUniqueKey((originStart, to, nextColor))

                if self.isColorMatch(startColor, nextColor):
                    if not travel[edgeUniqueKey]:
                        travel[edgeUniqueKey] = True
                        pg.append((to, step+1, nextColor))

                        # if not self.ifInStack(pg, edgeUniqueKey):
                        #     pg.append((to, step+1, nextColor))

    def getFinalResult(self, n, dist):
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        dist = [float('inf') for i in range(n)]
        (graph, travel) = self.initGraph(n, red_edges, blue_edges)
        pg = deque()
        dist[0] = 0

        
        self.dfs(graph, dist, travel, pg)
        print(travel)
        return self.getFinalResult(n, dist)


if __name__ == "__main__":
    startTime = time.time()
    # n = 5

    # # red_edges = [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]
    # # blue_edges = [[1,3],[0,0],[0,3],[4,2],[1,0]]

    # red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    # blue_edges = [[1, 2], [2, 3], [3, 1]]

    n=7
    red_edges=[[0,5],[3,1],[3,6],[1,0],[1,4],[1,2],[5,6],[5,0],[0,6],[0,3],[5,4],[6,1],[5,5],[1,1],[4,6],[2,2]]
    blue_edges=[[3,1],[4,3],[5,4],[5,3],[5,1],[3,2],[4,4],[5,0],[1,2],[1,1],[4,5],[0,0]]

    solution = Solution()
    print(solution.shortestAlternatingPaths(n, red_edges, blue_edges))
    # print(solution.findMinHeightTrees(909, grid))

    print('执行时间---%d', time.time() - startTime)
