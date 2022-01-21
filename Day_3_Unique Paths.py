# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# ans = (m+n-2) C (n-1)

from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x=m+n-2
        if m==1 or n==1:
            return 1
        return comb(x, m-1)
