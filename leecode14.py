#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 无向有环图的冗余链接

import time

from collections import deque


class Solution(object):
    def initGraph(self, edges, n, priority):
        vetex = {i: deque() for i in range(1, n+1)}
        idx = 0
        for edge in edges:
            one = edge[0]
            other = edge[1]
            vetex[one].append(other)
            vetex[other].append(one)

            key = str(one) + str(other)
            priority[key] = idx
            idx = idx+1

        return vetex

    def filterTheEdge(self, stack, to, priority):
        finalEdges = []

        length = len(stack)

        keyPoints = []
        order = -1
        result = []

        startIdx = stack.index(to)
        for i in range(startIdx, length-1):
            pre = stack[i]
            nextPoint = stack[i+1]
            keyPoints = [pre, nextPoint]

            if pre > nextPoint:
                keyPoints = [nextPoint, pre]

            priorityKey = "".join([str(i) for i in keyPoints])
            if priority[priorityKey] > order:
                order = priority[priorityKey]
                result = keyPoints

        return result

    def dfs(self, vetex, start, parent, marked, stack, priority):
        marked[start] = True
        stack.append(start)
        for to in vetex[start]:
            if not marked[to]:
                result = self.dfs(vetex, to, start, marked, stack, priority)
                if result:
                    return result
            else:
                if to != parent:
                    # 如果有环，会来判断最后给的边是哪个？
                    stack.append(to)
                    return self.filterTheEdge(stack, to, priority)

        stack.pop()

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        start = edges[0][0]
        n = len(edges)
        marked = dict.fromkeys(range(1, n+1), False)

        priority = {}
        for edge in edges:
            key = "".join(str(i) for i in edge)
            priority[key] = -1

        vetex = self.initGraph(edges, n, priority)

        stack = []

        return self.dfs(vetex, start, start, marked, stack, priority)


if __name__ == "__main__":
    startTime = time.time()
    # grid = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    # grid = [[1, 2], [1, 3], [2, 3]]
    grid = [[30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],[44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],[6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],[19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],[31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]
    solution = Solution()
    print(solution.findRedundantConnection(grid))
    # print(solution.findMinHeightTrees(909, grid))

    print('执行时间---%d', time.time() - startTime)
