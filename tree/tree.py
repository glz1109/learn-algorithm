from ast import NodeTransformer
from typing import List
from collections import deque

class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def create_binary_tree(arr: List[int]) -> TreeNode:
    n = len(arr)
    root = TreeNode(arr[0])
    queue = []
    queue.append(root)
    for i in range(n//2):
        print('node val', i, arr[i])
        node = queue.pop(0)
        if node :
            if arr[2*i+1]:
                node.left = TreeNode(arr[2*i+1])
            queue.append(node.left)
            
            if arr[2*i+2]:
                node.right = TreeNode(arr[2*i+2])
            queue.append(node.right)            
    return root

# 前序遍历二叉树 根左右
def preOrder(root: TreeNode):
    if root is None:
        return    
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

# 中序遍历二叉树 左根右 
# 对二叉查找树(排序树), 中序遍历可直接输出有序的数据序列
def inOrder(root: TreeNode):
    if root is None:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

# 后序遍历二叉树
def postOrder(root: TreeNode):
    if root is None:
        return
    inOrder(root.left)
    inOrder(root.right)
    print(root.val)

# 广度优先遍历 Breadth First Search
def BFS(root: TreeNode):
    if root is None:
        return []

    queue = deque()
    queue.append(root)
    res = []
    curlevel = 0
    while queue:
        level_size = len(queue)
        curlevel += 1 
        for _ in range(len(queue)):
            node = queue.popleft()
            res.append('%d-%d' % (curlevel, node.val))
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
    print(res)

# 深度优先遍历 Depth First Search
def DFS(root: TreeNode):
    res = []
    visit = set()
    _dfs(root, visit, res)

    print(res)

def _dfs(root: TreeNode, visit, res):
    if root is None:
        return

    res.append(root.val)
    visit.add(root)

    if not root.left in visit:
        _dfs(root.left, visit, res)
    if not root.right in visit:
        _dfs(root.right, visit, res)

# 深度优先搜索 非递归
def DFS_stack(root: TreeNode):
    if root is None:
        return
    
    visit = []
    stack = [root]

    while stack:
        node = stack.pop()
        visit.append(node)
        print('pop node', node.val)

        # print('loop visit:', visit)
        # print('loop stack:', stack)

        if node.right and not node.right in visit:
            stack.append(node.right)

        if node.left and not node.left in visit:
            stack.append(node.left)
    
    for node in visit:
        print('dfs end', node.val)

# 广度优先遍历， 按层打印节点
def LevelOrder(root: TreeNode):
    if not root:
        return []

    queue = deque()
    queue.append(root)
    res = []

    while queue:
        level = len(queue)
        curlevel = []
        for _ in range(len(queue)):
            node = queue.popleft()
            curlevel.append(node.val)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        res.append(curlevel)
    print(res)

if __name__ == '__main__':
    '''
                        13
                8               18
            6       10      16      20
          4   7   9    11

    '''
    
    # root = TreeNode(13)
    
    # second_1 = TreeNode(8)
    # second_2 = TreeNode(18)

    # third_1 = TreeNode(
    #     6)
    # third_2 = TreeNode(10)
    # third_3 = TreeNode(16)
    # third_4 = TreeNode(20)

    # fourth_1 = TreeNode(4)
    # fourth_2 = TreeNode(7)    
    # fourth_3 = TreeNode(9)
    # fourth_4 = TreeNode(11)

    # root.left, root.right = second_1, second_2
    # second_1.left, second_1.right = third_1, third_2
    # second_2.left, second_2.right = third_3, third_4

    # third_1.left, third_1.right = fourth_1, fourth_2
    # third_2.left, third_2.right = fourth_3, fourth_4
    
    # print('preOrder: ')
    # preOrder(root)

    # print('inOrder: ')
    # inOrder(root)

    # print('postOrder: ')
    # postOrder(root)

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(arr)
    root = create_binary_tree(arr)
    # preOrder(root)

    BFS(root)

    DFS(root)

    DFS_stack(root)