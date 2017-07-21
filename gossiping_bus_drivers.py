class driver:
	def __init__(self,route,driver_number):
		self.route = route.split() #might put this in a list here
		self.driver_number = driver_number
		self.gossips = [driver_number]
		self.stop = self.route[0]
		self.stop_position = 0
		self.minute = 1
	def __repr__(self):
		return "Driver " + str(self.driver_number) + " with route: "+ str(self.route)
	def advance(self):
		if self.stop_position == len(self.route) - 1:
			self.stop_position = 0
		else:
			self.stop_position += 1
		self.stop = self.route[self.stop_position]
		self.minute +=1



def gossip_exchange(routes):
	'''
	Finds the number of stops it takes to get all gossips
	'''
	index = 0
	driver_dict = {}
	has_all_gossip = []
	#set up all the drivers
	for route in routes.split('\n'):
		driver_dict['driver_'+str(index)]=driver(route,index)
		index += 1
	other_index = 0
	while driver_dict['driver_0'].minute<481:
		stop_dict={}
		for zdriver in driver_dict.values():
			if zdriver.stop in stop_dict.keys():
				stop_dict[zdriver.stop] = stop_dict[zdriver.stop] + [zdriver]
			else:
				stop_dict[zdriver.stop] = [zdriver]
			zdriver.advance()
		for driver_list in stop_dict.values():
			if len(driver_list)==1:
				continue
			else:
				shared = list({x for y in driver_list for x in y.gossips })
				for zdriver in driver_list:
					zdriver.gossips = shared
					if len(shared) == index:
						has_all_gossip += [zdriver]
						has_all_gossip = list(set(has_all_gossip))
						if len(has_all_gossip) == index:
							return other_index
		other_index += 1
	return "NEVER"



r1 = """3 1 2 3
3 2 3 1 
4 2 3 4 5"""
print gossip_exchange(r1)

r2="""2 1 2
5 2 8"""
print gossip_exchange(r2)


r3="""7 11 2 2 4 8 2 2
3 0 11 8
5 11 8 10 3 11
5 9 2 5 0 3
7 4 8 2 8 1 0 5
3 6 8 9
4 2 11 3 3"""
print gossip_exchange(r3)

r4="""12 23 15 2 8 20 21 3 23 3 27 20 0
21 14 8 20 10 0 23 3 24 23 0 19 14 12 10 9 12 12 11 6 27 5
8 18 27 10 11 22 29 23 14
13 7 14 1 9 14 16 12 0 10 13 19 16 17
24 25 21 4 6 19 1 3 26 11 22 28 14 14 27 7 20 8 7 4 1 8 10 18 21
13 20 26 22 6 5 6 23 26 2 21 16 26 24
6 7 17 2 22 23 21
23 14 22 28 10 23 7 21 3 20 24 23 8 8 21 13 15 6 9 17 27 17 13 14
23 13 1 15 5 16 7 26 22 29 17 3 14 16 16 18 6 10 3 14 10 17 27 25
25 28 5 21 8 10 27 21 23 28 7 20 6 6 9 29 27 26 24 3 12 10 21 10 12 17
26 22 26 13 10 19 3 15 2 3 25 29 25 19 19 24 1 26 22 10 17 19 28 11 22 2 13
8 4 25 15 20 9 11 3 19
24 29 4 17 2 0 8 19 11 28 13 4 16 5 15 25 16 5 6 1 0 19 7 4 6
16 25 15 17 20 27 1 11 1 18 14 23 27 25 26 17 1"""
print gossip_exchange(r4)