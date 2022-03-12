# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

def removeDuplicates(self, nums: List[int]) -> int:
    x=1
    for i in range(len(nums)-1):
        if(nums[i]!=nums[i+1]):
            nums[x] = nums[i+1]
            x+=1
    return x
