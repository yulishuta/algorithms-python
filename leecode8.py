#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安全终点--找换，按照算法书上来


class Solution(object):
    def dfs(self, graph, start, marked):

        marked[start] = 1

        for to in graph[start]:
            if marked[to] == 0:
                hasCircle = self.dfs(graph, to, marked)
                if hasCircle:
                    return True

            else:
                if marked[to] == 1:
                    return True

        marked[start] = 2

        return False

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        stack = []
        length = len(graph)
        node = range(length)
        # 0-未遍历 1-已遍历 2-安全节点
        marked = [0 for i in node]

        for (i, val) in enumerate(graph):
            if marked[i] == 0:
                self.dfs(graph, i, marked)

        result = []

        for i, val in enumerate(marked):
            if val == 2:
                result.append(i)
        return result


if __name__ == "__main__":
    grid = [[0], [2, 3, 4], [3, 4], [0, 4], []]
    solution = Solution()

    print solution.eventualSafeNodes(grid)
