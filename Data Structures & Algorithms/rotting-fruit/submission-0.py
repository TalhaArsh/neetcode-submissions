class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS - > QUEUE
        row,col = len(grid) , len(grid[0])
        totalFresh,totalTime = 0,0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    totalFresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        while q and totalFresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dx,dy in directions:
                    r , c = dx + row, dy + col
                    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    q.append([r,c])
                    totalFresh -= 1
            totalTime += 1


        if totalFresh != 0:
            return -1

        return  totalTime



        