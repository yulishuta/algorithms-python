#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 等式的传递性

# 识别无向图的环，但是flag要设置正确

import time
from collections import defaultdict, deque

UNEQUAL = 0
EQUAL = 1


class Solution(object):
    def initGraph(self, equations):
        graph = defaultdict(list)
        for item in equations:
            start = item[0]
            color = EQUAL if item[1] == '=' else UNEQUAL
            to = item[3]

            # a!=a直接判断去掉
            if start == to and color == UNEQUAL:
                return None

            graph[start].append((to, color))
            graph[to].append((start, color))

        for start in graph:
            graph[start] = set(graph[start])
        return graph

    def isTheWrongCircle(self, stack, endEdge):
        # 当且仅当这个环里,仅仅有一条不等式，其他都是等式的时候
        # 返回false
        newStack = deque()
        (currentStart, currentEnd, color) = endEdge

        isAdd = False
        for (idx, edgeInfo) in enumerate(stack):
            (edgestart, edgeEnd, color) = edgeInfo
            if edgestart == currentEnd:
                isAdd = True
            if isAdd:
                newStack.append(edgeInfo)

        newStack.append(endEdge)

        print('****')
        print(stack)
        print(newStack)
        unequalLen = 0
        for edge in newStack:
            (start, currentEnd, color) = edge
            if color == UNEQUAL:
                unequalLen = unequalLen + 1

        return len(newStack) > 1 and unequalLen == 1

    def dfs(self, graph, start,anstor, stack, marked):
        
        marked[start] = True
        for endEdge in graph[start]:
            (end, color) = endEdge
            if not marked[end]:
                stack.append((start,end,color))
                result = self.dfs(graph, end,start, stack, marked)
                if not result:
                    return False
            elif end != anstor and end != start:
                stackPoints = [edge[0] for edge in stack]

                if end in stackPoints:
                    if self.isTheWrongCircle(stack, (start, end, color)):
            
                        return False

        if len(stack):
            stack.pop()
        return True

        # stack.append(edgeInfo)
        # (start, to, edgeColor) = edgeInfo
        # marked[to] = True
        # for endEdge in graph[to]:
        #     (end, color) = endEdge
        #     if not marked[end]:
        #         result = self.dfs(graph, (to, end, color), stack, marked)
        #         if not result:
        #             return False
        #     elif end != start and end != to:
        #         stackPoints = [edge[0] for edge in stack]

        #         if end in stackPoints:
        #             if self.isTheWrongCircle(stack, (to, end, color)):
        #                 return False
        # stack.pop()
        # return True

    def checkGraph(self, graph):
        for start in graph:
            edges = graph[start]
            tos = [edge[0] for edge in edges]
            checkRepeat = len(tos) != len(set(tos))
            if checkRepeat:
                return False

        return True

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        graph = self.initGraph(equations)
        if graph == None:
            return False
        marked = defaultdict(bool)

        print(graph)
        if not self.checkGraph(graph):
            return False

        for start in graph:
            print(start,':',graph[start])
            marked[start] = False

        for start in graph:
            if not marked[start]:
                stack = deque()
                result = self.dfs(graph, start,start, stack, marked)
                if not result:
                    return False
        print(marked)
        return True


if __name__ == "__main__":
    startTime = time.time()
    equations =["t!=b","h!=u","l!=y","j==j","w==s","p==q","r!=t","r==i","e!=y","v==s","i!=p","h!=i","i==o","e==e","j!=h","y!=s","k==g","c==f","n==v","a==w","d==w","f!=e","v==s","w!=g","g!=s","j!=d","c!=u","y!=n","q!=j","d!=x","l==m","q!=b","r!=n","j!=o","w!=q","t!=e","a!=m","m!=j","j!=b","v!=w"]

    solution = Solution()
    print(solution.equationsPossible(equations))
