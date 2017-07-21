def game_of_threes(number):
	if number == 1:
		return ''
	elif number%3 == 0:
		return str(number) + ' 0\n' + game_of_threes(number/3)
	elif number%3 == 1:
		return str(number) + ' -1\n' + game_of_threes((number-1)/3)
	else:
		return str(number) + ' 1\n' + game_of_threes((number+1)/3)
print game_of_threes(100)
print game_of_threes(31337357)