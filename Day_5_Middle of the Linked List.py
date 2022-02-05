# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if not head:
    return head
  l = 1
  curr=head
  while curr:
    l+=1
    curr=curr.next 
  l = (l+1)//2-1
  while l:
    l-=1
    head = head.next
  return head
