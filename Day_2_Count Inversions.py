# Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).

# What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].

def merge(arr, l, m, r):
    n1, n2, cnt = m-l+1, r-m, 0
    L, R = [0]*n1, [0]*n2
    for i in range(n1):
        L[i] = arr[l+i]
    for i in range(n2):
        R[i] = arr[m+1+i]
    i, j, k = 0, 0, l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
            k+=1
        else:
            arr[k]=R[j]
            j+=1
            k+=1
#             print(i, j, k, m, m-i+1)
            cnt+=(n1-i)
    while i<n1:
        arr[k] = L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k] = R[j]
        j+=1
        k+=1
    return cnt
    
def merge_sort(arr, l, r):
    cnt=0
    if l<r:
        m=l+(r-l)//2
        cnt += merge_sort(arr, l, m)
        cnt += merge_sort(arr, m+1, r)
        cnt += merge(arr, l, m, r)
    return cnt
