# Definition for singly-linked list.
# from gettext import lngettext
# from pandas.tseries.offsets import Second

# from requests.api import head

from LinkedList import ListNode, SingleLinkedList
from os import fspath


class Solution:
    # 链表翻转
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:            
            # tmp = cur.next
            # cur.next = pre 
            # pre = cur
            # cur = tmp
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def swapPairs_my(self, head: ListNode) -> ListNode:
        first, pre = head, self
        phead = head.next
        while first and first.next:
            second = first.next
            pre.next = second
            third = second.next
            second.next = first
            first.next = third
        
            pre = first
            first = third
        return phead

    '''
    “链表交换相邻元素”中 self 是怎么回事。
    ------
    1. 首先看到最后 return self.next ，可以看到作者是想把 self 当做链表的头指针使用的
      （注意：头指针 pHead 与传入的参数 head 是不同的，head 是第一个结点，而 pHead.next == next ）。
      用头指针有什么好处呢？因为我们让头指针的 next 域（pHead.next）永远指向第一个结点，就是避免最后返回的时候找不到第一个结点了。
    2. 那么作者为什么可以 pre, pre.next = self, head 这样写呢？
      因为 self 是这个类的一个对象，所以在类定义的时候可以在任何地方，给 self 增加新的属性。
      相信大家都知道在 __init__(self, attr) 里面可以定义通过 self.myattr = attr 来定义一个 myattr 属性。
      其实这个语句写在任意一个类的方法里都可以，所以在原文 swapPairs() 里面当然也可以定义新的属性。
      所以这行代码应该理解为，pre 指向 self（虽然 self 不是一个 ListNode 类型的对象，但它只要有一个 next 就可以了），
      同时为 pre（同时也是为 self，它们是一样的现在）增加一个 next 属性，这个 next 属性指向第一个结点 head。
    3. 明白上面之后，这里就好办了。
       在第一次 while 循环的时候，pre.next 被赋值为 b（也就是原来第二个结点，转换为变成了第一个，也就成为了新链表的第一个结点。
       如果原来是[1,2,3,4]，那么现在就是[2,1,3,4]，这个 self.next 就是指向 2 这个结点）。
       所以最后只要返回 self.next 就得到了答案。
    ------

    其实换个写法大家就好理解很多了：
    pHead = ListNode(None)
    pre, pre.next = pHead, head
    也就是说不用 self 也可以，只是原作者秀了一把小技巧而已。
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    '''
    19. 删除链表的倒数第N个节点
        给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
        示例：
            给定一个链表: 1->2->3->4->5, 和 n = 2.
            当删除了倒数第二个节点后，链表变为 1->2->3->5.
        说明：
            给定的 n 保证是有效的
        进阶：
            你能尝试使用一趟扫描实现吗？
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        
        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)            
        dummy.next = None
        l3 = dummy
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        
        if l2:
            l3.next = l2
        
        return dummy.next

if __name__ == '__main__':
    test_list = SingleLinkedList()
   
    for i in range(1, 2):
        test_list.append(i)
    
    head = test_list.head

    opt_list = Solution()

    # ret_head = opt_list.removeNthFromEnd(head, 1)

    # ret_head = opt_list.reverseList(head)
  
    # ret_head = opt_list.swapPairs(head)

    l1 = SingleLinkedList()
    l2 = SingleLinkedList()
  
    l1.append(1)
    l1.append(2)
    l1.append(3)
    
    l2.append(1)
    l2.append(3)
    l2.append(3)

    ret_head = opt_list.mergeTwoLists(l1.head, l2.head)

    cur = ret_head
    while cur:
        print(cur.val)
        cur = cur.next



  