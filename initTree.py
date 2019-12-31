#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 初始化二叉树
import time
from collections import defaultdict, deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class InitTree(object):
    def isEmptyNode(self, node):
        return node.val == None or node.left == None or node.right == None

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
