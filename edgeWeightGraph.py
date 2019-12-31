from weightEdge import WeightEdge


class EdgeWeightGraph:
    def __init__(self):
        self.vertex = {}
        self.edges = []

    def addEdge(self, v, w, weight):
        edge = WeightEdge(v, w, weight)
        v1 = edge.either()
        v2 = edge.other(v1)
        self.edges.append(edge)
        if v1 in self.vertex:
            self.vertex[v1].append(edge)
        else:
            self.vertex[v1] = [edge]

        if v2 in self.vertex:
            self.vertex[v2].append(edge)
        else:
            self.vertex[v2] = [edge]

    def adj(self, v):
        return self.vertex[v]

    def edges(self):
        return self.edges

    # 这种以边为核心的图，不会有获得顶点的操作。。
    def getPoints(self):
        return self.vertex.keys()
