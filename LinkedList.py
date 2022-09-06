'''
@@@@@@ Singly Linked List @@@@@@
total 14 +1

If we want to add a new value after a given node prev, we should: 
1. Initialize a new node cur with the given value
2. Link the "next" field of cur to prev's next node next
3. Link the "next" field of prev to cur
'''
# Design Linked List 
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return

        curr = self.head
        node_new = Node(val) #추가할 노드 생성
        #Addathead
        if index <= 0:
            node_new.next = curr #밀어내기
            self.head = node_new #자리안착
        else:
            for i in range(index-1):
                curr = curr.next
            node_new.next = curr.next # 밀어내서 자리만들기
            curr.next = node_new #자리 들어가기
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return

        curr = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.len -= 1

# Design Linked List (Better?)
class MyLinkedList(object):
    def __init__(self):
        self.linkedlist = list()

    def get(self, index):
        if index < 0 or index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]

    def addAtHead(self, val):
        self.linkedlist.insert(0, val)

    def addAtTail(self, val):
        self.linkedlist.append(val)

    def addAtIndex(self, index, val):
        if 0 <= index and index <= len(self.linkedlist):
            self.linkedlist.insert(index, val)

    def deleteAtIndex(self, index):
        if 0 <= index and index < len(self.linkedlist):
            self.linkedlist.pop(index)

'''
@@@@@@ Two Pointer Technique @@@@@@
What should be the proper speed for the two pointers?
It is a safe choice to move the slow pointer one step at a time while moving the fast pointer two steps at a time.

1. Always examine if the node is null before you call the next field.
2. Carefully define the end conditions of your loop.
'''
# Linked List Cycle
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        curr = head
        curr_fast = head.next
        
        while curr!=curr_fast:
            if curr_fast is None or curr_fast.next is None:
                return False
            curr = curr.next
            curr_fast = curr_fast.next.next
        
        return True

# Linked List Cycle (hash table)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        def dfs(head):
            if not head:
                return False
            if not head.next:
                return False
    
            visited = set()
            stack = list()
            stack.append(head)

            while(stack):
                curr = stack.pop()
                

                if not curr:
                    return False

                if curr in visited:
                    return True
                else:
                    visited.add(curr)
                    stack.append(curr.next)
        return dfs(head)

# Linked List Cycle II

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return
        seen = []
        curr = head
        while curr.next:
            seen.append(curr)
            if curr.next in seen:
                return curr.next
            curr = curr.next
        return

# Linked List Cycle II (faster)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None

        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow

# Intersection of Two Linked Lists

class Solution:
    def getIntersectionNode(self, headA, headB):
        dict = {}
        while headA:
            dict[headA]=1
            headA = headA.next
        while headB:
            if headB in dict:
                return headB
            headB = headB.next
        return None

# Intersection of Two Linked Lists (Better)
class Solution(object):
    def getIntersectionNode(self, headA, headB):      
        a, b = headA, headB
        while a != b:
            if a is None:
                a = headB
            else:
                a = a.next
            if b is None:
                b = headA
            else:
                b = b.next
        return a

# Remove Nth Node from End of List

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        while n:
            fast = fast.next
            n -= 1
        while fast != None:
            if fast.next is None:
                slow.next = slow.next.next
                return head
            fast = fast.next
            slow = slow.next
        head = slow.next
        return head

# Remove Nth Node from End of List (better)      
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        while n!=0:
            right = right.next
            n-=1
            
        if right==None:
            return head.next
        
        while right.next!=None:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return head

'''
@@@@@@ Classic Problems @@@@@@
'''

# Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        #자리는 그대로 두고 화살표 방향만 바꾼다는 개념
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next   
        head = prev
        return head
        
# Reverse Linked List (Little bit better)        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

# Remove Linked List Elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next= curr.next.next
            else:
                curr=curr.next
        if head and head.val == val:
            head = head.next 
        return head

# Remove Linked List Elements (faster?)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None,next=head)
        cur = head
        prev = dummy
        
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

# Odd Even Linked List
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        curr = head
        right_list_head = curr.next
        curr_right = right_list_head

        while curr.next and curr.next.next:
                curr.next = curr.next.next
                curr = curr.next
                curr_right.next = curr.next
                curr_right = curr_right.next

        curr.next = right_list_head
        return head

# Odd Even Linked List (little bit better)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            junction = head.next
            even,odd = head.next,head
            while odd.next != None and even.next:
                odd.next = odd.next.next
                odd = odd.next
                even.next = even.next.next
                even = even.next
            odd.next = junction
        return head

# Palindrome Linked List (need to study)
'''https://www.geeksforgeeks.org/python-program-to-check-if-a-singly-linked-list-is-palindrome/'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        # 초깃값은 모두 head에서 시작
        slow = fast = head
        # print('slow', slow) ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
        
        # 러너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            # 빠른 러너는 두 칸씩, 느린 러너는 한 칸씩 이동
            fast = fast.next.next
            # rev에 현재 slow, rev.next에 이전 rev를 넣어 역순 만듦, slow는 정방향으로 진행
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
        
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

'''
@@@@@@ Doubly Linked List @@@@@@
prev 추가
'''
# Doubly Linked List (Is this right?)
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return

        curr = self.head
        node_new = Node(val) #추가할 노드 생성
        
        if index <= 0:#Addathead
            node_new.next = curr #밀어내기
            self.head = node_new #자리안착
            if curr:
                curr.prev = node_new
        else:
            for i in range(index-1):
                curr = curr.next
            node_new.next = curr.next # 밀어내서 자리만들기 (curr랑 curr.next 사이에)
            node_new.prev = curr
            curr.next = node_new #자리 들어가기
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return

        curr = self.head
        if index == 0:
            curr = curr.next
            curr.prev = None
            self.head = self.head.next        
            
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.prev = curr #??
        self.len -= 1


'''
@@@@@@ Conclusion @@@@@@
If you need to add or delete a node frequently, a linked list could be a good choice.

If you need to access an element by index often, an array might be a better choice than a linked list.
'''
# Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        curr1, curr2 = list1, list2
        if curr1 != None and curr2 != None:
            while curr1:
                temp.append(curr1.val)
                curr1 = curr1.next
            while curr2:
                temp.append(curr2.val)
                curr2 = curr2.next
            
            temp.sort()
            head = ListNode(temp[0], None)
            curr = head
            for i in range(1, len(temp)):
                curr.next = ListNode(temp[i], None)
                curr = curr.next
            return head
        elif curr1 == None and curr2 != None:
            return list2
        elif curr1 != None and curr2 == None:
            return list1

# Merge Two Sorted Lists (Best)
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
# Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        n = curr1.val + curr2.val
        m = 0
        if n > 9:
            n -= 10
            m = 1
        curr1.val = n
        while curr1.next and curr2.next:
            curr1, curr2 = curr1.next, curr2.next
            n = curr1.val + curr2.val + m
            m = 0
            if n > 9:
                n -= 10
                m = 1
            curr1.val = n

        while curr1.next:
            curr1 = curr1.next
            n = curr1.val + m
            m = 0
            if n > 9:
                n -= 10
                m = 1
            curr1.val = n

        while curr2.next:
            curr2 = curr2.next
            curr1.next = curr2
            curr1 = curr1.next
            n = curr1.val + m
            m = 0
            if n > 9:
                n -= 10
                m = 1
            curr1.val = n
        if m:
            curr1.next = ListNode(m)
        return l1

# Flatten a Multilevel Doubly Linked List
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                nodenext = curr.next
                curr.next = curr.child #link
                curr.child.prev = curr #link
                curr.child = None #flatten
                curr = self.findchild(curr.next)
                if nodenext:
                    curr.next = nodenext
                    nodenext.prev = curr
            else:
                curr = curr.next           
        return head

    def findchild(self, curr):
        if curr.next is None:
            if curr.child:
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                curr = self.findchild(curr.next)
            else:
                return curr
        while curr.next:
            if curr.child:
                nodenext = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                curr = self.findchild(curr.next)
                curr.next = nodenext
                nodenext.prev = curr
            curr = curr.next
        return curr

# Flatten a Multilevel Doubly Linked List (Other)
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # dummy = Node(0, None, head, None )
        
        cur = head
        while cur:
                        
            if cur.child:
                curNext = cur.next if cur.next else None
                temp = cur.child
                cur.next, temp.prev = temp, cur
                while temp.next:
                    temp = temp.next
                temp.next = curNext
                if curNext: curNext.prev = temp
                cur.child = None
            else:
                cur = cur.next
                # if cur.next else None
            
        return head

# Flatten a Multilevel Doubly Linked List (Best)
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        prehead = Node(None,None,head,None)
        head.prev = prehead
        p=prehead
        stack = []
        stack.append(head)
        while stack:
            cur=stack.pop()
            cur.prev=p
            p.next=cur
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child=None
            p=cur
            
        head.prev=None
        return head

#Copy List with Random Pointer



#Rotate List
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        if curr is None:
            return
        len = 1
        while curr.next:
            curr = curr.next
            len += 1
        if k > len:
            k = k % len
        elif k == len:
            return head
      
        while k:
            curr = head
            while curr.next:
                if curr.next.next is None: #this part takes time. need to be fixed
                    temp = curr
                    curr = curr.next
                    curr.next = head
                    head = curr
                    temp.next = None
                    break
                curr = curr.next
            k -= 1
        return head

#Rotate List (better)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        n = 1
        node = head
        while node.next:
            n += 1
            node = node.next
        node.next = head # make a cycle
        
        k = k%n
        k = n-k
        node = head
        
        while k-1:
            head = head.next
            k -= 1
        res = head.next
        head.next = None
        
        return res