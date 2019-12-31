class WeightEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, vertex):
        if vertex == self.w:
            return self.v
        else:
            return self.w

    def getWeight(self):
        return self.weight

    def compareTo(self, that):
        if (that.weight() > self.weight()):
            return -1
        elif(self.weight > that.weight()):
            return 1
        else:
            return 0
