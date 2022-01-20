# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, n-1
        while i>=0 and j>=0 and i<m and j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j-=1
            else:
                i+=1
        return False


# Method 2: Binary search
def bs(mat, l, r, t):
    if l<=r:
        mid=l+(r-l)//2
        m = len(mat)
        n = len(mat[0])
        i = mid//n if n!=0 else 0
        j = mid%n if n!=0 else 0
        # print(i, j, m, n)
        if i>m or j>n or i<0 or j<0:
            return -1
        if mat[i][j]==t:
            return i
        if mat[i][j]>t:
            return bs(mat, l, mid-1, t)
        return bs(mat, mid+1, r, t)
    else:
        return -1
class Solution:
   
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if bs(matrix, 0, len(matrix)*len(matrix[0])-1, target)==-1:
            return False
        return True
