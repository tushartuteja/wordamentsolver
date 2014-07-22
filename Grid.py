class Grid():
    def __init__(self,height,width):
        self._grid_height=height
        self._grid_width=width
        self._grid=[['' for _ in range(height)] for _ in range(width)]
    def get_row(self):
        return self._grid_height
    def get_col(self):
        return self._grid_width
    def get_element(self,row,col):
        return self._grid[row-1][col-1]
    def set_element(self,row,col,value):
        self._grid[row-1][col-1]=value

    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        """
        ans = []
        if row > 1:
            ans.append((row - 1, col))
        if row < self._grid_height:
            ans.append((row + 1, col))
        if col > 1:
            ans.append((row, col - 1))
        if col < self._grid_width:
            ans.append((row, col + 1))
        return ans

    def eight_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []
        if row > 1:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 1:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        if (row > 1) and (col > 1):
            ans.append((row - 1, col - 1))
        if (row > 1) and (col < self._grid_width):
            ans.append((row - 1, col + 1))
        if (row < self._grid_height ) and (col > 1):
            ans.append((row + 1, col - 1))
        if (row < self._grid_height ) and (col < self._grid_width):
            ans.append((row + 1, col + 1))
        return ans

    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = ""
        for row in range(self._grid_height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans


#test suit
grid=Grid(3,3)
grid.set_element(1,1,'a')
grid.set_element(1,2,'b')
grid.set_element(1,3,'c')
grid.set_element(2,1,'d')
grid.set_element(2,2,'e')
grid.set_element(2,3,'f')
grid.set_element(3,1,'g')
grid.set_element(3,2,'h')
grid.set_element(3,3,'i')

print str(grid)
print grid.four_neighbors(1,1)
print grid.eight_neighbors(1,1)
