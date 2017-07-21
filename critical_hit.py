def crit(d,h):
	number_over_h = (d-h)+1.0
	if not(h>d):#no crits needed
		return number_over_h/d
	else:#need those crits
		crit_chance = 1.0/d
		prob = 1.0
		remaining_health = h
		while remaining_health>d:
			prob = prob * crit_chance
			remaining_health = remaining_health - d
			number_over_h = (d-remaining_health)+1.0
		return (number_over_h/d)*prob

if __name__ == '__main__':
	print crit(4,1),1
	print crit(4,4),0.25
	print crit(4,5),0.25
	print crit(4,6),0.1875
	print crit(1,10),1
	print crit(100,200),0.0001
	print crit(8,20),0.009765625

#print 1*.25+2*.25+3*.25+5*(.25*.25)+6*(.25*.25)+7*(.25*.25)+9*(.25*.25*.25)+10*(.25*.25*.25)+10*(.25*.25*.25)

prob = 0.25
total = 0
i = 1
while i <1000:
	if i % 4 == 0:
		prob = prob * 0.25
		pass
	else:
		total += i*prob
	i = i + 1
print total