class BSTree: 
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.n = 0 
        self.height = 0 

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

def inOrder(self):
    if(self == None): return 

    
    inOrder(self.left) 
    print(self.key, self.n)
    inOrder(self.right)

def minVal(tree):
    if  tree ==None: return None
    while(tree.left != None):
        tree = tree.left
    return tree.key

def maxVal(tree):
    if  tree ==None: return None
    while(tree.right != None):
        tree = tree.right
    return tree.key

def floor(tree,key):
    if tree == None: return None
    while(tree != None):
        if (tree.key < key):
            min_val_rightTree =  minVal(tree.right)

            if (min_val_rightTree  != None and min_val_rightTree < key and min_val_rightTree < tree.key):
                return min_val_rightTree
            else:
                return tree.key
        elif(tree.key > key):
            tree = tree.left
        else:
            return tree.key
    return None

def ceiling(tree,key):
    if (tree == None): return None

    while(tree != None):
        if (tree.key < key):
            tree = tree.right
        elif(tree.key > key):
            max_of_leftTree = maxVal(tree.left)

            if (max_of_leftTree != None and max_of_leftTree>key and max_of_leftTree > tree.key ):
                return max_of_leftTree
            else:
                return tree.key
        else:
            return tree.key
    return None

#size
def size(tree):
    if (tree == None): return 0
    
    leftTree = tree.left
    rightTree = tree.right
    leftDeep = 0
    rightDeep = 0

    while(leftTree != None):
        leftTree = leftTree.left
        leftDeep  = leftDeep + 1
    while(rightTree != None):
        rightTree = rightTree.right
        rightDeep  = rightDeep + 1

    return leftDeep + rightDeep + 1
    


def select(tree, k):
    if (tree == None): return None

    while(tree != None):
        len = size(tree.left)
        if (len>k):
            tree = tree.left
        elif (len < k):
            len = k -len
            tree = tree.right
        else:
            return tree.key
    return None

def rank(tree, key):
    if (tree == None): return None

    preRank = 0
    while(tree != None):
        len = size(tree.left)
        if (tree.key > key):
            tree = tree.left
        elif (tree.key < key):
            preRank = preRank + len
            tree = tree.right
        else:
            return len + preRank +1 

    return None





if __name__=="__main__":
    tree = BSTree(4)
    insert2(tree,3.2)
    insert2(tree,8)
    insert2(tree,3)
    insert2(tree,7)
    insert2(tree,1)

    # rank(tree)
    inOrder(tree)
    print '---------'
    print('min ', minVal(tree))
    print('max', maxVal(tree))
    print('floor',3.5, floor(tree, 3.5))
    print('ceil',3.5, ceiling(tree, 3.5))
    print('size', size(tree))
    print('select',3,select(tree, 3))
    print('rank',8, rank(tree, 8))
    print('rank',3, rank(tree, 3))
    