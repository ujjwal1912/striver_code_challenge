# Given an array of integers A and an integer B.
# Find the total number of subarrays having bitwise XOR of all elements equals to B.

def subarraysXor(arr, x):
    # Write your code here
    # Return an integer
    xr = 0
    d={}
    cnt=0
    for a in arr:
        xr^=a
        if xr==x:
            cnt+=1
        if xr^x in d:
            cnt+=d[xr^x]
        if xr in d:
            d[xr]+=1
        else:
            d[xr]=1
    return cnt
