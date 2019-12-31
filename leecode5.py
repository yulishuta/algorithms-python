#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安排飞机行程


class Solution(object):
    def initGraph(self, tickets):
        vertex = {}
        for path in tickets:
            start = path[0]
            end = path[1]
            if start in vertex:
                vertex[start].append(end)
            else:
                vertex[start] = [end]

            if end not in vertex:
                vertex[end] = []

        # 对每一个vertex按从小到大排序
        for start in vertex:
            toList = vertex[start]
            toList.sort()
            vertex[start] = toList

        return vertex

    def dfs(self, vertex, start, result):
        if (len(vertex[start]) == 0):
            result.append(start)
            return
        while (len(vertex[start])):
            nextPoint = vertex[start].pop(0)
            self.dfs(vertex, nextPoint, result)

        result.append(start)

        return

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        startAirPort = 'JFK'
        vertex = self.initGraph(tickets)
        result = []

        self.dfs(vertex, startAirPort, result)

        result.reverse()
        return result


if __name__ == "__main__":
    grid = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    solution = Solution()

    print solution.findItinerary(grid)
