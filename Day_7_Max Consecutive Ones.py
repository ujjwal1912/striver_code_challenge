# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    maxi=cnt=0
    for i in nums:
        if i==1: 
            cnt+=i
        else:
            maxi = max(cnt, maxi)
            cnt=0
    return max(maxi, cnt)
