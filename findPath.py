class FindPath:
    def __init__(self):
        self.vertex = {}

#查看以s为开始的路径。这个方法递归了太多次，不大好
checked = {}
def all_path_startwith(G,s):

    result = []
    for singlev in G.adj(s):
        if (not checked[singlev]):
            path = pathTo(G,s,singlev)
            if path:
                result.push(path)


    return result

#试一下，能不能较少递归次数
def workPath={}
def all_path_startwith2(G,s):
    result = []

    for singlev in G.adj(s):
        if (not workPath[singlev]):
            workPath[s] = singlev
            subPath = all_path_startwith2(G,singlev) #数据结构是[[2,3,4],[4,5,6]]
            
            if len(subPath) > 0:
                newPath = map(lambda x:[s].concat(subPath), subPath)
                
                result.push(newPath)


    return [s] if len(result) == 0 else result


def has_path_to(G,s, v):
    if (s === v) :
        return True
    result = False
    checked[s] = True
    for singlev in G.adj(s):
        if (not checked[singlev]):
            result = result or has_path_to(G, singlev,v)
            if result:
               break

    return result

#获取s->v的路径
def pathTo(G,s, v):
    if (s === v) :
        return [v]

    result = None
    for singlev in G.adj(s):
        if (not checked[singlev]):
            prePath = pathTo(G, singlev,v)
            if prePath :
                result = [s]+prePath
                break


    return result

#广度优先遍历,利用队列
temp = []
edgeTo ={}
def breadPathTo(G,s):
    temp.append(s)
    while(len(temp) !== 0):
        first = temp.pop(0)

        for (shortPoint in G.adj(first)):
            if (not marked[shortPoint]):
                edgeTo[shortPoint] = first
                markded[shortPoint] = True
                temp.append(shortPoint)


    
#这是一幅无环图吗
def isHasCircle(G, s): 
    checked[s] = True

    result = False
    for v in G.adj(s):
        if (s == v) return True
        if (checked[v]) return 
        result = result or isHasCircle(G, v)
        if (result) return True

    return result

#这是一幅二分图吗？
#二分图是指图的顶点会分成两个集合。某个点的邻接点，一定是属于另外一个集合
red = []
black = []
def isTwoGraph(G,s,whichColor):
    checked[s] = True
   
    if (whichColor === 'red'):
        if (s not in red):
            return False
    else:
        if (s not in black):
            return False

    result = True
    nextColor = 'red' if whichColor == 'black' else 'black'
    for v in G.adj(s):
        if (not checked[v]): 

            if nextColor == 'red' :
                red.push(v)
            else:
                black.push(v)
            result = result and  isTwoGraph(G,v, nextColor)
        if not result:
            break 

    return result
