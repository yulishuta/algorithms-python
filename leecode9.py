class Solution(object):
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        node = range(len(graph))
        color = [0 for i in node]

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True

        return filter(dfs, range(len(graph)))


if __name__ == "__main__":
    grid = [[0], [2, 3, 4], [3, 4], [0, 4], []]
    solution = Solution()

    print solution.eventualSafeNodes(grid)
