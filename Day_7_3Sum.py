# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(self, nums: List[int]) -> List[List[int]]:
    l = len(nums)
    ans=[]
    hash={}
    nums.sort()
    for i in range(l):
        hash[nums[i]] = i
    for i in range(l):
        if i!= 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, l):
            if j!= i+1 and nums[j] == nums[j-1]:
                continue
            c = -(nums[i]+nums[j])
            if (c in hash) and hash[c]>j:
                ans.append([nums[i], nums[j], c])
    return ans
