# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
  l = 0
  curr = head
  while curr:
      l+=1
      curr=curr.next
  t = l//k
  curr = head
  first = curr
  x = k
  while x>1:
      x-=1
      first = first.next
  c=0
  while c<t:
      c+=1
      i = 0
      prev = curr
      while prev:
          prev = prev.next
          i+=1
          comp = 2*k-1 if c != t else k
          # print(i, comp, c, k)
          if i==comp:
              i=0
              break
      # print(c, prev)
      while i<k:
          i+=1
          next = curr.next
          curr.next = prev
          prev = curr
          curr = next

  return first
