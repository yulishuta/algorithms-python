class Node:
    def __init__(self,key, color='BLACK'):
        self.key = key
        self.left = None
        self.right = None
        self.color = color

def inOrder(tree):
    if (tree == None): return 

    inOrder(tree.left)
    print self.key
    inOrder(tree.right)

def rotateLeft(node):
    rightNode = node.right
    node.color = rightNode.color 
    node.right = rightNode.left
    rightNode.left = node
    node.color = 'RED'
    
    return rightNode

def rotateRight(node):
    leftNode = node.left
    node.color = leftNode.color
    node.right = leftNode.left
    leftNode.left = node
    leftNode.color = 'RED'
    
    return leftNode

def flipColor(node):
    if (node == None): return None
    if (node.left): node.left.color = 'BlACK'
    if (node.right): node.right.color = 'BlACK'

    node.color = 'RED'
    return node 

def isRedNode(tree):
    if(tree == None): return False

    return tree.color == 'RED'


def insert(tree, key):
    if (tree ==None): 
        return Node(key,'RED')
    
    if (key< tree.key):
        tree.left = insert(tree.left, key)
    else:
        tree.right = insert(tree.right, key)

    #yes
    if (isRedNode(tree.right) and not isRedNode(tree.left)):
        tree = rotateLeft(tree)

    if (isRedNode(tree.left) and tree.left != None and isRedNode(tree.left.left)):
        tree = rotateRight(tree)

    if (isRedNode(tree.right) and  isRedNode(tree.left)):
        flipColor(tree)
    #WRONG
    # if (isRedNode(tree.right)):
    #     if (isRedNode(tree.left)):
    #         flipColor(tree)
    #     elif not isRedNode(tree.left):
    #         tree = rotateLeft(tree)
    # elif (isRedNode(tree.left) and tree.left != None and isRedNode(tree.left.left)):
    #         tree = rotateRight(tree)

    return tree



def insert2(tree, key):
    if (tree ==None): 
        return Node(key,'RED')

    if (isRedNode(tree.right) and  isRedNode(tree.left)):
        flipColor(tree)
    
    
    if (key< tree.key):
        tree.left = insert(tree.left, key)
    else:
        tree.right = insert(tree.right, key)

    if (isRedNode(tree.right) and not isRedNode(tree.left)):
        tree = rotateLeft(tree)

    if (isRedNode(tree.left) and tree.left != None and isRedNode(tree.left.left)):
        tree = rotateRight(tree)

        
    return tree




def isTwoNode(tree):
    return not isRedNode(tree.left) and not isRedNode(tree.right)


def setRedNode(tree):
    tree.color = 'RED'

def flipColors(tree):
    tree.left.color = 'RED'
    tree.right.color = 'RED'
    tree.color = 'BLACK'

def reBuildTree(tree):
    if (isRedNode(tree.right) and not isRedNode(tree.left)):
        tree = rotateLeft(tree)

    if (isRedNode(tree.left) and tree.left != None and isRedNode(tree.left.left)):
        tree = rotateRight(tree)

        
    return tree

def moveRedToLeft(tree):
    flipColors(tree)
    tree.right = rotateRight(tree.right)
    tree = rotateLeft(tree)
    flipColors(tree)
        
    return tree

def moveRedToRight(tree):
    flipColors(tree)
    tree = rotateRight(tree)
    tree.right = rotateLeft(tree.right)
    flipColors(tree)
        
    return tree
    
def deleteMinVal(tree): 
    if(tree.left ==None):
        return None

    if (not isRedNode(tree.left.left)):
        #如果右边的节点是红的，需要进行一系列的转化
        #将右边的黑节点，移动到左边
        if (isRedNode(tree.right.left)):
            tree = moveRedToLeft(tree)
        else: 
            #两个节点都需要变红,但是为什么根节点要变黑？
            flipColors(tree)

    tree.left = deleteMinVal(tree.left)
    
    #向上的过程中重新塑造平衡二叉树
    return reBuildTree(tree)

            

def deleteMinVal1(root): 
    if(root ==None): return 

    #树的根节点比较特殊。需要保持颜色为黑节点。所以才有这层设置
    if(not isRedNode(root.left) and not isRedNode(root.right)):
        root.color ='RED'
    root = deleteMinVal(root)
    root.color ='BLACK'
    return root

def deleteMaxVal(tree):
    if (tree.right ==None):
        return None
    
    if (not isRedNode(tree.right.left)):
        #如果右边的节点是红的，需要进行一系列的转化
        #将右边的黑节点，移动到左边
        if (isRedNode(tree.left.left)):
            tree = moveRedToRight(tree)
        else: 
            #两个节点都需要变红,但是为什么根节点要变黑？
            flipColors(tree)

    tree.right = deleteMinVal(tree.right)
    
    #向上的过程中重新塑造平衡二叉树
    return reBuildTree(tree)

def getMinNode(tree):
    if (tree.left ==None) return tree.key
    return getMinNode(tree.left)
def deleteMaxVal1(root):
    if(root ==None): return 

    #树的根节点比较特殊。需要保持颜色为黑节点。所以才有这层设置
    if(not isRedNode(root.left) and not isRedNode(root.right)):
        root.color ='RED'
    root = deleteMaxVal(root)
    root.color ='BLACK'
    return root

#去选择右子树的最小值，删掉。然后替换
#缺少了关键的几步，在遍历左子树和右子树时，同时需要保证左边的
#节点是3，4节点；右边节点也是3，5
def deleteVal1(tree,val):
    if (tree.key > val):
        #走删除最小节点的路子
        if (not isRedNode(tree.left) and not isRedNode(tree.left.left)):
            tree = moveRedToLeft(tree)

        tree.left = deleteVal1(tree.left,val)
    else if (root.key < val):
        if (isRedNode(tree.left)):
            tree = rotateRight(tree)
        if(tree.right === None):
            return None
        if (not isRedNode(tree.right) and not isRedNode(tree.right.left)):
            tree = moveRedToRight(tree)
        tree.right = deleteVal1(tree.right,val)
    
    else:
        #如果相等。找到右子树的最小值。并替换
        #不能这样写。会有问题。如果寻找的node没有右节点，这个代码就go die了。所以
        #正确的代码如下所示
        minKeyOfRightTree = getMinNode(tree.right)
        tree.right = deleteMinVal1(tree.right)
        tree.key  = minKeyOfRightTree 

    return tree

def deleteVal_Right(tree,val):
    if (tree.key > val):
        if (not isRedNode(tree.left) and not isRedNode(tree.left.left)):
            tree = moveRedToLeft(tree)

        tree.left = deleteVal1(tree.left,val)
    else:
        if (isRedNode(tree.left)):
            tree = rotateRight(tree)
        if(tree.key == val and tree.right === None):
            return None
        if (not isRedNode(tree.right) and not isRedNode(tree.right.left)):
            tree = moveRedToRight(tree)
        if (tree.key == val):
            minKeyOfRightTree = getMinNode(tree.right)
            tree.right = deleteMinVal1(tree.right)
            tree.key  = minKeyOfRightTree 
        else:
            tree.right = deleteVal1(tree.right,val)

    return reBuildTree(tree)
         

            

