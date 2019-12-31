#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 网络延时时间

import sys
import time


class Solution(object):
    def initGraph(self, times, N):
        nodes = range(1, N+1)
        edges = {new_list: [] for new_list in nodes}

        for item in times:
            edges[item[0]].append(item)
        return edges

    def hasInPg(self, beAddEdge, queue):
        for edge in queue:
            if edge.isSame(beAddEdge):
                return True
        return False

    def relax(self, graph, start, queue, distTo):
        for edge in graph[start]:
            to = edge[1]
            weight = edge[2] 
            if distTo[to] > distTo[start] + weight:
                distTo[to] = distTo[start] + weight

                
    def foundMinIndex(self, queue,distTo):
        minEdge = sys.maxint
        minIdx = -1

        for (idx,to) in enumerate(queue):

            if distTo[to]< minEdge:
                minEdge = distTo[to]
                minIdx = idx

        return minIdx


    def dfs(self, graphEdges, queue, distTo):
        count = 0

        while(len(queue) != 0):
            count = count + 1
            # start_time = time.time()

            currentIdx = self.foundMinIndex(queue, distTo)
            nextPoint = queue.pop(currentIdx)
            
            self.relax(graphEdges, nextPoint, queue, distTo)
        #     print("--- %s seconds ---" % (time.time() - start_time))

        # print 'count is ', count


    def isAllTravel(self, distTo):

        for i in distTo:
            if distTo[i] == sys.maxint:
                return False
        return True

    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        edges = self.initGraph(times, N)
        nodes = range(1, N+1)
        distTo = dict.fromkeys(nodes, sys.maxint)
        distTo[K] = 0
        queue = range(1, N+1)


        self.dfs(edges, queue, distTo)

        if not self.isAllTravel(distTo):
            return -1
        else:
            return max(distTo.values())


if __name__ == "__main__":
    grid = [[2, 1, 2], [2, 3, 1], [3, 4, 1], [4, 5, 1]]
    
    grid=[[3,38,69],[8,3,96],[1,41,4],[13,8,15],[44,42,39],[8,11,24],[3,15,64],[45,34,26],[1,44,8],[38,20,61],[31,25,51],[2,34,53],[48,34,45],[4,48,2],[21,43,45],[10,1,56],[36,3,72],[50,49,55],[28,49,99],[21,50,17],[45,1,68],[28,6,67],[14,1,71],[13,5,41],[6,1,51],[8,7,36],[12,31,38],[10,37,17],[11,38,53],[48,8,54],[18,5,54],[36,34,59],[4,47,61],[27,10,65],[18,17,67],[21,24,25],[7,50,47],[45,17,7],[32,20,7],[41,24,24],[47,30,61],[31,41,66],[29,4,42],[11,6,38],[33,31,64],[42,17,20],[41,15,66],[8,22,49],[29,31,89],[39,36,16],[19,27,82],[47,32,77],[37,1,89],[42,40,21],[25,6,15],[41,28,55],[5,44,64],[29,43,95],[9,34,49],[16,22,36],[34,42,64],[18,39,46],[45,27,46],[34,20,37],[8,44,44],[23,35,71],[30,41,64],[45,19,6],[42,30,90],[41,47,63],[29,30,5],[44,47,95],[40,44,23],[38,29,42],[28,36,38],[22,10,74],[44,40,14],[8,36,35],[17,27,66],[9,19,62],[22,47,91],[29,40,39],[24,31,84],[47,19,63],[42,46,0],[30,19,60],[6,12,1],[20,22,36],[7,40,12],[23,48,30],[35,21,26],[28,50,18],[20,23,98],[6,22,18],[19,13,15],[22,44,34],[34,49,97],[35,20,70],[21,29,59],[35,1,58],[15,38,79],[43,17,78],[13,38,2],[12,44,23],[32,14,87],[48,35,80],[34,18,80],[31,4,2],[4,24,80],[15,10,32],[22,3,18],[39,33,80],[26,35,93],[21,11,25],[35,48,24],[19,31,57],[39,13,39],[44,15,92],[20,45,57],[29,28,32],[3,49,86],[23,39,18],[3,17,4],[49,37,14],[26,21,64],[50,42,94],[7,32,56],[48,25,73],[43,44,17],[50,23,46],[34,27,97],[20,49,37],[40,3,3],[44,1,42],[9,26,62],[23,27,5],[19,35,86],[27,33,61],[50,25,4],[20,26,76],[18,9,2],[15,30,52],[5,19,55],[8,12,7],[50,22,35],[15,46,61],[20,14,48],[7,43,30],[18,44,56],[24,13,31],[3,31,91],[7,47,70],[39,17,10],[2,24,61],[24,11,75],[19,25,95],[35,23,53],[27,5,72],[20,11,95],[35,42,47],[17,35,54],[45,32,27],[46,7,88],[19,18,64],[40,42,11],[24,16,64],[50,20,36],[21,30,83],[5,23,31],[21,7,37],[36,11,2],[3,5,33],[30,50,89],[18,21,58],[34,10,49],[45,33,14],[11,34,35],[47,6,64],[31,11,36],[14,33,42],[1,20,52],[3,22,8],[38,3,10],[29,23,82],[38,6,91],[39,3,75],[4,13,10],[41,12,65],[6,44,77],[42,9,60],[37,9,81],[41,13,55],[30,32,93],[17,38,36],[6,42,11],[22,1,16],[39,8,61],[17,2,19],[29,38,79],[10,30,43],[15,31,44],[25,42,76],[6,37,92],[45,23,99],[38,36,11],[44,9,12],[12,48,21],[26,14,72],[45,42,11],[27,3,91],[20,18,71],[17,44,15],[43,1,51],[37,48,76],[37,35,63],[50,30,72],[14,42,71],[36,17,86],[8,13,29],[20,39,81],[1,34,76],[44,49,70],[47,1,56],[44,29,94],[28,42,44],[10,16,9],[1,39,44],[5,33,5],[24,22,87],[38,21,11],[32,30,71],[38,25,99],[35,2,42],[31,13,10],[40,13,0],[35,33,77],[41,16,82],[16,39,69],[1,22,59],[23,33,44],[42,14,25],[13,3,49],[14,39,2],[16,19,10],[28,21,96],[13,48,86],[28,31,51],[16,2,53],[37,13,25],[18,34,83],[32,38,32],[46,27,35],[1,24,6],[30,44,2],[42,44,88],[19,26,91],[36,27,44],[22,42,22],[42,50,39],[27,34,22],[15,16,67],[43,3,72],[46,48,84],[10,34,81],[6,31,0],[49,31,91],[26,16,13],[42,33,33],[34,36,5],[24,40,53],[47,23,49],[31,15,47],[30,34,61],[30,33,93],[23,10,8],[39,1,42],[22,36,27],[29,11,67],[41,30,7],[42,12,23],[39,5,72],[20,36,52],[5,47,83],[37,42,6],[48,2,46],[48,44,19],[35,22,97],[48,41,81],[31,33,62],[38,27,24],[11,15,78],[35,36,65],[37,41,13],[21,27,54],[29,25,55],[25,24,99],[46,11,22],[43,8,12],[26,38,96],[39,27,72],[15,39,39],[25,11,9],[15,24,81],[12,20,35],[38,45,86],[33,5,8],[25,14,72],[20,43,28],[17,31,2],[42,6,14],[39,34,64],[19,45,33],[4,32,78],[41,14,34],[1,40,48],[24,44,0],[45,36,29],[36,46,97],[19,49,90],[26,13,92],[47,3,75],[12,21,21],[47,27,2],[25,19,17],[10,19,59],[3,10,37],[41,39,75],[36,39,93],[36,29,20],[49,22,16],[30,24,70],[29,2,24],[3,20,94],[14,40,53],[23,34,5],[33,21,47],[23,46,83],[13,41,18],[42,11,68],[22,15,60],[47,37,88],[48,12,93],[19,6,56],[10,11,79],[43,18,13],[36,13,48],[49,6,66],[42,18,87],[8,49,8],[5,9,47],[4,22,92],[24,29,49],[33,39,80],[28,8,93],[29,9,20],[29,14,39],[20,34,26],[27,32,34],[41,11,40],[46,32,32],[21,12,33],[3,2,13],[32,9,6],[28,32,87],[37,4,15],[2,43,37],[35,19,65],[17,5,15],[9,45,75],[49,42,58],[34,12,71],[23,31,49],[34,39,27],[17,28,15],[20,46,18],[13,33,53],[33,48,21],[38,16,81],[34,41,30],[28,2,15],[39,23,81],[5,48,13],[5,31,52],[34,47,29],[49,16,74],[19,30,8],[22,13,56],[45,2,23],[27,37,13],[9,14,66],[24,3,39],[37,19,12],[19,23,47],[17,4,97],[32,31,66],[40,26,96],[35,29,19],[13,15,85],[2,44,80],[43,50,88],[31,20,53],[49,44,52],[15,48,50],[49,28,68],[12,18,7],[39,15,93],[17,34,55],[31,19,75],[9,23,20],[23,32,45],[44,37,95],[38,39,60],[37,39,10],[16,7,71],[33,17,59],[47,10,27],[33,16,57],[3,43,18],[25,16,58],[40,38,91],[37,33,77],[32,22,16],[44,8,56],[4,25,65],[27,8,81],[43,15,89],[8,25,42],[3,45,68],[10,7,96],[46,39,73],[30,13,41],[23,22,98],[29,47,15],[7,6,96],[45,13,38],[11,3,98],[37,45,2],[23,28,33],[20,16,58],[49,30,0],[24,2,50],[16,10,2],[14,6,14],[2,19,16],[2,5,12],[4,38,77],[8,23,19],[49,18,96],[50,18,49],[47,33,58],[1,46,64],[18,50,32],[39,49,56],[26,28,82],[50,31,34],[9,3,53],[27,26,1],[44,24,53],[12,23,1],[44,34,52],[40,50,69],[41,32,54],[43,22,4],[49,50,83],[14,18,59],[20,29,89],[42,31,35],[4,17,56],[8,9,30],[43,30,65],[10,39,33],[32,24,80],[7,5,99],[38,46,43],[18,31,69],[50,7,95],[5,25,3],[14,34,85],[28,45,14],[28,37,96],[43,48,84],[11,10,88],[17,10,75],[12,5,92],[43,26,43],[1,23,97],[28,29,13],[11,14,90],[7,31,69],[13,43,23],[23,3,63],[39,14,91],[49,20,28],[26,48,41],[43,6,85],[19,22,78],[32,16,53],[6,18,17],[9,49,51],[44,45,98],[25,43,69],[6,19,16],[31,35,49],[24,41,86],[44,14,17],[27,29,70],[35,49,39],[35,46,26],[33,22,18],[4,27,88],[22,26,46],[2,12,47],[25,2,33],[21,17,2],[49,48,25],[33,46,16],[13,26,16],[43,12,63],[19,46,84],[40,49,61],[30,20,38],[26,22,99],[25,48,3],[9,20,19],[13,19,66],[38,1,13],[5,14,91],[23,8,2],[20,47,80],[49,17,70],[27,40,70],[1,37,25],[11,7,44],[24,25,63],[11,27,28],[17,40,19],[39,50,22],[24,28,20],[26,19,25],[15,44,35],[23,40,8],[49,5,21],[25,34,37],[17,3,26],[16,27,1],[45,47,96],[23,41,3],[21,14,81],[46,34,25],[20,25,34],[18,30,55],[44,13,44],[10,17,22],[27,44,24],[23,42,20],[17,11,44],[8,15,14],[21,46,4],[11,43,39],[36,12,64],[22,29,93],[29,22,7],[24,34,25],[48,10,70],[24,35,14],[25,41,7],[30,36,63],[42,28,3],[28,39,19],[41,22,52],[26,49,51],[37,20,75],[21,34,71],[22,8,11],[31,49,18],[12,38,30],[50,9,81],[36,44,15],[43,45,47],[14,16,7],[6,46,57],[12,4,18],[42,4,26],[49,35,35],[21,38,18],[44,2,60],[38,2,74],[5,11,51],[3,18,98],[12,8,80],[25,12,98],[19,17,77],[43,42,75],[30,27,21],[30,49,10],[50,44,13],[11,32,64],[37,38,26],[44,38,53],[2,18,77],[15,17,95],[31,46,40],[24,23,19],[1,50,5],[1,43,19],[13,24,35],[49,14,62],[38,5,55],[38,23,12],[35,5,7],[27,28,29],[26,47,75],[21,2,60],[11,9,51],[50,14,58],[26,23,17],[22,12,91],[47,43,24],[26,25,20],[5,50,68],[19,2,35],[31,48,24],[41,6,27],[42,19,85],[19,44,54],[41,7,98],[26,5,96],[22,45,51],[26,46,71],[8,29,39],[20,8,87],[12,14,14],[5,34,52],[7,15,85],[5,41,39],[3,11,70],[25,7,21],[45,11,29],[34,22,93],[5,29,32],[30,2,94],[8,10,60],[1,33,18],[43,19,26],[45,22,70],[7,2,6],[28,47,12],[9,31,80],[4,30,3],[50,41,40],[11,33,6],[13,17,24],[26,20,69],[16,18,17],[22,21,75],[39,10,98],[21,13,78],[24,48,60],[1,36,71],[9,48,88],[34,25,9],[3,21,56],[20,40,25],[4,42,79],[28,14,15],[8,39,64],[19,14,53],[21,1,24],[30,1,64],[15,25,25],[19,47,33],[49,15,21],[24,8,22],[8,6,28],[35,37,78],[1,3,55],[27,23,3],[42,21,88],[42,35,61],[20,44,35],[27,16,75],[43,31,32],[28,9,41],[33,37,27],[21,18,78],[23,25,6],[45,30,15],[6,21,88],[46,13,24],[8,34,18],[43,10,85],[20,2,15],[4,31,25],[46,15,64],[32,3,6],[3,37,26],[15,6,21],[7,11,6],[18,47,27],[32,2,39],[4,1,50],[37,6,8],[14,32,91],[21,41,5],[49,40,19],[9,46,86],[5,26,7],[35,26,14],[37,28,50],[42,37,95],[6,50,28],[47,22,69],[13,37,92],[2,40,69],[12,1,55],[40,15,91],[34,5,63],[41,4,91],[27,48,96],[10,5,97],[29,20,49],[13,20,93],[4,36,37],[21,4,20],[25,17,60],[31,8,48],[10,21,91],[38,18,39],[4,23,50],[11,20,30],[30,21,99],[21,16,88],[9,11,72],[35,18,86],[9,27,13],[19,50,66],[47,13,39],[49,33,74],[13,27,4],[22,39,28],[9,16,13],[26,4,46],[39,40,84],[16,6,4],[30,47,52],[14,21,72],[13,34,0],[17,7,39],[42,10,56],[11,22,96],[14,5,83],[43,2,87],[6,24,59],[13,2,83],[29,8,93],[20,19,1],[16,41,83],[26,3,7],[8,41,83],[35,32,83],[44,28,55],[12,29,70],[2,15,98],[23,7,9],[12,15,30],[44,25,90],[12,41,51],[21,42,75],[48,49,86],[28,22,90],[44,20,95],[5,24,54],[49,43,45],[32,4,59],[24,5,4],[36,33,5],[13,32,4],[2,11,77],[42,5,96],[39,21,41],[43,47,47],[50,29,10],[17,15,14],[31,2,98],[32,42,17],[17,49,70],[17,6,55],[20,3,62],[25,31,87],[4,21,50],[4,9,66],[35,50,83],[28,19,43],[42,48,44],[35,14,1],[41,35,5],[5,6,88],[30,38,27],[20,35,80],[43,35,83],[36,48,19],[7,20,21],[3,7,36],[4,49,20],[34,16,76],[6,2,57],[48,36,92],[50,38,62],[1,25,59],[34,31,23],[7,33,79],[43,36,79],[13,44,34],[18,8,21],[23,9,78],[22,46,70],[21,35,84],[44,48,62],[36,35,61],[18,29,48],[36,37,50],[25,3,87],[47,50,9],[19,36,94],[40,41,59],[19,20,96],[16,34,28],[15,27,72],[47,12,60],[20,24,9],[38,48,15],[32,45,5],[24,4,75],[44,50,31],[30,43,78],[41,27,62],[10,50,23],[8,33,4],[12,13,29],[37,8,81],[20,33,98],[33,1,17],[32,27,88],[30,10,44],[34,50,70],[47,14,52],[34,4,55],[32,40,93],[11,21,62],[17,9,20],[2,9,90],[29,37,48],[10,46,92],[15,41,10],[17,25,32],[2,29,39],[40,48,15],[48,20,66],[9,10,50],[45,41,86],[34,37,44],[37,43,19],[12,27,23],[10,9,1],[7,49,0],[6,32,91],[29,45,72],[12,32,68],[6,36,5],[17,13,80],[10,29,42],[18,32,50],[1,15,72],[32,6,24],[20,28,97],[3,48,88],[27,46,20],[39,29,79],[19,21,99],[50,21,68],[1,4,1],[46,4,13],[44,7,22],[16,26,4],[11,13,39],[22,23,7],[38,8,29],[40,11,83],[33,29,67],[36,42,60],[12,46,33],[3,46,3],[18,37,26],[15,47,25],[6,10,8],[43,23,96],[30,16,9],[43,13,31],[22,40,72],[15,45,69],[13,50,26],[19,9,86],[36,9,1],[15,40,63],[5,20,26],[49,46,66],[1,8,15],[29,26,75],[16,40,64],[46,26,49],[45,5,95],[36,20,92],[12,24,76],[41,3,65],[9,5,24],[24,33,0],[42,13,95],[10,6,45],[38,42,52],[38,24,5],[5,32,59],[29,5,94],[31,5,95],[32,44,43],[42,1,88],[32,26,44],[19,48,65],[23,44,48],[23,47,33],[16,28,78],[29,1,6],[10,28,85],[41,5,81],[7,35,62],[44,21,1],[17,36,63],[15,14,2],[46,16,65],[5,45,2],[47,49,83],[3,34,97],[48,6,98],[9,28,16],[34,7,45],[22,18,33],[36,50,5],[41,18,0],[46,18,58],[26,37,53],[17,20,61],[29,46,19],[43,25,35],[44,31,71],[26,12,99],[10,49,16],[20,12,42],[29,7,68],[2,3,5],[34,6,50],[9,39,59],[43,49,53],[23,2,28],[50,36,86],[14,23,16],[18,25,0],[8,38,51],[15,12,77],[14,11,3],[41,46,23],[16,15,94],[8,32,18],[16,23,87],[25,10,38],[11,35,54],[50,48,39],[14,43,99],[48,13,10],[45,9,3],[10,33,42],[32,25,16],[2,48,63],[36,2,35],[13,4,35],[4,19,29],[5,18,41],[16,13,52],[10,31,95],[37,50,96],[10,2,98],[11,50,61],[49,3,49],[35,16,28],[16,21,95],[7,38,59],[11,8,35],[18,33,30],[16,42,82],[16,5,33],[28,3,85],[29,15,43],[15,32,71],[30,4,18],[38,41,30],[16,50,23],[12,10,37],[46,25,91],[32,12,10],[17,42,82],[17,43,99],[11,46,59],[7,9,68],[45,6,93],[47,34,1],[31,45,63],[28,40,97],[7,41,1],[36,41,75],[35,6,91],[3,4,13],[22,48,68],[15,37,54],[8,45,66],[21,25,57],[48,21,54],[31,6,46],[2,50,38],[1,48,64],[39,35,88],[29,24,29],[8,17,84],[6,17,83],[32,13,17],[42,23,73],[39,48,16],[15,33,94],[41,10,15],[33,13,45],[6,25,25],[43,46,13],[20,5,18],[7,24,92],[1,7,12],[3,6,64],[22,4,84],[13,16,53],[14,29,93],[47,45,36],[49,2,1],[21,49,28],[11,19,77],[33,2,72],[44,36,13],[29,50,30],[34,19,17],[12,28,33],[41,38,2],[18,20,55],[42,32,14],[16,12,0],[36,30,49],[5,30,83],[41,20,71],[45,38,40],[48,33,9],[40,29,41],[8,35,48],[38,19,88],[9,40,34],[48,32,83],[29,6,98],[46,49,97],[7,12,54],[37,26,17],[43,9,26],[11,49,34],[2,33,82],[13,40,66],[14,36,47],[22,49,1],[18,46,87],[42,34,32],[4,35,66],[7,17,0],[3,23,22],[21,40,60],[22,7,55],[21,31,1],[46,35,45],[35,8,81],[38,49,17],[36,26,75],[34,3,59],[36,23,39],[35,15,80],[20,42,14],[32,21,33],[7,48,30],[17,8,57],[6,27,83],[18,43,79],[10,8,50],[36,43,98],[29,44,47],[40,7,11],[7,10,96],[49,10,14],[14,45,38],[24,10,68],[19,8,65],[47,11,53],[9,30,35],[36,14,67],[20,27,3],[3,14,67],[38,9,78],[2,28,28],[23,6,75],[36,28,34],[44,22,49],[15,20,80],[23,26,25],[1,29,52],[32,1,10],[7,46,59],[42,25,93],[24,37,25],[7,30,48],[9,32,21],[23,1,1],[25,38,97],[3,8,17],[10,38,17],[7,26,57],[41,49,79],[41,17,18],[30,18,61],[7,45,8],[15,22,17],[7,22,96],[50,24,90],[14,2,70],[26,9,18],[6,11,73],[47,5,33],[32,7,85],[11,23,70],[15,43,46],[25,13,39],[12,6,8],[40,28,78],[13,29,91],[6,29,44],[30,42,84],[30,39,95],[32,39,87],[26,45,34],[4,44,49],[45,26,70],[24,47,73],[24,20,80],[15,2,59],[16,48,36],[36,25,25],[49,32,65],[50,27,71],[45,8,56],[29,13,92],[40,1,36],[26,36,60],[7,19,49],[33,43,45],[25,26,76],[40,21,16],[27,35,87],[15,13,73],[31,12,97],[33,34,2],[33,40,20],[34,23,62],[30,15,13],[40,47,61],[8,26,95],[46,40,59],[19,42,12],[28,27,38],[30,9,77],[2,17,71],[29,10,20],[31,1,18],[30,48,82],[13,39,47],[42,16,85],[23,24,14],[19,43,88],[18,49,95],[2,20,64],[45,35,53],[42,26,68],[27,49,93],[10,13,18],[50,1,41],[19,1,88],[15,11,12],[20,50,66],[6,5,7],[36,31,18],[30,5,29],[14,19,20],[41,26,17],[20,31,1],[26,40,82],[1,27,62],[32,47,11],[25,46,79],[50,15,94],[47,36,74],[50,12,66],[34,1,17],[13,18,98],[42,41,50],[25,1,59],[1,30,73],[14,48,6],[27,41,54],[10,41,71],[46,44,86],[16,44,59],[18,35,2],[18,41,81],[44,43,92],[19,10,97],[28,18,25],[31,14,59],[2,10,52],[46,50,43],[33,4,62],[25,37,5],[17,30,75],[6,39,65],[8,48,42],[21,8,38],[12,36,81],[2,41,69],[18,23,85],[37,22,31],[30,14,40],[19,34,49],[26,8,76],[8,43,85],[36,8,63],[34,28,93],[33,20,92],[24,7,36],[30,29,86],[8,14,27],[15,29,35],[25,23,62],[47,31,5],[31,23,49],[39,31,40],[42,43,36],[24,50,18],[25,50,8],[7,21,16],[14,50,61],[48,9,43],[21,9,31],[37,24,99],[39,28,43],[29,21,10],[38,44,27],[1,45,40],[8,40,28],[25,21,39],[37,30,44],[47,38,52],[5,3,77],[15,42,57],[20,15,56],[30,46,97],[27,39,44],[4,33,21],[4,34,98],[10,36,27],[35,45,94],[38,22,48],[48,27,5],[25,15,50],[33,24,3],[17,48,8],[19,37,26],[44,18,10],[39,12,54],[41,1,76],[22,37,63],[14,12,33],[3,50,35],[3,28,26],[38,50,12],[1,31,26],[47,4,84],[38,37,43],[27,7,46],[49,26,38],[4,29,91],[23,45,20],[20,13,76],[6,20,68],[9,37,59],[14,15,50],[48,22,24],[13,1,99],[39,37,95],[6,43,17],[14,20,85],[12,7,83],[28,11,46],[3,27,71],[28,34,91],[2,36,46],[16,24,63],[9,35,21],[42,7,93],[17,22,1],[15,1,13],[46,42,8],[49,27,6],[35,27,21],[8,42,31],[26,1,7],[42,24,60],[8,24,74],[21,39,19],[38,30,87],[46,45,83],[32,15,60],[34,26,36],[16,20,50],[45,21,39],[21,45,61],[49,38,55],[33,18,29],[48,39,32],[38,11,42],[27,24,23],[9,22,55],[28,4,81],[25,45,13],[15,7,55],[20,48,91],[39,18,11],[13,23,59],[28,33,47],[12,49,7],[32,33,35],[27,38,76],[46,14,90],[48,18,81],[30,6,59],[17,32,54],[18,22,73],[19,40,60],[46,38,50],[31,44,32],[13,28,68],[37,5,84],[42,15,2],[23,21,69],[47,16,64],[10,25,77],[12,16,31],[29,39,33],[20,6,9],[23,30,29],[44,27,75],[11,28,20],[3,33,19],[42,49,85],[28,13,62],[13,25,41],[42,2,79],[11,29,83],[45,50,57],[6,7,40],[26,31,48],[4,45,62],[35,12,74],[11,5,50],[30,12,97],[28,43,5],[18,42,12],[45,24,61],[24,36,80],[36,1,12],[4,18,19],[23,13,35],[18,14,63],[41,25,15],[1,49,74],[3,13,29],[20,32,54],[50,34,66],[32,34,92],[2,42,8],[13,14,99],[44,32,30],[32,37,62],[45,37,31],[46,33,56],[4,50,32],[18,15,96],[34,43,12],[21,28,76],[8,50,49],[43,34,87],[39,42,97],[46,2,1],[28,10,0],[49,13,52],[30,26,38],[24,19,23],[21,48,4],[30,17,21],[6,14,98],[40,17,68],[45,49,45],[14,8,85],[48,28,32],[3,9,48],[6,38,13],[14,17,18],[41,37,36],[47,26,53],[14,26,41],[48,30,49],[14,4,43],[27,14,48],[40,32,66],[46,9,47],[17,14,59],[5,16,28],[2,47,29],[2,1,43],[22,20,44],[13,46,20],[18,26,72],[35,39,83],[36,38,72],[40,37,54],[48,46,84],[31,34,19],[5,8,38],[46,24,22],[35,10,76],[33,47,38],[16,30,58],[1,21,64],[43,4,39],[5,7,49],[22,6,58],[20,9,30],[31,50,34],[28,46,99],[49,21,58],[38,26,55],[7,37,48],[39,38,80],[42,38,52],[50,33,36],[42,20,62],[24,17,5],[46,10,44],[45,48,81],[22,30,40],[11,16,3],[50,11,77],[44,10,56],[1,2,87],[28,41,58],[14,28,12],[24,38,78],[9,44,47],[8,4,24],[13,30,95],[16,33,34],[45,25,44],[4,7,57],[5,37,64],[11,44,42],[33,30,50],[34,14,90],[47,15,66],[29,36,98],[1,35,10],[8,27,38],[25,8,51],[35,17,49],[31,30,19],[43,20,12],[10,48,21],[21,26,41],[9,12,29],[3,16,61],[27,13,71],[14,30,30],[22,41,9],[16,37,79],[43,11,11],[45,15,85],[48,7,58],[31,21,97],[35,9,54],[34,24,92],[40,10,97],[31,47,65],[11,36,97],[21,15,66],[31,22,52],[15,50,11],[33,41,63],[12,9,83],[4,2,64],[18,19,65],[29,42,73],[12,17,53],[45,29,93],[30,23,37],[14,25,47],[12,37,45],[27,15,88],[36,6,62],[39,11,91],[35,40,3],[27,2,32],[47,25,37],[16,3,0],[29,16,38],[31,32,79],[9,50,31],[18,36,43],[31,24,72],[27,20,91],[9,15,29],[19,32,77],[48,1,15],[21,19,15],[38,10,43],[20,7,11],[3,30,94],[50,17,67],[26,7,13],[18,12,7],[7,25,99],[25,9,62],[27,25,82],[47,21,33],[7,27,84],[19,11,9],[46,17,68],[27,45,6],[12,40,55],[25,4,63],[5,4,74],[50,39,22],[26,15,33],[35,24,79],[7,34,11],[45,31,99],[47,42,34],[12,19,49],[10,12,7],[35,7,80],[24,49,87],[42,47,60],[2,30,98],[39,9,27],[34,30,24],[16,45,34],[37,18,94],[4,5,31],[30,25,75],[1,26,26],[38,7,64],[22,38,36],[4,3,66],[35,4,96],[43,7,34],[21,3,78],[34,48,33],[10,32,99],[16,17,84],[15,28,52],[41,31,81],[38,4,35],[18,48,27],[37,47,21],[46,23,0],[29,33,46],[10,23,80],[50,3,50],[14,10,65],[9,8,86],[15,18,28],[31,27,59],[44,6,90],[20,17,4],[21,22,14],[6,33,75],[44,19,6],[27,30,92],[25,47,40],[26,10,80],[4,14,71],[23,4,65],[41,23,4],[1,32,15],[32,8,33],[12,45,65],[7,23,94],[32,36,66],[40,33,48],[24,43,73],[1,12,93],[16,47,28],[49,34,47],[48,5,2],[40,8,13],[7,44,86],[14,47,64],[18,45,99],[29,34,26],[7,14,20],[25,32,12],[26,43,86],[34,38,72],[47,35,88],[6,26,39],[29,12,89],[40,45,46],[19,28,99],[13,45,85],[48,42,69],[23,37,82],[48,19,36],[32,28,74],[24,26,36],[27,6,59],[10,26,22],[35,47,95],[6,41,54],[50,4,40],[10,47,18],[14,49,76],[41,9,62],[40,5,75],[48,23,6],[40,2,64],[32,48,27],[19,41,38],[8,47,13],[50,8,30],[49,7,3],[5,35,16],[1,9,84],[35,34,64],[42,39,39],[22,50,66],[24,6,69],[10,43,53],[26,27,18],[43,41,12],[32,18,91],[47,18,99],[5,39,8],[47,44,33],[14,7,54],[4,26,10],[17,1,13],[23,17,84],[6,48,62],[19,7,29],[22,32,40],[5,15,76],[44,12,66],[48,40,61],[33,50,20],[39,30,43],[18,10,39],[33,36,19],[39,32,80],[23,49,41],[3,19,40],[11,25,48],[31,38,73],[12,39,9],[43,21,65],[9,17,10],[5,36,74],[37,25,99],[7,3,19],[24,30,4],[40,14,24],[2,13,31],[9,25,27],[27,36,0],[36,10,28],[10,35,52],[36,21,53],[21,10,37],[13,6,97],[9,29,27],[39,47,80],[36,40,36],[24,45,94],[35,28,14],[37,31,8],[40,35,37],[43,28,54],[19,3,95],[12,42,73],[33,6,17],[41,40,67],[46,22,22],[37,32,28],[48,29,15],[12,43,87],[4,46,77],[27,9,76],[38,47,63],[43,14,0],[28,38,66],[1,18,69],[48,47,19],[47,9,67],[2,26,2],[34,9,35],[35,25,37],[44,23,97],[11,47,61],[29,48,20],[33,45,28],[5,42,90],[49,12,75],[25,33,67],[49,1,79],[6,45,40],[48,31,72],[49,47,89],[11,40,56],[33,44,97],[34,40,43],[40,46,84],[31,17,89],[23,50,58],[13,22,37],[47,24,51],[22,24,61],[4,20,89],[34,46,77],[22,2,92],[31,7,21],[2,37,62],[38,17,57],[27,11,55],[43,5,95],[17,37,11],[33,14,22],[18,4,41],[44,11,33],[40,23,89],[46,6,33],[16,14,47],[31,10,33],[46,1,14],[25,27,50],[7,8,67],[22,25,4],[46,20,71],[8,1,99],[16,38,70],[17,41,44],[31,36,7],[2,25,41],[30,8,82],[42,36,98],[21,44,46],[15,35,96],[16,9,90],[18,11,61],[11,45,38],[5,28,74],[10,22,87],[14,3,25],[31,26,1],[8,2,13],[40,6,72],[15,36,76],[49,39,48],[27,50,5],[6,9,69],[40,9,55],[30,7,94],[13,49,59],[17,47,58],[2,16,5],[37,21,62],[37,46,70],[28,26,11],[14,31,80],[39,19,7],[9,18,20],[48,15,90],[8,19,1],[32,43,45],[7,39,73],[26,32,91],[25,35,97],[22,17,96],[30,31,23],[49,8,31],[44,3,27],[20,1,88],[17,24,10],[19,12,66],[43,16,12],[2,27,10],[9,47,75],[7,13,70],[30,22,30],[29,27,61],[2,8,40],[33,10,90],[41,42,57],[50,35,32],[42,22,23],[5,38,33],[46,30,91],[9,2,14],[1,16,11],[36,32,46],[14,9,21],[24,32,95],[36,5,7],[15,26,16],[26,39,15],[11,39,28],[24,18,23],[3,42,49],[46,3,20],[28,23,64],[7,18,14],[12,30,9],[2,7,24],[35,30,16],[9,7,79],[29,35,54],[45,44,22],[11,1,60],[36,49,64],[29,3,94],[32,19,20],[34,29,89],[15,19,45],[18,38,44],[49,36,44],[36,45,9],[38,14,70],[41,8,57],[22,5,86],[33,42,8],[9,6,45],[4,15,84],[32,50,47],[10,45,42],[19,24,38],[33,11,4],[40,34,9],[34,8,85],[31,28,53],[16,49,76],[45,4,79],[45,20,95],[18,2,3],[40,39,52],[44,46,9],[28,12,57],[29,17,98],[41,43,29],[39,20,71],[29,49,34],[11,31,18],[1,47,78],[38,12,99],[17,50,27],[30,40,32],[28,24,20],[28,48,32],[27,17,42],[5,43,62],[21,36,89],[3,12,62],[46,47,13],[5,13,0],[25,5,5],[18,3,12],[11,48,62],[25,44,72],[24,42,7],[5,40,61],[12,2,19],[7,42,92],[50,6,5],[24,27,46],[18,6,61],[41,34,50],[45,28,12],[33,28,42],[11,4,52],[9,41,11],[20,21,27],[29,19,25],[38,31,19],[23,38,44],[11,30,51],[44,35,8],[46,29,24],[36,24,46],[37,36,12],[34,32,69],[48,3,47],[30,45,89],[14,37,78],[7,1,63],[45,7,26],[24,14,10],[4,40,47],[10,14,17],[14,24,47],[8,18,56],[40,12,7],[23,18,58],[1,42,97],[4,11,61],[39,2,70],[39,45,11],[5,1,12],[23,14,73],[20,37,12],[48,26,89],[21,47,76],[42,3,83],[14,44,80],[50,40,47],[19,16,68],[12,3,67],[45,39,87],[33,26,85],[27,1,14],[26,44,54],[39,41,57],[28,20,95],[9,38,74],[23,43,8],[11,24,93],[46,36,90],[8,31,10],[37,3,82],[31,40,49],[45,16,66],[11,37,29],[16,4,17],[26,50,27],[31,29,30],[49,23,54],[46,41,39],[37,15,75],[10,27,47],[1,6,77],[17,19,63],[5,22,12],[22,33,0],[49,25,78],[2,21,82],[45,10,53],[6,30,28],[45,46,56],[15,9,29],[7,28,99],[10,18,54],[25,20,24],[3,36,12],[16,36,19],[42,45,43],[16,1,54],[4,39,19],[34,44,65],[15,3,61],[30,28,25],[38,34,57],[48,14,44],[39,44,59],[33,35,98],[37,12,46],[27,4,16],[25,36,39],[35,43,58],[23,5,93],[4,10,4],[5,21,87],[6,49,61],[43,40,85],[4,8,28],[8,5,67],[34,17,19],[48,38,9],[30,35,63],[4,12,26],[44,5,18],[30,11,29],[33,23,91],[28,16,95],[8,21,33],[50,45,91],[48,43,7],[32,17,80],[41,48,15],[30,3,68],[13,21,48],[34,45,2],[7,36,9],[22,16,36],[13,10,35],[27,31,72],[29,41,12],[36,4,13],[27,22,56],[10,24,31],[8,16,21],[50,32,89],[46,31,33],[35,3,62],[4,16,46],[7,16,86],[27,19,29],[43,24,38],[36,19,34],[45,12,47],[16,32,9],[3,29,66],[6,28,1],[26,2,95],[47,28,11],[4,6,34],[16,35,46],[46,12,49],[23,16,54],[19,4,97],[15,23,14],[32,29,44],[1,10,43],[17,26,98],[44,39,42],[10,44,32],[14,13,10],[44,33,17],[12,33,21],[23,15,87],[25,40,19],[6,23,29],[39,46,65],[13,35,84],[49,4,22],[11,26,60],[33,7,0],[19,33,2],[50,19,11],[44,17,21],[19,29,83],[15,34,17],[39,43,42],[23,29,27],[40,36,20],[37,2,98],[16,8,72],[1,13,27],[22,11,95],[15,49,79],[49,41,82],[47,41,57],[11,41,58],[39,4,8],[10,15,29],[6,35,50],[9,33,82],[23,12,63],[39,16,82],[39,25,34],[25,18,26],[2,4,97],[27,42,93],[46,37,0],[50,13,29],[28,7,52],[15,8,13],[9,4,60],[8,30,53],[43,29,62],[46,43,5],[10,40,24],[45,40,52],[26,18,51],[4,37,7],[50,26,60],[28,5,21],[23,19,54],[25,49,1],[48,50,63],[25,29,40],[38,13,23],[12,25,62],[46,5,14],[35,44,30],[37,11,59],[48,17,52],[28,44,78],[33,15,69],[45,18,71],[6,15,78],[41,45,52],[49,11,91],[17,29,23],[36,7,86],[37,23,14],[43,39,67],[12,35,68],[15,4,24],[44,16,43],[25,39,3],[4,41,84],[37,17,20],[6,47,31],[43,27,46],[50,47,74],[16,29,7],[35,41,64],[47,20,61],[2,14,67],[29,18,21],[32,46,5],[40,25,85],[37,10,27],[2,35,33],[47,29,87],[2,32,86],[33,19,65],[41,19,59],[18,16,52],[5,49,44],[18,13,49],[28,17,50],[12,22,16],[26,33,76],[12,34,25],[33,8,72],[32,49,34],[50,16,87],[36,47,76],[3,32,8],[34,13,18],[14,38,69],[28,15,33],[36,16,32],[38,28,27],[50,37,63],[33,27,48],[3,25,29],[43,38,65],[29,32,38],[2,6,89],[13,11,92],[9,24,7],[2,22,16],[11,2,65],[4,28,38],[27,43,12],[22,28,19],[32,41,58],[20,38,71],[31,16,98],[33,38,27],[33,49,37],[21,23,30],[13,9,23],[24,1,51],[39,6,79],[8,28,71],[36,15,68],[22,31,96],[8,37,83],[17,18,15],[27,21,74],[17,39,10],[9,36,58],[40,19,8],[40,20,39],[31,9,43],[22,9,37],[12,50,63],[1,14,97],[41,44,26],[37,34,24],[1,28,66],[26,6,90],[6,3,75],[43,37,71],[37,29,78],[22,19,55],[35,13,14],[41,50,0],[24,46,66],[10,20,64],[33,32,98],[37,49,36],[32,35,85],[18,28,52],[48,24,64],[6,8,79],[22,35,49],[33,25,77],[17,23,42],[17,45,63],[34,35,15],[41,33,46],[46,8,87],[11,18,89],[21,33,1],[10,42,41],[2,49,40],[9,43,78],[47,48,53],[38,32,64],[24,12,44],[28,25,87],[50,28,57],[27,18,68],[31,39,67],[16,46,76],[28,35,47],[36,22,82],[25,28,34],[44,30,13],[49,45,54],[21,20,1],[45,3,22],[40,27,16],[48,37,23],[2,46,0],[18,27,83],[18,7,81],[33,12,52],[13,7,58],[50,2,1],[38,33,5],[48,4,51],[41,29,67],[5,46,34],[11,17,12],[5,10,33],[2,31,5],[14,35,85],[21,37,78],[3,47,19],[31,18,72],[14,41,5],[40,31,11],[3,39,50],[28,1,66],[2,38,57],[3,24,55],[39,22,24],[17,33,52],[19,38,89],[26,34,91],[13,31,33],[21,32,64],[34,15,22],[25,30,70],[16,11,97],[7,4,55],[37,16,84],[40,4,25],[47,46,17],[17,16,56],[26,42,67],[19,15,54],[49,24,70],[26,29,20],[47,2,41],[3,40,80],[48,16,52],[31,37,98],[2,23,95],[23,36,47],[15,21,91],[16,25,59],[2,45,37],[44,4,59],[39,24,75],[18,24,20],[34,11,58],[40,16,75],[18,1,88],[49,9,32],[37,7,96],[41,21,4],[8,20,96],[40,24,79],[12,47,24],[17,12,33],[34,21,43],[35,31,97],[37,40,70],[16,43,1],[34,33,73],[38,15,24],[37,27,95],[43,32,90],[49,19,74],[50,10,65],[46,28,62],[6,13,4],[1,11,38],[9,42,49],[5,27,43],[6,4,47],[13,36,41],[35,11,37],[44,41,82],[24,15,25],[4,43,12],[22,27,43],[10,4,9],[28,30,42],[43,33,96],[37,44,27],[3,1,69],[47,7,81],[27,12,36],[14,22,1],[32,23,15],[5,12,66],[1,19,26],[41,36,14],[32,5,29],[21,5,0],[47,8,90],[41,2,17],[45,43,91],[27,47,5],[21,6,85],[50,5,65],[31,3,50],[25,22,30],[36,18,72],[2,39,48],[19,5,37],[33,3,40],[26,30,26],[37,14,69],[1,38,11],[13,12,73],[30,37,41],[13,47,0],[6,40,55],[31,43,3],[20,4,32],[9,13,51],[6,16,78],[47,40,86],[35,38,96],[13,42,65],[26,24,21],[17,46,81],[11,42,40],[42,27,17],[3,44,64],[48,45,59],[24,21,90],[3,26,23],[20,30,74],[23,11,6],[18,40,81],[44,26,60],[5,17,67],[9,1,27],[34,2,76],[39,26,67],[8,46,56],[9,21,35],[17,21,90],[50,43,62],[38,43,19],[15,5,2],[38,35,69],[22,14,24],[26,11,61],[42,29,29],[6,34,16],[50,46,99],[46,21,74],[3,41,38],[1,17,58],[42,8,51],[19,39,50],[12,26,56],[5,2,5],[47,17,6],[48,11,7],[45,14,64],[16,31,13],[23,20,57],[40,22,14],[10,3,17],[32,11,29],[20,41,33],[40,30,68],[24,9,8],[32,10,18],[14,27,42],[12,11,48],[24,39,97],[11,12,70],[20,10,58],[40,18,67],[26,41,84],[22,34,67],[46,19,76],[14,46,34],[22,43,82],[33,9,27],[7,29,82],[26,17,47],[31,42,42],[38,40,18],[3,35,53],[49,29,82],[47,39,79],[1,5,84],[39,7,31],[40,43,1]]


    print len(grid)
    solution = Solution()
    start_time = time.time()
    print(solution.networkDelayTime(grid, 50, 2))
    print("--- %s seconds ---" % (time.time() - start_time))
