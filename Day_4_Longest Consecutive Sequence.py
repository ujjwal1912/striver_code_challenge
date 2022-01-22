# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxi, cnt=0, 1
        if len(nums)<1: return 0
        prev=nums[0]
        for i, num in enumerate(nums):
            if num==prev+1:
                cnt+=1
            elif num==prev:
                continue
            else:
                maxi = cnt if maxi<cnt else maxi
                cnt=1
            prev=num
                
        if cnt>maxi:
            maxi=cnt
        return maxi
