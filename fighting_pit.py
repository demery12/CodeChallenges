
def who_wins(n1, n2, t1, t2):
    # sums are unique per team i.e. if t1 has 5, that is the only config for it that has 5
    print len(t1), sum(t1), len(t2), sum(t2)

    matchup = w[n1][n2]
    s1 = sum(t1)
    s2 = sum(t2)
    w[n1][n2][s1] = {}
    if s1 in w[n1][n2] and s2 in w[n1][n2][s1]:
        return w[n1][n2][s1][s2]
    if t1[-1] >= len(t2) or len(t2) == 0:
        return n1
    w[n1][n2][s1][s2] = who_wins(n2, n1, t2[:-t1[-1]], t1)
    return w[n1][n2][s1][s2]

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_fighters, num_teams, num_queries = (int(x) for x in raw_input().strip().split(' '))
teams = {i+1:[] for i in range(num_teams)}
strengths = {i+1:0 for i in range(num_teams)}
Q ={(1,2), 2}
w = {i+1:{i+1:{} for i in range(num_teams)} for i in range(num_teams)}
for fighter in range(num_fighters):
    strength, team = (int(x) for x in raw_input().strip().split(' '))
    teams[team].append(strength)
    strengths[team]+=strength

for q in range(num_queries):
    q_type, p1, p2 = (int(x) for x in raw_input().strip().split(' '))
    if q_type == 1: # add fighter
        teams[p2].append(p1)
        strengths[p2]+=p1
    else:
        
        print who_wins(p1, p2, sorted(teams[p1]), sorted(teams[p2])
        #if strengths[p1]/float(len(teams[p1]))>=strengths[p2]/float(len(teams[p2])):
        #    print p1
        #else:
        #    print p2
        """
        t1 = sorted(teams[p1])
        t2 = sorted(teams[p2])
        p1_wins=False
        p2_wins=False
        while(len(t1)>0 and len(t2)>0):
            
            try:
                if len(t2) in w[p1][p2][len(t1)]:
                    print p1
                    p1_wins = True
                    break
            except KeyError:
                pass
            
            if t1[-1] >= len(t2):
                print p1
                p1_wins = True
                break
            t2 = t2[:-t1[-1]]
            if len(t2)==0:
                print p1
                p1_wins = True
                break
            
            try:
                if len(t1) in w[p2][p1][len(t2)]:
                    print p2
                    p2_wins = True
                    break
            except KeyError:
                pass
                        
                
            if t2[-1] >= len(t1):
                print p2
                p2_wins = True
                break                         
            t1 = t1[:-t2[-1]]
            if len(t1)==0:
                print p2
                p2_wins = True
                break
        lp1 = len(teams[p1])
        lp2 = len(teams[p2])
        if p1_wins:
            win = w[p1]
            if p2 in win:
                lose = win[p2]
                if lp1 in lose:
                    lose[lp1].add(lp2)
            else:
                win[p2] = {lp1:set([lp2])}

                
        elif p2_wins:
            win = w[p2]
            if p1 in win:
                lose = win[p1]
                if lp2 in lose:
                    lose[lp2].add(lp1)
            else:
                win[p1] = {lp2:set([lp1])}

        """     

#print w       
#print w[1][2][4]
"""     


# Enter your code here. Read input from STDIN. Print output to STDOUT
num_fighters, num_teams, num_queries = (int(x) for x in raw_input().strip().split(' '))
teams = {i+1:0 for i in range(num_teams)}
for fighter in range(num_fighters):
    strength, team = (int(x) for x in raw_input().strip().split(' '))
    teams[team] += strength
for q in range(num_queries):
    q_type, p1, p2 = (int(x) for x in raw_input().strip().split(' '))
    if q_type == 1: # add fighter
        teams[p2] += p1
    else:
        if p1 >= p2:
            print p1
        else:
            print p2
"""
        
        