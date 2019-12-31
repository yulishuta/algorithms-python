#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开房间钥匙


class Solution(object):
    def initGraph(self, rooms):
        vetex = {}
        for (idx, data) in enumerate(rooms):
            vetex[idx] = filter(lambda x: x != idx, data)

        return vetex

    def dfs(self, vetex, counts, start):
        counts[start] = 1
        if (len(vetex[start]) == 0):
            return

        for to in vetex[start]:
            if counts[to] == 0:
                self.dfs(vetex, counts, to)

    def initCount(self, rooms):
        length = len(rooms)

        return [0 for i in range(length)]

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        ids = self.initCount(rooms)
        vetex = self.initGraph(rooms)

        self.dfs(vetex, ids, 0)

        travelCounts = 0
        for i in ids:
            if i == 0:
                travelCounts = travelCounts + 1
        return travelCounts == 0


if __name__ == "__main__":
    grid = [[1, 3], [3, 0, 1], [2], [0]]
    solution = Solution()

    print solution.canVisitAllRooms(grid)
