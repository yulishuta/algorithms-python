class BSTree: 
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0
        self.n = 0
        self.xAxis = 0
        
def inOrder(self):
    if(self == None): return 

    
    inOrder(self.left) 
    print(self.key, self.xAxis)
    inOrder(self.right)

def insert1(node ,key):
    if node is None: 
        return BSTree(key) 
    
    if node.left ==None:
        node.left = BSTree(key) 
    elif node.right ==None:
        node.right =  BSTree(key) 
    else:
        node.left = insert1(node.left,key)

    return node 

def insert2(node,key):
     # If the tree is empty, return a new node 
    if node is None: 
        return BSTree(key) 
  
    # Otherwise recur down the tree 
    if key < node.key: 
        node.left = insert2(node.left, key) 
    else: 
        node.right = insert2(node.right, key) 
  
    # return the (unchanged) node pointer 
    #height of tree
    left_height =  1 if node.left == None else node.left.height
    right_height = 1 if node.right == None else node.right.height
    node.height = max(left_height, right_height) + 1

    return node 

def size(tree):
    if (tree == None): return 0
    len = size(tree.left) +size(tree.right)+1

    return len 


def isBTree(tree):
    if (tree == None): return True

    isLeftBTree = isBTree(tree.left)
    len = size(tree)
    return True if len == tree.n else False

    isRightBTree = isBTree(tree.right)

    return isLeftBTree and isRightBTree


def isOrdered(tree,minVal,maxVal):
    #first ordered
    if (tree == None): return True

    if (tree.key< minVal): return False
    if (tree.key > maxVal): return False
    
    # if (tree.key>= minVal and tree.key < maxVal):
    #     return True
    # else:
    #     return False

    return isOrdered(tree.left,minVal, tree.key)  and isOrdered(tree.right,tree.key, maxVal)



def draw(tree,pre):
    if (tree == None): return pre

    tree.xAxis = pre
    draw(tree.left,tree.xAxis-2)
    draw(tree.right,tree.xAxis+2 )

def minAxis(tree):
    if (tree == None): return 0

    temp = tree
    while(temp.left != None):
        temp = temp.left
    return temp.xAxis
        
def printTree(myQueue, origin):
    if (len(myQueue) == 0): return 
    myQueueLen = len(myQueue)

    temp =''
    prexAxis= 0
    for index in range(myQueueLen):
        r = myQueue.pop(0)
        sep = ''
        actual = r.xAxis+origin -prexAxis
        # print actual
        for index in range(actual):
            sep = sep + ' '
        temp =  temp + sep + str(r.key)
        if (r.left != None):
            myQueue.append(r.left)

        if (r.right != None):
            myQueue.append(r.right)

        prexAxis = r.xAxis+origin
    print(temp)

    printTree(myQueue, origin)

    



if __name__=="__main__":
    tree = BSTree(4)
    insert2(tree,3)
    insert2(tree,8)
    insert2(tree,2)
    insert2(tree,7)
    insert2(tree,1)

    # fakeTree = BSTree(1)
    # insert1(fakeTree, 3)
    # insert1(fakeTree, 2)
    # insert1(fakeTree, 5)
    # insert1(fakeTree, 8)



    # print isOrdered(tree, 0, 8)
    # print isOrdered(fakeTree, 1, 8)
    draw(tree,0)
    minAxisOfTree = minAxis(tree)
    
    inOrder(tree)
    print minAxisOfTree
    printTree([tree],abs(minAxisOfTree))