import './graph'

class SymbolGraph: 
    def __init__(self):
        self.st = {}
        self.keys = []
        self.graph = Graph

    def get_ST(self, printIn):
        pointList = printIn.split(' ')
        if len(pointList) ==2:
            pointA = pointList[0]
            pointB = pointList[1]

            currentSTlen = len(self.st)

            if pointA not in self.st:
                self.st[pointA] = currentSTlen + 1
                self.keys.push(pointA)

            if pointB not in self.st:
                self.st[pointB]= currentSTlen + 1
                self.keys.push(pointB)

    def get_Graph(self):
        #从map中获取graph

    