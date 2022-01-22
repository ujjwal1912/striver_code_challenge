# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans=[]
        for i in range(0, n):
            for j in range(i+1, n):
                t = target - nums[i] - nums[j]
                low, high = j+1, n-1
                while True:
                    if high<=low:
                        break
                    s=nums[low] + nums[high]
                    if s==t:
                        ans.append([nums[i], nums[j], nums[low], nums[high]])
                        high-=1
                    elif s>t:
                        high-=1
                    else:
                        low+=1
        fans=[]
        for x in ans:
            if x not in fans:
                fans.append(x)
        return fans
