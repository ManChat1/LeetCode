class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        maxLocal = []
        for i in range (0, n - 2):
            maxim = []
            for j in range (0, n - 2):
                l1 = max(grid[i][j : j + 3])
                l2 = max(grid[i + 1][j : j + 3])
                l3 = max(grid[i + 2][j : j + 3])
                max_ = max(l1, l2, l3)
                maxim.append(max_)
            maxLocal.append(maxim)
        return maxLocal