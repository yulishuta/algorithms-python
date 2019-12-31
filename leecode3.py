#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 判断一颗树是否是平衡二叉树


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SearchTree(object):
    def __init__(self, centerArr):
        self.nextNodes = []
        self.allValues = centerArr
        self.root = None

    def item2ValidateBST(self, root, postOrder):
        if root is None:
            return True

        leftResult = self.item2ValidateBST(root.left, postOrder)
        if len(postOrder) != 0:
            lastVal = postOrder.pop()
            if lastVal >= root.val:
                return False

        postOrder.append(root.val)
        rightResult = self.item2ValidateBST(root.right, postOrder)

        return leftResult and rightResult

    def itemValidateBST(self, root, postOrder):
        # 前序遍历，是否从小到大

        if root is None:
            return

        self.itemValidateBST(root.left, postOrder)
        postOrder.append(root.val)
        self.itemValidateBST(root.right, postOrder)

    def isValidBST(self, root):
        postOrder = []
        self.itemValidateBST(root, postOrder)

        # 判断postOrder 是否从小到大
        result = True
        length = len(postOrder)
        print postOrder
        for idx, val in enumerate(postOrder):
            if idx+1 >= length:
                break
            if postOrder[idx] >= postOrder[idx+1]:
                result = False
                break

        return result

    def isValidBST2(self, root):
        postOrder = []
        return self.item2ValidateBST(root, postOrder)

    def startBuildTree(self):
        if (len(self.allValues) == 0):
            return

        currentVal = self.allValues.pop(0)
        node = TreeNode(currentVal)

        if (len(self.nextNodes) != 0):
            beAddNode = self.nextNodes[0]

            if (beAddNode.left is None):
                beAddNode.left = node
            elif (beAddNode.right is None):
                beAddNode.right = node
                # 将这个颗node删掉
                self.nextNodes.pop(0)

        else:
            # 初始化的时候
            self.root = node

        # 值为null的不加入nextNodes中
        if not (currentVal is None):
            self.nextNodes.append(node)

        self.startBuildTree()


if __name__ == "__main__":
    myList = [10, 5, 15, None, None, 6, 20]
    # myList = [2, 1, 3]
    tree = SearchTree(myList)
    tree.startBuildTree()
    root = tree.root

    print tree.isValidBST2(root)


# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         tree = SearchTree()
