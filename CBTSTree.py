class CBSTree: 
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def inOrder(tree):
    if  tree == None: return 

    print tree.key
    inOrder(tree.left)
    inOrder(tree.right)

def generateTree(arr):
    length = len(arr)
    if length == 1:
        return CBSTree(arr[0])

    centerIndex =length /2
    centerVal = arr[centerIndex]
    newNode = CBSTree(centerVal)
    newNode.left = generateTree(arr[0:centerIndex])
    newNode.right = generateTree(arr[(centerIndex+1):length])

    return newNode



if __name__=="__main__":
    tree = generateTree([1,2,3,4,5,6,7])
    inOrder(tree)