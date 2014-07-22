with open('words.txt') as f:
    content = f.read()

import copy

from Grid import Grid

class Solver(Grid):
	def __init__(self,height,width,grid=None):
		Grid.__init__(self,height,width)
		if grid is not None:
			i=1
			for line in grid:
				j=1
				for item in line:
					self.set_element(i,j,item)
					j+=1
			i+=1
	def solve(self):
		words=[]
		for row in range(self.get_row()):
			for col in range(self.get_col()):
				#now the code for bfs words
				word=''
				
				grid = [[0 for _ in range(self.get_row())] for _ in range(self.get_col())]
				grid[row][col]=1
				word=self.get_element(row+1,col+1)
				item=[row+1,col+1]
				print word,item,grid
				newwords=self.get_words(word,item,grid)
				words+=(newwords)
		newwords=[]
		for item in words:
			if len(item)>2 and '\n'+item+'\n' in content:
				newwords.append(item)
				#print item
		
		return newwords

	def get_words(self, word , currentitem,grid):
		rows=len(grid)
		cols=len(grid[0])
		words=[]
		if len(word)>5:
			words.append(word)
		neighbours=self.eight_neighbors(currentitem[0],currentitem[1])
		grid[currentitem[0]-1][currentitem[1]-1]=1

		for item in neighbours:
			if grid[item[0]-1][item[1]-1]==0:
				newgrid=copy.deepcopy(grid)
				if word in content:
					#if len(word)>4:
					#	print word
					words+=(self.get_words(word+self.get_element(item[0],item[1]),item,newgrid))
		return set(words)





grid=Solver(4,4)
item=[['l','t','n','e'],['u','a','s','g'],['o','s','a','n'],['s','h','i','a']]
for i in range(4):
	for j in range(4):
		grid.set_element(i+1,j+1,item[i][j])
#print str(grid)
#print grid.four_neighbors(1,1)
#print grid.eight_neighbors(1,1)
anwers = grid.solve()

for item in anwers:
	print item