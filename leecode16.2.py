#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 颜色交替的最短路径v2-- 深度优先遍历

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
            if start == end:
                vetex[start].append((start, end, color))
            else:
                vetex[start].appendleft((start, end, color))
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

    def isColorRight(self, startColor, edgeColor):
        if startColor == INIT_COLOR:
            return True
        else:
            return True if startColor != edgeColor else False

    def handleInitStart(self,graph,start):
        #对于初始的点，策略是这样的： 自环最后加入，平行边选择一个加入
        #对于其它点： 自环最后加入

        hasAddTos = deque()
        result = deque()
        for edge in graph[start]:
            (start, to, nextColor) = edge
            if start != to:
                if start  == 0:
                    if to not in hasAddTos:
                        result.append(edge)
                        hasAddTos.append(to)
                else:
                    result.append(edge)

        #当且仅仅只有自环时，才将自环加入pg中
        if len(result) == 0:
            for edge in graph[start]:
                result.append(edge)
        return result


    def dfs(self, graph, dist, travel,stack, start,startColor,n=1):
        edges = self.handleInitStart(graph, start)
        if start not in stack:
            stack.append(start)
        for edge in edges:
            originEdgeUniqueKey = self.getUniqueKey(edge)
            (originStart, originTo, tocolor) = edge
            if self.isColorRight(startColor,tocolor) and not travel[originEdgeUniqueKey]:
                travel[originEdgeUniqueKey] = True

                if originTo in stack:
                    n = n+1
                if dist[originTo] > dist[originStart] + n:
                    dist[originTo] = dist[originStart] + n

                self.dfs(graph, dist, travel,stack, originTo,tocolor,n)
        if len(stack) !=0:
            stack.popleft()



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
        stack = deque()

        print(graph)
        self.dfs(graph, dist, travel,stack, 0,INIT_COLOR,1)
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
