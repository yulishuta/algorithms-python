class DigraphOrder:
    def __init__(self, n, graph):
        node = range(1, n+1)
        self.marked = dict.fromkeys(node, False)
        self.prePost = []
        self.post = []
        self.reversePost = []
        self.graph = graph

        self.travel()

    def dfs(self, p):
        self.marked[p] = True

        self.prePost.append(p)
        for e in self.graph.adj(p):
            if not self.marked[e]:
                self.dfs(e)
        self.post.append(p)

    def travel(self):
        for p in self.graph.getPoints():
            if not self.marked[p]:
                self.dfs(p)

    def getPrePostOrder(self):
        return self.prePost

    def getPostOrder(self):
        return self.post

    def getReversePostOrder(self):
        print 'self..post'
        print self.post[::-1]
        return self.post[::-1]
