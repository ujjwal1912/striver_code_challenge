# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

def merge(arr, l, m, r):
    n1, n2 = m-l+1, r-m
    L, R = [0]*n1, [0]*n2
    for i in range(n1):
        L[i] = arr[l+i]
    for i in range(n2):
        R[i] = arr[m+i+1]
    i, j, k = 0, 0, l
    cnt=0
    while i<n1 and j<n2:
        if L[i] <= 2*R[j]:
            i += 1
        else:
            cnt += n1-i
            j += 1
    i, j, k = 0, 0, l
    while i<n1 and j<n2:
        if L[i]>=R[j]:
            arr[k]=R[j]
            j+=1
            k+=1
        else:
            arr[k]=L[i]
            i+=1
            k+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1
    return cnt
def merge_sort(arr, l, r):
    cnt=0   
    if l<r:
        m=l+(r-l)//2
        cnt+=merge_sort(arr, l, m)
        cnt+=merge_sort(arr, m+1, r)
        cnt+=merge(arr, l, m, r)
    return cnt
