#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 树的遍历

# 二叉树的垂序遍历
import time
from collections import defaultdict, deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isEmptyNode(self, node):
        return node.left == None or node.right == None

    def insertNode(self, node, root):
        if root == None:
            return node

        if root.left == None:
            root.left = node
        elif root.right == None:
            root.right = node
        else:
            if self.isEmptyNode(root.left):
                self.insertNode(node, root.left)
            else:
                self.insertNode(node, root.right)

        return root

    def initTree(self, initData):
        # 初始化树
        root = None
        for val in initData:
            node = TreeNode(val)
            root = self.insertNode(node, root)

        return root

    def travel(self, root, x, y, xMap):
        if (root == None):
            return

        if root.val != None:
            xMap[x].append((root.val, y))
        self.travel(root.left, x-1, y-1, xMap)
        self.travel(root.right, x+1, y-1, xMap)

    def getResult(self, xMap):
        result = []

        print(xMap)
        result = sorted(xMap.items(), key=lambda d: d[0])

        finalResult = []

        for x, valList in result:
            valList = sorted(valList, key=lambda val: (-val[1], val[0]))
            finalResult.append([val for (val, y) in valList])

        return finalResult

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        startTime = time.time()
        xMap = defaultdict(deque)
        self.travel(root, 0, 0, xMap)

        result = self.getResult(xMap)
        print(time.time() - startTime)
        return result


if __name__ == "__main__":
    equations = [0, 8, 1, None, None, 3, 9, None, 4, 5, None, None, 7, 6]

    solution = Solution()
    tree = solution.initTree(equations)
    print(solution.verticalTraversal(tree))
