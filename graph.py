class Graph:
    def __init__(self):
        self.vertex = {}

    def addPoint(v):
        if v in self.vertex:
            self.vertex[v].push(v)
        else:
            self.vertex[v] = []

    def addEdge(v1,  v2):
        addPoint[v1]
        addPoint(v2)

    def adj(v):
        return self.vertex[v]

    def getPoints():
        return self.vertex.keys()


# 在图中搜索和s联通的所有点
checked = {}


def dfs(G, s):
    checked[s] = True

    for v in G.adj(s):
        if (checked[v]) return
        dfs(G, v)


def isTwoNodeConnect(G, v1, v2):
    checked[v1] = True
    # if all checked return false
    result = False

    if (v1 == = v2):
        return true
    for v in G.adj(v1):
        if (not checked[v]):
            result = result or isTwoNodeConnect(G, v, v2)
            if result:
                break

    return result
