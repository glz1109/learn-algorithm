
from collections import deque


class TreeNode():
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def find(self, value: int):
        node = self.root
        while node and node.val != value:
            node = node.left if node.val > value else node.right
        return node
    
    def insert(self, value:int):
        if not self.root:
            self.root = TreeNode(value)
            return

        node = self.root
        parent = None
        while node : 
            parent = node
            node = node.left if node.val > value else node.right
        
        insert_node = TreeNode(value)
        if parent.val > value:
            parent.left = insert_node        
        else:
            parent.right = insert_node
    
    def delete(self, value:int):
        '''
        删除操作
        1. 如果要删除的节点没有子节点，只需直接将父节点中指向要删除节点的指针置为null。
        2. 如果要删除的节点只有一个子节点（只有左子节点或者右子节点），只需更新父节点中指向要删除节点的指针，
           让它指向要删除节点的子节点就可以了。
        3. 第三种情况是，如果要删除的节点有两个子节点。
           需要找到这个节点的右子树中的最小节点，把它替换到要删除的节点上。
           然后再删除掉这个最小节点，因为最小节点肯定没有左子节点（如果有左子结点，那就不是最小节点了），
           所以，可以应用上面两条规则来删除这个最小节点。
        '''
        del_node = self.root
        del_node_parent = None
        while del_node and del_node.val != value:
            del_node_parent = del_node
            del_node = del_node.left if del_node.val > value else del_node.right
        
        if not del_node:
            return
        
        if del_node.left and del_node.right:
            replace_node = del_node.right
            replace_node_parent = del_node    

            while replace_node.left:
                replace_node_parent = replace_node
                replace_node = replace_node.left

            # 节点的右子树中的最小节点，替换到要删除的节点上，赋值即可
            del_node.val = replace_node.val
          
            # 要删除的节点变为
            del_node_parent, del_node = replace_node_parent, replace_node
          
            child = del_node.left if del_node.left else del_node.right
            
            # 删除节点是叶子节点或者仅有一个子节点
            if not del_node_parent:
                self.root = child
            elif del_node_parent.left == del_node:
                del_node_parent.left = child
            else:
                del_node_parent.right = child

    # 广度优先遍历， 按层打印节点
    def level_order(self):
        if not self.root:
            return []

        queue = deque()
        queue.append(self.root)
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


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(33)
  
    bst.insert(16)    
    bst.insert(13) 
    bst.insert(18) 
    bst.insert(15)
    bst.insert(17)    
    bst.insert(25)
    bst.insert(19)
    bst.insert(27)    
   
    bst.insert(50)
    bst.insert(34)    
    bst.insert(58)        
    bst.insert(51)        
    bst.insert(66)    
    bst.insert(55)

    bst.level_order()

    # bst.delete(13)
    # print('after delete 13')
    # bst.level_order()

    bst.delete(18)
    print('after delete 18')
    bst.level_order()

    # bst.delete(55)
    # print('after delete 55')
    # bst.level_order()

    # print(bst.find(99))

