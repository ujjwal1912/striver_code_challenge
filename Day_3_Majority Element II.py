# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<=2:
            return list(set(nums))
        me1, me2, cnt1, cnt2 = -1, -1, 0, 0
        for num in nums:
            if num == me1:
                cnt1+=1
            elif num == me2:
                cnt2+=1
            elif cnt1==0:
                me1 = num
                cnt1=1
            elif cnt2==0:
                me2 = num
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        n = len(nums)//3
        c1, c2 = 0, 0
        for num in nums:
            if num == me1:
                c1+=1
            elif num==me2:
                c2+=1
        ans=[]
        if c1>n:
            ans.append(me1)
        if c2>n:
            ans.append(me2)
        return ans
