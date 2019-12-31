#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 颜色交替的最短路径v2

#这个代码被我毁坏了。采用一个新的代码

import time
from collections import deque
RED = 0
BLUE = 1
INIT_COLOR = -1


class Solution(object):
    def initEdge(self, arr, color, vetex, traveled):
        for edge in arr:
            start = edge[0]
            end = edge[1]

            # 子环放在最后面
            vetex[start].append((start, end, color))
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
        currentUnique = [self.getUniqueKey(originEdge) for originEdge in pg ]
        return edgeUniqueKey in currentUnique

    def handleInitStart(self,graph,pg):
        #对于初始的点，策略是这样的
        #自环最后加入，某个终点只加一个点

        pg.append((0, 0 ,RED))
        pg.append((0, 0 ,BLUE))

    def dfs(self, graph, dist, travel, pg, colorMap,tempDist):
        
        self.handleInitStart(graph, pg)
        n= 1
        while(len(pg)):
            nextEdge = pg.popleft()
            (originStart, nextStep, startColor) = nextEdge
            

            originEdgeUniqueKey = self.getUniqueKey(nextEdge)
            travel[originEdgeUniqueKey] = True
            (originStart, originTo, color) = nextEdge
            #自环算长度吗？
            n = 0 if originStart == originTo else 1
            tempDist[originTo] =  tempDist[originStart] + n
            
            dist[originTo] = min(dist[originTo],tempDist[originTo])

            colorMap[originTo] = color

            for edge in graph[originTo]:
                (start, to, nextColor) = edge
                edgeUniqueKey = self.getUniqueKey((start, to, nextColor))

                if not travel[edgeUniqueKey]:
                    if nextColor != colorMap[start] and not self.ifInStack(pg, edgeUniqueKey) :
                        pg.append(edge)


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
        colors = [-1 for i in range(n)]
        pg = deque()
        dist[0] = 0
        tempDist = [float('inf') for i in range(n)]
        tempDist[0]  = 0

        print(graph)
        self.dfs(graph, dist, travel, pg, colors,tempDist)
        return self.getFinalResult(n, dist)


if __name__ == "__main__":
    startTime = time.time()
    n = 5

    red_edges = [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]
    blue_edges = [[1,3],[0,0],[0,3],[4,2],[1,0]]

    # red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    # blue_edges = [[1, 2], [2, 3], [3, 1]]

    solution = Solution()
    print(solution.shortestAlternatingPaths(n, red_edges, blue_edges))
    # print(solution.findMinHeightTrees(909, grid))

    print('执行时间---%d', time.time() - startTime)
