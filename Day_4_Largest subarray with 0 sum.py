# Given an array having both positive and negative integers. 
# The task is to compute the length of the largest subarray with sum 0.

def maxLen(self, n, arr):
        #Code here
        dic = {}
        s, maxi=0, 0
        
        for i, v in enumerate(arr):
            s +=v
            if s==0:
                maxi=i+1
                continue
            if s in dic:
                maxi=max(maxi, (i-dic[s]))
            else:
                dic[s]=i
            
        return maxi
