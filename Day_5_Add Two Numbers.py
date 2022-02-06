# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  num = 0
  carry = 0
  ans = ListNode(val=None)
  fi = ans
  while l1 and l2:
      added = l1.val + l2.val + carry
      num = added % 10
      carry = added//10
      ans.next = ListNode(val=num)
      ans = ans.next
      l1 = l1.next
      l2 = l2.next
  while l1:
      added = l1.val + carry
      num = added % 10
      carry = added//10
      ans.next = ListNode(val=num)
      ans = ans.next
      l1 = l1.next
  while l2:
      added = l2.val + carry
      num = added % 10
      carry = added//10
      ans.next = ListNode(val=num)
      ans = ans.next
      l2 = l2.next 
  if carry:
      carry = added//10
      ans.next = ListNode(val=carry)
      ans = ans.next
  return fi.next
