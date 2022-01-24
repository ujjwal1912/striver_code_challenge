# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
# O(n)
def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
                return 0
        hash_set = set(nums)
        maxi=0
        for num in hash_set:
            if num-1 not in hash_set:
                x=num
                cnt=1
                while x+1 in hash_set:
                    x+=1
                    cnt+=1
                maxi=max(maxi, cnt)
        return maxi

# O(nlog(n))
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
