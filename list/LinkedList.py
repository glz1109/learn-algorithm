# --*-- utf-8 --*--

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def getItem(self):
    #     return self.val

    # def getNext(self):
    #     return self.next

    # def setItem(self,newitem):
    #     self.val=newitem

    # def setNext(self,newnext):
    #     self.next=newnext

class SingleLinkedList():  
    def __init__(self):
        self.head = None  #初始化为空链表

    def isEmpty(self):
        return self.head == None
        
    def size(self):
        cur=self.head
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        cur=self.head
        while cur:
            print(cur.val)
            cur = cur.next
    
    def add(self,val):
        temp=ListNode(val)
        temp.setNext(self.head)
        self.head = temp
 
    def append(self,val):
        temp = ListNode(val)
        if self.isEmpty():
            self.head = temp   #若为空表，将添加的元素设为第一个元素
        else:
            cur=self.head
            while cur.next:
                cur = cur.next   #遍历链表
            cur.next = temp   #此时cur为链表最后的元素

    def search(self,val):
        cur = self.head
        founditem = False
        while cur and not founditem:
            if cur.val == val:
                founditem = True
            else:
                cur = cur.next
        return founditem

    def index(self,val):
        cur=self.head
        count=0
        found=None
        while cur and not found:
            count+=1
            if cur.val == val:
                found = True
            else:
                cur = cur.next
        if found:
            return count
        else:
            raise ValueError('%s is not in linkedlist'%val)
    
    def remove(self,val):
        cur = self.head
        pre = None
        while cur:
            if cur.val == val:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next                       
    
    def insert(self,pos,val):
        if pos<=1:
            self.add(val)
        elif pos>self.size():
            self.append(val)
        else:
            temp = ListNode(val)
            count = 1
            pre = None
            cur = self.head
            while count<pos:
                count += 1
                pre = cur
                cur = cur.next
            pre.next = temp
            temp.next = cur
