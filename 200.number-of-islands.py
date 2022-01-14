#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    ans+=1
                    q=deque([(i,j)])
                    grid[i][j]="0"
                    while q:
                        pi,pj=q.popleft()
                        d=[(0,1),(0,-1),(1,0),(-1,0)]
                        for di,dj in d:
                            ni,nj=pi+di,pj+dj
                            if 0<=ni<m and 0<=nj<n and grid[ni][nj]=="1":
                                q.append((ni,nj))
                                grid[ni][nj]="0"
        return ans


# @lc code=end

[["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]]