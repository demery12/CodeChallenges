matrix = [['1','2','3'],['4','5','6'],['7','8','9'],['.','0',None]]
def typing_dist(ip):
	prev_row=None
	prev_col=None
	dist = 0
	for char in ip:
		row = next((i for i, sublist in enumerate(matrix) if char in sublist), -1)
		column = matrix[row].index(char)
		if prev_row != None:
			dist += ((prev_row-row)**2 +(prev_col-column)**2)**0.5
		prev_row = row
		prev_col = column
	return str(round(dist,2))+'cm'

print typing_dist('219.45.143.143')