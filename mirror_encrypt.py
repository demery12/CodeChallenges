def arrayify(text):
	line_list=[]
	line = []
	for char in text:
		if char == '\n':
			line_list += [line]
			line = []
		else:
			line += [char]
	line_list += [line]
	return line_list

def check(grid,position,direction):
	if grid[position[0]][position[1]] == "/":
		if direction == 'right':
		 	return walk(grid,position,'up')
		elif direction == 'left':
			return walk(grid,position,'down')
		elif direction == 'up':
			return walk(grid,position,'right')
		elif direction == 'down':
			return walk(grid,position,'left')
	elif grid[position[0]][position[1]] == "\\":
		if direction == 'right':
		 	return walk(grid,position,'down')
		elif direction == 'left':
			return walk(grid,position,'up')
		elif direction == 'up':
			return walk(grid,position,'left')
		elif direction == 'down':
			return walk(grid,position,'right')
	else:
		return walk(grid,position,direction)
def walk(grid,position,direction):
	if direction == 'right':
		if position[1]+1 == 13:
			return [position[0],position[1]+1]
	 	position = [position[0],position[1]+1]
	elif direction == 'left':
		if position[1]-1 == -1:
			return [position[0],position[1]-1]
		position = [position[0],position[1]-1]
	elif direction == 'up':
		if position[0] - 1 == -1:
			return [position[0] - 1,position[1]]
		position = [position[0] - 1,position[1]]
	elif direction == 'down':
		if position[0] + 1 == 13:
			return [position[0] + 1,position[1]]
		position = [position[0] + 1,position[1]]
	return check(grid,position,direction)

def mirror_encrypt(grid,word):
	grid = arrayify(grid)
	locations = {'A': [0, -1], 'C': [2, -1], 'B': [1, -1], 'E': [4, -1], 'D': [3, -1], 'G': [6, -1], 'F': [5, -1], 'I': [8, -1], 'H': [7, -1], 'K': [10, -1], 'J': [9, -1], 'M': [12, -1], 'L': [11, -1], 'O': [13, 1], 'N': [13, 0], 'Q': [13, 3], 'P': [13, 2], 'S': [13, 5], 'R': [13, 4], 'U': [13, 7], 'T': [13, 6], 'W': [13, 9], 'V': [13, 8], 'Y': [13, 11], 'X': [13, 10], 'Z': [13, 12], 'a': [-1, 0], 'c': [-1, 2], 'b': [-1, 1], 'e': [-1, 4], 'd': [-1, 3], 'g': [-1, 6], 'f': [-1, 5], 'i': [-1, 8], 'h': [-1, 7], 'k': [-1, 10], 'j': [-1, 9], 'm': [-1, 12], 'l': [-1, 11], 'o': [1, 13], 'n': [0, 13], 'q': [3, 13], 'p': [2, 13], 's': [5, 13], 'r': [4, 13], 'u': [7, 13], 't': [6, 13], 'w': [9, 13], 'v': [8, 13], 'y': [11, 13], 'x': [10, 13], 'z': [12, 13]}

	ivd = {str(value):key for key, value  in locations.items()}

	decrypt = ""
	ans = {}
	for char in word:
		if char not in locations.keys():
			print char
			decrypt += char
		elif char in ans.keys():
			decrypt += ans[char]
		else:
			position = locations[char]
			if position[1] == -1:
				endkey = walk(grid,position,'right')
				ans[char]=ivd[str(endkey)]
				decrypt += ivd[str(endkey)]
			elif position[1] == 13:
				endkey = walk(grid,position,'left')
				ans[char]=ivd[str(endkey)]
				decrypt += ivd[str(endkey)]
			elif position[0] == -1:
				endkey = walk(grid,position,'down')
				ans[char]=ivd[str(endkey)]
				decrypt += ivd[str(endkey)]
			elif position[0] == 13:
				endkey = walk(grid,position,'up')
				ans[char]=ivd[str(endkey)]
				decrypt += ivd[str(endkey)]
	print ans
	return decrypt

#Don't actually use this, but it is this in a text file
the_grid = """   \\  /\    
            \
   /         
      \     \
    \        
  /      /   
\  /      \  
     \       
\/           
/            
          \  
    \/       
   /       / """

with open('grid_for_mirror_encrypt.txt', 'r') as f:
	the_grid = f.read()
print mirror_encrypt(the_grid,"TpnQSjdmZdpoohd")



#Makes a dict of letters and there 'location'
#I am just copy and pasting it in
letter_list="A,B,C,D,E,F,G,H,I,J,K,L,M".split(',')
i=0
dicti={}
for char in letter_list:
	dicti[char]=[i,-1]
	i+=1
letter_list2="N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(',')
i=0
for char in letter_list2:
	dicti[char]=[13,i]
	i+=1
letter_list2="N,O,P,Q,R,S,T,U,V,W,X,Y,Z".lower().split(',')
i=0
for char in letter_list2:
	dicti[char]=[i,13]
	i+=1
letter_list="A,B,C,D,E,F,G,H,I,J,K,L,M".lower().split(',')
i=0
for char in letter_list:
	dicti[char]=[-1,i]
	i+=1
#Uncomment below if you want the list
#print dicti
