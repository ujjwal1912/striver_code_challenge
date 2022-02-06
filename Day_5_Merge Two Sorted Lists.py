# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  if not list1:
      return list2
  elif not list2:
      return list1

  if list1.val <= list2.val:
      ans = list1
      list1 = list1.next
  else:
      ans = list2
      list2 = list2.next
  first = ans
  while list1 and list2:
      if list1.val <= list2.val:
          ans.next = list1
          ans = ans.next
          list1 = list1.next
      else:
          ans.next = list2
          ans = ans.next
          list2 = list2.next

  while list1:
      ans.next = list1
      ans = ans.next
      list1 = list1.next
  while list2:
      ans.next = list2
      ans = ans.next
      list2 = list2.next

  return first
