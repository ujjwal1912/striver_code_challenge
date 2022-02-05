# Given the head of a singly linked list, reverse the list, and return the reversed list.

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if not head:
    return head
  rev = ListNode(val=head.val)
  curr = head
  while curr.next:
    curr = curr.next
    temp = ListNode(curr.val)
    temp.next = rev
    rev = temp
  return rev
