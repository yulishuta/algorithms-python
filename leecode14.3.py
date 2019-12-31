#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 无向有环图的冗余链接 -官方解答。使用Union-find算法

import time

from collections import deque


class Solution(object):
    def findRoot(self, j, ids):
        i = j-1
        if ids[i] == i:
            return i

        while(ids[i] != i):
            i = ids[i]
        return i

    def initGraph(self, edges, n):
        ids = [i for i in range(n)]
        degree = [1 for i in range(n)]

        for edge in edges:
            one = edge[0]
            other = edge[1]

            root1 = self.findRoot(one, ids)
            root2 = self.findRoot(other, ids)

            if root1 == root2:
                return edge

            if degree[root1] > degree[root2]:
                ids[root2] = root1
                degree[root1] = degree[root1] + degree[root2]
            else:
                ids[root1] = root2
                degree[root2] = degree[root2] + degree[root1]

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)

        return self.initGraph(edges, n)


if __name__ == "__main__":
    startTime = time.time()
    grid = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    # grid = [[1, 2], [1, 3], [2, 3]]
    # grid = [[30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],[44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],[6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],[19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],[31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]
    solution = Solution()
    print(solution.findRedundantConnection(grid))
    # print(solution.findMinHeightTrees(909, grid))

    print('执行时间---%d', time.time() - startTime)
