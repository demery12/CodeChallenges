# Enter your code here. Read input from STDIN. Print output to STDOUT
from decimal import *
import itertools
print "DONING"
n=raw_input()
p=raw_input().strip().split(' ')
#list of all ways to sort
all_sort = [i for i in itertools.permutations(p)]
prob = 1.0/len(all_sort)
#list of all ways to sort the list
all_sorted = [z for z in all_sort if list(z)==sorted(p)]
prob_sorted = len(all_sorted)*prob
print prob_sorted
#print all_sort,len(all_sort)
#print all_sorted
i = 1
zsum=0.000000
while i<3001:
    zsum += i*((1-prob_sorted)**(i-1)*prob_sorted)
    i+=1
getcontext().prec = 10
SIXPLACES = Decimal(10) ** -6
print Decimal(str(zsum)).quantize(SIXPLACES)
'''

#mul=lambda x,y:x*y
#def nCk(n,k): 
#  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )
count_dict = {}
print "TING"
for i in sorted(p):
    if i not in count_dict.keys():
        count_dict[i]=1
    else:
        count_dict[i]+=1
#print count_dict
for key in count_dict:
    #print count_dict[key]*[0]
    for i in itertools.permutations(count_dict[key]*[0]):
        pass
        # print i, "yth"
    #print [i for i in itertools.permutations(count_dict[key]*[0])]
    count_dict[key]= len([i for i in itertools.permutations(count_dict[key]*[0]) if i != ()])

#print count_dict
#print len([i for i in itertools.permutations(int(n)*[0])]), sum(count_dict.values())
reduce(lambda x, y: x*y, [1,2,3,4,5,6])
prob = reduce(lambda x, y: x*y, count_dict.values())/(len([i for i in itertools.permutations(int(n)*[0])])+0.0)
print prob
i = 0
zsum=0.000000
while i<3001:
    zsum += prob**i
    i+=1
getcontext().prec = 10
SIXPLACES = Decimal(10) ** -6
print zsum
print Decimal(str(zsum)).quantize(SIXPLACES)
#10
#1 1 1 1 2 2 2 3 3 3
'''





#passes more cases
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from decimal import *
import itertools
import math
n=raw_input()
p=raw_input().strip().split(' ')
def time_takes(p):
    if p == sorted(p):
        print '0.000000'
        return
    #list of all ways to sort
    #all_sort = [i for i in itertools.permutations(p)]
    #prob = 1.0/len(all_sort)
    #print len(all_sort)
    #print math.factorial(len(p))
    prob = 1.0/math.factorial(len(p)+0.000)

    count_dict = {}
    for i in p:
        if i not in count_dict.keys():
            count_dict[i]=1
        else:
            count_dict[i]+=1

    for key in count_dict:
        count_dict[key]= math.factorial(count_dict[key])

    number_of_ways_to_sort = 1
    for val in count_dict.values():
        number_of_ways_to_sort += (val-1)
    prob_sorted = number_of_ways_to_sort*prob
    x = math.factorial(len(set(p)))
    '''i = 1
    zsum=0.000000
    zsum_old= 50
    while i<99000001 and abs(zsum_old-zsum)>0.0000000001:
        zsum_old = zsum
        zsum += i*((1-prob_sorted)**(i-1)*prob_sorted)
        i+=1
    '''
    getcontext().prec = 1000
    SIXPLACES = Decimal(10) ** -6
    print Decimal(x).quantize(SIXPLACES)
    #print Decimal(1.0/prob_sorted).quantize(SIXPLACES)

    '''
    #list of all ways to sort the list
    all_sorted = [z for z in all_sort if list(z)==sorted(p)]
    prob_sorted = len(all_sorted)*prob
    print prob_sorted
    #print all_sort,len(all_sort)
    #print all_sorted

    i = 1
    zsum=0.000000
    while i<3001:
        zsum += i*((1-prob_sorted)**(i-1)*prob_sorted)
        i+=1
    getcontext().prec = 10
    SIXPLACES = Decimal(10) ** -6
    print Decimal(str(zsum)).quantize(SIXPLACES)
    '''
    '''

    #mul=lambda x,y:x*y
    #def nCk(n,k): 
    #  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )
    count_dict = {}
    print "TING"
    for i in sorted(p):
        if i not in count_dict.keys():
            count_dict[i]=1
        else:
            count_dict[i]+=1
    #print count_dict
    for key in count_dict:
        #print count_dict[key]*[0]
        for i in itertools.permutations(count_dict[key]*[0]):
            pass
            # print i, "yth"
        #print [i for i in itertools.permutations(count_dict[key]*[0])]
        count_dict[key]= len([i for i in itertools.permutations(count_dict[key]*[0]) if i != ()])

    #print count_dict
    #print len([i for i in itertools.permutations(int(n)*[0])]), sum(count_dict.values())
    reduce(lambda x, y: x*y, [1,2,3,4,5,6])
    prob = reduce(lambda x, y: x*y, count_dict.values())/(len([i for i in itertools.permutations(int(n)*[0])])+0.0)
    print prob
    i = 0
    zsum=0.000000
    while i<3001:
        zsum += prob**i
        i+=1
    getcontext().prec = 10
    SIXPLACES = Decimal(10) ** -6
    print zsum
    print Decimal(str(zsum)).quantize(SIXPLACES)
    #10
    #1 1 1 1 2 2 2 3 3 3
    '''
time_takes(p)
"""