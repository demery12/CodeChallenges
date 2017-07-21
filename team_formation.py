class Team:
    def __init__(self):
        members = []
        min_skill = None
        max_skill = None
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_test = int(raw_input())
for test in range(num_test):
    people = [int(x) for x in raw_input().split(' ')]
    print people
    teams = []
    for person in people[1:]:
        found_team_min = False
        found_team_min = False
        for team in teams:
            if not found_team_min and team.min_skill == person + 1:
                team.min_skill = person
                team.members.append(person)
                if found_team_max:
                    that_team.members.extend(team)
                    that_team
                found_team_min = True
                that_team = team
            elif not found_team_max and team.max_skill == person - 1:
                team.max_skill = person
                team.members.append(person)
                if found_team_min:
                    that_team.members.extend(team)
                found_team_max = True
                that_team = team