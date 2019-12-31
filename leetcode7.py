#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安全终点--就是找到非环上的点(别忘记自环)


class Solution(object):
    def dfs(self, graph, start, stack, marked, circle):
        marked[start] = True
        stack.append(start)
        for to in graph[start]:
            if not marked[to]:
                self.dfs(graph, to, stack, marked, circle)
            else:
                if to in stack or circle[to]:
                    for item in stack:
                        if not circle[item]:
                            circle[item] = True

        stack.remove(start)

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        stack = []
        length = len(graph)
        node = range(length)
        marked = [False for i in node]
        circle = [False for i in node]

        for (i, val) in enumerate(graph):
            if not marked[i]:
                self.dfs(graph, i, stack, marked, circle)
        result = []
        for (idx, item) in enumerate(circle):
            if not item:
                result.append(idx)

        return result


if __name__ == "__main__":
    grid = [[0], [2, 3, 4], [3, 4], [0, 4], []]
    solution = Solution()

    print solution.eventualSafeNodes(grid)
