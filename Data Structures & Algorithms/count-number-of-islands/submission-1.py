class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noOfIslands = 0
        row, col = len(grid), len(grid[0])   
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()

        def bfs(row,col):
            visited.add((row,col))
            q.append((row,col))
            while q:
                row, col = q.popleft()
                print(row,col)
                for dx, dy in directions:
                    r,c = row + dx, col + dy
                    if (r >= 0 and r < len(grid) and (c >= 0 and c < len(grid[0])) and (r,c) not in visited and grid[r][c] == "1"):
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(row):
            for c in range(col):
                if ( grid[r][c] == "1" and (r,c) not in visited):
                    noOfIslands += 1
                    bfs(r,c)

        
                        

        return noOfIslands 

    

        
                    


        