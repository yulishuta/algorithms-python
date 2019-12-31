#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 参与通信服务器
# 图的连通数目

import time
from collections import defaultdict, deque


class Solution(object):
    def find(self, p, ids):
        while(ids[p] != p):
            p = ids[p]
        return p

    def getResult(self, sz):
        finalResult = 0

        for num in sz:
            if sz[num] > 1:
                finalResult = finalResult + sz[num]
        return finalResult

    def union(self, start, to, ids, sz):
        startRoot = self.find(start, ids)
        endRoot = self.find(to, ids)
        if startRoot == endRoot:
            return

        if sz[startRoot] > sz[endRoot]:
            ids[endRoot] = startRoot
            sz[startRoot] = sz[startRoot] + sz[endRoot]
            sz[endRoot] = 1
        else:
            ids[startRoot] = endRoot
            sz[endRoot] = sz[startRoot] + sz[endRoot]
            sz[startRoot] = 1

    def printsz(self, sz):
        result = {}

        for key in sz:
            if sz[key] >= 1:
                result[key] = sz[key]

        # print(result)

    def startUnion(self, grid, m, n):
        ids = {}
        sz = {}

        # 先合并行(这里可以优化)
        for i in range(0, n):
            preNum = -1
            for j in range(0, m):
                if grid[i][j] == 1:
                    num = i*m + j
                    ids[num] = num
                    sz[num] = 1
                    # 和前面的union
                    if preNum != -1:
                        self.union(preNum, num, ids, sz)
                    preNum = num

        self.printsz(sz)
        # 再合并列
        for j in range(0, m):
            preNum = -1
            for i in range(0, n):
                if grid[i][j] == 1:
                    num = i*m + j
                    if preNum != -1:
                        self.union(preNum, num, ids, sz)
                    preNum = num

        return sz

    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        sz = self.startUnion(grid, m, n)
        self.printsz(sz)
        return self.getResult(sz)


if __name__ == "__main__":
    startTime = time.time()
    equations = [[1, 0], [1, 1]]
    #equations = [[1,0,0,0,0,0],[0,0,1,1,1,1],[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,1]]
    solution = Solution()
    print(solution.countServers(equations))
