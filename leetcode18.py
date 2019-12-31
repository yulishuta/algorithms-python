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

        if sz[startRoot] > sz[endRoot]:
            ids[endRoot] = startRoot
            sz[startRoot] = sz[startRoot] + sz[endRoot]
        else:
            ids[startRoot] = endRoot
            sz[endRoot] = sz[startRoot] + sz[endRoot]

    def startUnion(self, coods, m,n):
        ids = defaultdict()
        sz = defaultdict()
        length = len(coods)
        # 初始化ids和szs
        for (i, j) in coods:
            num = i*m + j
            ids[num] = num
            sz[num] = 1

        # 开始合并

        for i in range(0, length-1):
            (preX, preY) = coods[i]
            (lastX, lastY) = coods[i+1]

            if preX == lastX or preY == lastY:
                preNum = preX*m + preY
                lastNum = lastX*m + lastY
                self.union(preNum, lastNum, ids, sz)
        return sz

    def getCoordinate(self, grid):
        coods = deque()

        for row_idx, row in enumerate(grid):
            for col_idx, computer in enumerate(row):
                if computer == 1:
                    coods.append((row_idx, col_idx))

        return coods

    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        coods = self.getCoordinate(grid)
        sz = self.startUnion(coods, m)
        #print(sz)
        return self.getResult(sz)


if __name__ == "__main__":
    startTime = time.time()
    equations = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

    solution = Solution()
    print(solution.countServers(equations))
