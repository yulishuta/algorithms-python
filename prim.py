#!/usr/bin/python
# -*- coding: UTF-8 -*-

from edgeWeightGraph import EdgeWeightGraph


class Prim:
    def __init__(self, n, weightGraph):
        self.graph = weightGraph
        node = range(0, n)
        self.marked = dict.fromkeys(node, False)
        self.finalTreeEdge = []
        self.minPg = []

        self.finalTreeEdge = []
        self.edgeTo = dict.fromkeys(node, None)  # 存储顶点到树的最小边
        self.distTo = {}  # 存储权重
        self.sortedEdge = []

    def filterValidateEdge(self, edge):
        v = edge.either()
        w = edge.other(v)

        return not(self.marked[v] and self.marked[w])

    def clearMinPg(self, removeIndexs):
        newMinPg = []
        for idx, val in enumerate(self.minPg):
            if idx not in removeIndexs:
                newMinPg.append(self.minPg[idx])
        self.minPg = newMinPg

    def startGetTree(self):
        # 从minpg中找到第一个不在marked列表中的顶点。
        nextPoint = None
        nextEdge = None
        removeIndexs = []
        # 对minpg进行排序
        # 为什么算法书上的代码就这么清晰
        # 1.每次从pg中删除最小边，如果该边的两个顶点都已标记过
        # 那就跳过此处循环；如果没有将边加入最小生成树，并将未标记过
        # 2.的顶点的边加入横切边的list中，
        # 我反省了一下，不需要用什么递归啊？
        self.minPg = sorted(self.minPg, key=lambda x: x.weight)
        print '-----start------'
        self.printMinPgTree()
        for index, edge in enumerate(self.minPg):
            v = edge.either()
            w = edge.other(v)
            if (self.marked[v] and self.marked[w]):
                removeIndexs.append(index)
            else:
                if (self.marked[v] and not self.marked[w]):
                    nextPoint = w
                    nextEdge = edge
                    removeIndexs.append(index)
                    break

                if (self.marked[w] and not self.marked[v]):
                    nextPoint = v
                    nextEdge = edge
                    removeIndexs.append(index)
                    break
        if (nextPoint == None or nextEdge == None):
            return

        # 设置该顶点加入树中，设置包含改顶点的边加入最小生成树中。同时在将改边再minpg中去掉
        self.marked[nextPoint] = True
        self.finalTreeEdge.append(nextEdge)
        self.clearMinPg(removeIndexs)

        print '过滤以后的minPg=--'
        print self.printMinPgTree()

        # 获取剩下的有效边
        theEdgesOfNext = self.graph.adj(nextPoint)
        theRestEdge = filter(self.filterValidateEdge, theEdgesOfNext)
        # 获取它的最小边，边的另外一个顶点不能再marked中
        if(len(theRestEdge) == 0):
            return
        self.minPg.extend(theRestEdge)

        # 重复上诉过程
        self.startGetTree()

    def start(self):
        for point in self.graph.getPoints():
            if(not self.marked[point]):
                print point
                self.marked[point] = True
                allEdges = self.graph.adj(point)
                newAllEdges = sorted(
                    allEdges, key=lambda x: x.weight)
                self.minPg.extend(newAllEdges)
                self.startGetTree()

    def findFirstValidatePoint(self):
        newDistList = sorted(self.distTo.items(), key=lambda d: d[1])
        for newTuple in newDistList:
            s = newTuple[0]
            theEdge = self.edgeTo[s]
            w = theEdge.other(s)
            if self.marked[s] and self.marked[w]:
                continue

            return s
        return None
    # 最小生成树第2个版本v2

    def prim2v2(self):
        self.visit2(0)
        while(True):
            nextPointKey = self.findFirstValidatePoint()
            if (nextPointKey == None):
                break
            theEdge = self.edgeTo[nextPointKey]
            self.finalTreeEdge.append(theEdge)
            otherPoint = theEdge.other(nextPointKey)
            nextPoint = nextPointKey if not self.marked[nextPointKey] else otherPoint

            self.visit2(nextPoint)

    # 最小生成树的第2个版本
    def prim2(self):

        self.visit2(0)

        nextPointKey = self.findFirstValidatePoint()

        if (nextPointKey == None):
            return
        theEdge = self.edgeTo[nextPointKey]
        self.finalTreeEdge.append(theEdge)
        otherPoint = theEdge.other(nextPointKey)
        nextPoint = nextPointKey if not self.marked[nextPointKey] else otherPoint

        self.visit2(nextPoint)
        self.prim2()  # 如果递归用在最后面说明不需要递归

    def visit2(self, s):
        self.marked[s] = True
        for edge in self.graph.adj(s):
            w = edge.other(s)
            if not self.marked[w]:
                if self.edgeTo[w]:
                    if self.distTo[w] > edge.getWeight():
                        self.edgeTo[w] = edge
                        self.distTo[w] = edge.getWeight()
                else:
                    self.edgeTo[w] = edge
                    self.distTo[w] = edge.getWeight()

    def getSortedEdges(self):
        for s in self.graph.getPoints():
            if not self.marked[s]:
                edges = self.graph.adj(s)
                for edge in edges:
                    v = edge.either()
                    w = edge.other(v)
                    if not self.marked[v] and not self.marked[w]:
                        self.sortedEdge.append(edge)
                self.marked[s] = True

        # 对self.sortedEdge 排序
        self.sortedEdge = sorted(self.sortedEdge, key=lambda x: x.weight)

    def kruskal(self):
        # 将边按照大小顺序排序
        self.getSortedEdges()

        # 识别该边是否是环
        for edge in self.sortedEdge:

    def printMinPgTree(self):
        for edge in self.minPg:
            v = edge.either()
            w = edge.other(v)
            print("%s  %s  %s" % (v, w, edge.getWeight()))

    def printFinalTreeEdge(self):
        # print pg tree的问题
        for edge in self.finalTreeEdge:
            v = edge.either()
            w = edge.other(v)
            print("%s  %s  %s" % (v, w, edge.getWeight()))


if __name__ == "__main__":
    digraph = EdgeWeightGraph()
    digraph.addEdge(4, 5, 0.35)
    digraph.addEdge(4, 7, 0.37)
    digraph.addEdge(5, 7, 0.28)
    digraph.addEdge(0, 7, 0.16)
    digraph.addEdge(1, 5, 0.32)
    digraph.addEdge(0, 4, 0.38)
    digraph.addEdge(2, 3, 0.17)
    digraph.addEdge(1, 7, 0.19)
    digraph.addEdge(0, 2, 0.26)
    digraph.addEdge(1, 3, 0.29)
    digraph.addEdge(2, 7, 0.34)
    digraph.addEdge(6, 2, 0.4)
    digraph.addEdge(3, 6, 0.52)
    digraph.addEdge(6, 0, 0.58)
    digraph.addEdge(6, 4, 0.93)

    prim = Prim(8, digraph)
    # print '开始获取最小生成树'
    # prim.start()
    prim.prim2v2()

    print '开始打印最小生成树'
    prim.printFinalTreeEdge()
