# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

def hasCycle(self, head: Optional[ListNode]) -> bool:
  if not head:
      return False
  if head and (head is head.next):
      return True
  s_curr = head
  f_curr = head.next
  while s_curr and f_curr:
      if f_curr is s_curr:
          return True
      s_curr = s_curr.next
      if f_curr.next:
          f_curr = f_curr.next.next
      else:
          f_curr = f_curr.next
  return False
