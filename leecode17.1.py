#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 等式的传递性

# 识别无向图的环，但是flag要设置正确

import time
from collections import defaultdict, deque

UNEQUAL = 0
EQUAL = 1


class Solution(object):
    def find(self, p, ids):
        while(ids[p] != p):
            p = ids[p]
        return p

    def union(self, start, to, ids, sz):
        startRoot = self.find(start, ids)
        endRoot = self.find(to, ids)

        if sz[startRoot] > sz[endRoot]:
            ids[endRoot] = startRoot
            sz[startRoot] = sz[startRoot] + sz[endRoot]
        else:
            ids[startRoot] = endRoot
            sz[endRoot] = sz[startRoot] + sz[endRoot]

    def isConnected(self, start, to, ids):
        return self.find(start, ids) == self.find(to, ids)

    def initGraph(self, equations):
        points = deque()

        equalList = deque()
        notEqualList = deque()

        for item in equations:
            start = item[0]
            color = EQUAL if item[1] == '=' else UNEQUAL
            to = item[3]

            # a!=a直接判断去掉
            points.append(start)
            points.append(to)
            if color == EQUAL:
                equalList.append((start, to))

            else:
                notEqualList.append((start, to))
        points = set(points)
        ids = defaultdict()
        sz = defaultdict()

        for p in points:
            ids[p] = p
            sz[p] = 1

        # union
        for (start, to) in equalList:
            self.union(start, to, ids, sz)

        for (start, to) in notEqualList:
            if self.isConnected(start, to, ids):
                return False
        return True

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        return self.initGraph(equations)


if __name__ == "__main__":
    startTime = time.time()
    equations = ['a==b', 'b==c', 'a==c']
    #equations =["t!=b","h!=u","l!=y","j==j","w==s","p==q","r!=t","r==i","e!=y","v==s","i!=p","h!=i","i==o","e==e","j!=h","y!=s","k==g","c==f","n==v","a==w","d==w","f!=e","v==s","w!=g","g!=s","j!=d","c!=u","y!=n","q!=j","d!=x","l==m","q!=b","r!=n","j!=o","w!=q","t!=e","a!=m","m!=j","j!=b","v!=w"]

    solution = Solution()
    print(solution.equationsPossible(equations))
