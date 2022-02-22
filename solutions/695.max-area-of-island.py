#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from copy import deepcopy
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        tmp=deepcopy(grid)
        h,w=len(grid),len(grid[0])
        def bfs(pi,pj):
            if not (0<=pi<h and 0<=pj<w and tmp[pi][pj]):return 0
            tmp[pi][pj]=0
            return 1+bfs(pi-1,pj)+bfs(pi+1,pj)+bfs(pi,pj-1)+bfs(pi,pj+1)
        return max(bfs(i,j) for i in range(h) for j in range(w))
# @lc code=end

