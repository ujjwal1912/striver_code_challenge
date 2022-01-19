l=0
r=len(nums)
t=target
def bst(l, r, nums, t):
  if l<=r:
    m=l+(r-l)//2
    if nums[m]==t:
      return m
    if nums[m]>t:
      return self.bst(l, m-1, nums, t)
    else:
      return self.bst(m+1, r, nums, t)
  else:
    return -1
