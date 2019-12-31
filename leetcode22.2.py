#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 二叉树最大宽度
import time
from initTree import InitTree


class Solution(object):
    # 无非比较
    def travel(self, root, x, y, coordInfo):
        # 坐标的信息
        if root == None:
            return

        if coordInfo.get(y, None) == None:
            coordInfo[y] = {
                'minX': x,
                'maxX': x
            }
        else:
            coordInfo[y]['maxX'] = x

        self.travel(root.left, 2*x, y-1, coordInfo)
        self.travel(root.right, 2*x+1, y-1, coordInfo)

    def calcResult(self, coordInfo):
        valueList = [coordInfo[key]['maxX'] -
                     coordInfo[key]['minX']+1 for key in coordInfo]

        return max(valueList)

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        coordInfo = dict()

        self.travel(root, 0, 0, coordInfo)

        return self.calcResult(coordInfo)


if __name__ == "__main__":
    equations = [1, 1, 1, 1, 1, 1, 1, None, None, None, 1, None, None,
                 None, None, 2, 2, 2, 2, 2, 2, 2, None, 2, None, None, 2, None, 2]

    solution = Solution()
    tree = InitTree()
    root = tree.initTree(equations)
    print(solution.widthOfBinaryTree(root))
