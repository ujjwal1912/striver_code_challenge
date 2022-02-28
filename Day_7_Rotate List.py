# Given the head of a linked list, rotate the list to the right by k places.

def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    l = 0
    curr = head

    while curr:
        curr=curr.next
        l+=1
    if l==0:
        return head
    x = (l - k%l)%l
    if x==0:
        return head
    curr = head
    while x>0:
        curr = curr.next
        x-=1
    new_head = curr

    while curr.next:
        curr = curr.next
    curr.next = head

    while not head is new_head:
        prev = head
        head = head.next

    prev.next = None

    return new_head
