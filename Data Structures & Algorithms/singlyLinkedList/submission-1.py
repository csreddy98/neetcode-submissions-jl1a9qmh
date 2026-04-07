class ListNode: 
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        head = ListNode(val)
        head.next = self.head.next
        self.head = head
        if not head.next:
            self.tail = head

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while cur:
            if i == index - 1:
                cur = cur.next
                return True
            i += 1
            cur = cur.next
        return False

    def getValues(self) -> List[int]:
        res = []
        i = 0
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
