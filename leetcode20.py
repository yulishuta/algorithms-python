#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 二叉树的--求根到叶子节点的数字之和
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

    def getValFromPath(self, preValList, leafVal):
        result = leafVal

        inc = 10
        lastIndex = len(preValList) - 1

        while(lastIndex != -1):
            result = result + preValList[lastIndex]*inc
            inc = inc * 10
            lastIndex = lastIndex - 1

        return result

    def travel(self, root, preValList):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return self.getValFromPath(preValList, root.val)

        preValList.append(root.val)
        result = self.travel(root.left, preValList)
        result = result + self.travel(root.right, preValList)
        preValList.pop()

        return result

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        preValList = deque()
        return self.travel(root, preValList)


if __name__ == "__main__":
    equations = [4, 9, 0, 5, 1]

    solution = Solution()
    tree = solution.initTree(equations)

    startTime = time.time()
    print(solution.sumNumbers(tree))
    print(time.time() - startTime)
