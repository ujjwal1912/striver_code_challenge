# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

def majorityElement(self, nums: List[int]) -> int:
        me, cnt = nums[0], 1
        for num in nums:
            if num==me:
                cnt+=1
            elif num!=me:
                cnt-=1
                if cnt==0:
                    me=num
                    cnt=1
        return me
