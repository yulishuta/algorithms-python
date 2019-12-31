#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 二叉树的--求根到叶子节点的数字之和
import time
from collections import defaultdict, deque
from initTree import InitTree

# pathInfo={maxDeep:4, pathList: [a,b,c]}


class Solution(object):

    def getMinChildTreeRoot(self, pathInfo):
        pathList = pathInfo['pathList']

        if not len(pathList):
            return None

        lastIndex = len(pathList[0])

        while(lastIndex != -1):
            lastIndex = lastIndex - 1
            currentNode = pathList[0][lastIndex]
            isAllSame = True
            for pathItem in pathList:
                if pathItem[lastIndex].val != currentNode.val:
                    isAllSame = False
                    continue

            if isAllSame:
                break

        if lastIndex == -1:
            return None
        else:
            return pathItem[lastIndex]

    def travel(self, root, deep, pathList, pathInfo):
        if root == None or root.val == None:
            return
        deep = deep+1
        pathList.append(root)

        if root.left == None or root.right == None:
            if pathInfo['maxDeep'] < deep:
                pathInfo['maxDeep'] = deep
                pathInfo['pathList'] = [deque(pathList)]
            elif pathInfo['maxDeep'] == deep:
                pathInfo['pathList'].append(deque(pathList))

        # self.printPathInfo(pathInfo)
        self.travel(root.left, deep, pathList, pathInfo)
        self.travel(root.right, deep, pathList, pathInfo)
        pathList.pop()

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        deep = 0
        pathList = deque()
        pathInfo = {
            'maxDeep': -1,
            'pathList': []
        }

        self.travel(root, deep, pathList, pathInfo)

        return self.getMinChildTreeRoot(pathInfo)

    def printPathInfo(self, pathInfo):
        print('----')
        for numList in pathInfo['pathList']:
            itemList = [item.val for item in numList]
            print(itemList)


if __name__ == "__main__":
    equations = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

    solution = Solution()
    tree = InitTree()
    root = tree.initTree(equations)
    print(solution.subtreeWithAllDeepest(root).val)
