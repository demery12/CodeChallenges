import inflect
ie = inflect.engine()
def spend_exactly(amount,market,basket):
	#print amount,market,basket
	if amount == 0:
		return [basket]
	elif amount<0:
		return []
	elif len(market) == 0:
		return []
	else:
		#Do buy one!
	 	take = spend_exactly(amount - market[0][1],market,basket+[market[0]])
		#Don't buy one
		leave = spend_exactly(amount,market[1:],basket)

	 	return take + leave
	#print ans
#print spend_exactly(500,[('kiwi', 41), ('papaya', 254)],[]), "2"
#print spend_exactly(500,[('kiwi', 300), ('papaya', 200)],[])
#print spend_exactly(500,[('banana',32),('kiwi', 41) ,('mango', 97) ,('papaya', 254) ,('pineapple', 399)],[])

"""banana 32
,('kiwi' 41) ,('mango' 97) ,('papaya' 254) ,('pineapple' 399) """

def make_ouput(basket):
	basket_list = []
	for answer in basket:
		basket_dict = {}
		for item in answer:
			if item[0] not in basket_dict.keys():
				basket_dict[item[0]] = 1
			else:
				basket_dict[item[0]] += 1
		basket_list += [basket_dict]
	print "There are", len(basket_list),"answers:"
	for item in basket_list:
		out_str = "You could buy "
		out_list=[]
		for item2 in item:
			out_list += [str(item[item2]) + " " + ie.plural(item2,item[item2])]
		print"You could buy " + ', '.join(out_list)
def fruit_basket(fruits):
	"""
	Prepares input for other functions, manages all the calls, is what starts the call and makes the UI easy
	"""
	fruit_list = fruits.split('\n')
	fruit_input = []
	for fruit in fruit_list:
		fruit_input += [(fruit.split()[0],int(fruit.split()[1]))]
	make_ouput(spend_exactly(500,fruit_input,[]))


b1 = """banana 32
kiwi 41
mango 97
papaya 254
pineapple 399"""
fruit_basket(b1)

b2 = """apple 59
banana 32
coconut 155
grapefruit 128
jackfruit 1100
kiwi 41
lemon 70
mango 97
orange 73
papaya 254
pear 37
pineapple 399
watermelon 500"""
fruit_basket(b2)
#print answer_basket	