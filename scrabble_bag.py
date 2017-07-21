import sys
class bag: 
	def __init__(self):
		self.contents = {"A":9 ,"B":2 ,"C":2 ,"D":4 ,"E":12 ,"F":2 ,"G":3 ,"H":2 ,"I":9 ,"J":1 ,"K":1 ,"L":4 ,"M":2 ,"N":6 ,"O":8 ,"P":2 ,"Q":1 ,"R":6 ,"S":4 ,"T":6 ,"U":4 ,"V":2 ,"W":2 ,"X":1 ,"Y":2 ,"Z":1,"_":2}
		self.reverse_contents = {val:key for key,val in self.contents.items()}
		self.A=9
		self.B=2
		self.C=2
		self.D=4
		self.E=12
		self.F=2
		self.G=3
		self.H=2
		self.I=9
		self.J=1
		self.K=1
		self.L=4
		self.M=2
		self.N=6
		self.O=8
		self.P=2
		self.Q=1
		self.R=6
		self.S=4
		self.T=6
		self.U=4
		self.V=2
		self.W=2
		self.X=1
		self.Y=2
		self.Z=1
	def remove(self,str_to_remove):
		for char in str_to_remove:
			if self.contents[char] == 0:
				print "Trying to remove more",char,"'s then there are!"
				print "Skipping this one"
				continue
			self.contents[char] = self.contents[char] - 1
	def show(self):
		show_list=[]
		for key in self.contents.keys():
			val = self.contents[key]
			if val not in [item[0] for item in show_list]:
				show_list += [[val,[key]]]
			else:
				index = 0
				for item in show_list:
					if item[0]==val:
						show_list[index][1] += [key]
					else:
						index += 1
		nice_printout = ""
		for val in sorted(show_list,key=lambda num: num[0])[::-1]:
			letter_string = ""
			for letter in val[1]:
				letter_string += letter+","
			letter_string = letter_string[:-1]
			nice_printout += str(val[0]) + ': ' +letter_string+"\n"
		return nice_printout

#mybag = bag()
#mybag.remove("DDDE")
#print mybag.contents


if __name__ == '__main__':
	if len(sys.argv)==2 and type(sys.argv[1])==type("string"):
		mybag = bag()
		mybag.remove(sys.argv[1])
		print mybag.show()
	else:
		print "Invalid arguments"
		print "Please pass string of letters"
