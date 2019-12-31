#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 参与通信服务器
# 图的连通数目

import time
from collections import defaultdict, deque


class Solution(object):
    def getResult(self, ids):
        finalResult = 0

        for num in ids:
            finalResult = finalResult + 1

        return finalResult

    def printsz(self, sz):
        result = {}

        for key in sz:
            if sz[key] >= 1:
                result[key] = sz[key]

        # print(result)

    def startUnion(self, grid, m, n):
        ids = {}

        # 先合并行(这里可以优化)
        for i in range(0, n):
            preNum = -1
            for j in range(0, m):
                if grid[i][j] == 1:
                    num = i*m + j
                    # 和前面的union
                    if preNum != -1:
                        ids[preNum] = True
                        ids[num] = True
                    preNum = num

        # 再合并列
        for j in range(0, m):
            preNum = -1
            for i in range(0, n):
                if grid[i][j] == 1:
                    num = i*m + j
                    if preNum != -1:
                        ids[preNum] = True
                        ids[num] = True
                    preNum = num

        return ids

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
    # equations = [[1, 0], [0, 1]]
    equations = [[1,0,0,0,0,0],[0,0,1,1,1,1],[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,1]]
    solution = Solution()
    print(solution.countServers(equations))
