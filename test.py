class BSTree: 
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.n = 0 
        self.height = 0 


def inOrder(self):
    if(self == None): return 

    
    inOrder(self.left) 
    print(self.key, self.n)
    inOrder(self.right)


# def insert(self, val):
#     newNode = BSTree(val)
#     if (val < self.key):
#         if (self.left == None):
#             self.left = newNode
#         else:
#             insert(self.left, val)
#     else:
#         if (self.right == None):
#             self.right = newNode
#         else:
#             insert(self.right,val)

#     return self

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


def findMinNode(tree=None):
    if tree == None:
        return None
    start  = tree
    while(start.left != None):
        start = start.left
    return start
    
def deleteTree(self, val,  parent ):
    if (self == None):
        return None

    if (val < self.key):
        deleteTree(self.left, val,self)
    elif (val > self.key):
        deleteTree(self.right, val,self)
    else:
        if (self.left == None and self.right == None):
            self = None
        elif (self.left == None):
            self.key = self.right.key
            self.right = None
            
        elif (self.right == None):
            self.key = self.left.key
            self.left = None
        else:
            lastMinNode = findMinNode(self.right)
            print ('----',lastMinNode.key)
            if lastMinNode != None: 
                deleteTree(self.right, lastMinNode.key,self)
                self.key = lastMinNode.key

    return self

def searchInRange(tree, min,max):
    if(tree == None): return 

    searchInRange(tree.left, min, max)

    if (tree.key >=min and tree.key <=max):
        print tree.key

    searchInRange(tree.right, min, max)

def floor(tree,val):
    if(tree == None): return None
    if (tree.key == val): return tree.key

    if (tree.key > val):
        return floor(tree.left, val)
    else:
        t = floor(tree.right,val)
        if t== None: 
            return tree.key
        else:
            return t.key 

def size(tree):
    if (tree == None): return 0
    len = size(tree.left) +size(tree.right)+1

    return len 

# select the node of rank k
def select(tree, k):
    if (tree == None): return None
    rank_of_current = size(tree.left) +1

    if (rank_of_current >k):
        return select(tree.left, k)
    elif (rank_of_current < k):
        return select(tree.right, k-rank_of_current-1)
    else:
        return tree.key

   
def rank(tree,key):
    if (tree == None): return 0

    len = size(tree.left)
    if (tree.key < key):
        return len + rank(tree.right, key)+1
    elif (tree.key > key):
        return rank(tree.left, key)
    else:
        return len

def height(tree):
    if (tree == None): return 0
    left_height = height(tree.left)
    right_height = height(tree.right)

    return max(left_height, right_height)+1

# def select (tree, k):
#     if (tree == None): return None
    
#     select(tree.left, k)
#     if (tree.deep == k):
#         print tree.key
#     select(tree.right, k)

def noDuplicate(tree, val):
    if (tree == None): return True

    if (tree.key == val):
        return False
    else:
        leftResult = noDuplicate(tree.left,tree.key)
        rightResult = noDuplicate(tree.right, tree.key)
        return leftResult and rightResult


def hasNoDuplicates(tree):
    if (tree == None): return True

    return noDuplicate(tree.left, tree.key) and noDuplicate(tree.right, tree.key)
    
# def isBinaryTree(tree):
    


if __name__=="__main__":
    tree = BSTree(4)
    insert2(tree,3.5)
    insert2(tree,8)
    insert2(tree,3)
    insert2(tree,7)
    insert2(tree,1)
    insert2(tree,1)

    # rank(tree)
    inOrder(tree)
    print '---------'
    print hasNoDuplicates(tree)
    # print select(tree, 3)
    # print height(tree) 
    # print tree.right.height

    # deleteTree(tree,2,tree)
    # inOrder(tree)

    # searchInRange(tree, 3,5)

    # print floor(tree,3.5)
        

    

    