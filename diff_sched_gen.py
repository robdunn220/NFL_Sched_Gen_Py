import league_gen
import random

weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Assign imported list of Team objects
NFL = league_gen.Team._registry
# NFL = random.sample(NFL, len(NFL))

teams = random.sample(NFL, len(NFL))

def scheduler(team, opponent):
    team.schedule.append({team.weeks[0]: {opponent.name: opponent}})
    opponent.schedule.append({opponent.weeks[0]: {team.name: team}})
    if team.weeks[0] != opponent.weeks[0]:
        m = max(team.weeks[0], opponent.weeks[0])
    else:
        m = team.weeks[0]
    team.weeks.remove(m)
    opponent.weeks.remove(m)

def repeatSchedDebug(team, opponent, div=False):
    listOfOpp = []

    for match in team.schedule:
        for name, obj in match.items():
            if not div:
                listOfOpp.append(name)
            if div:
                if listOfOpp.count(opponent.name) < 2:
                    listOfOpp.append(name)
 
    # Uses created list to check if opponent is already on schedule to stop double-scheduling issue
    if not div:
        if opponent.name not in listOfOpp:
            scheduler(team, opponent)
            return True
    else:
        if listOfOpp.count(opponent.name) < 2:
            scheduler(team, opponent)
            return True

def team_checker():
    for i in range(1,len(teams)):
        if len(teams) > 1:
            team_one = random.choice(teams)
            team_two = random.choice(teams)
            if team_one.name != team_two.name:
                if team_one.conf == team_two.conf:
                    # Checks if team_two is in-division
                    if team_one.div == team_two.div:
                        d = repeatSchedDebug(team_one, team_two, True)
                        if d:
                            teams.remove(team_one)
                            teams.remove(team_two)
                    # Checks if team_two is out-of-division, in-conference, and has been assigned as divisional team_two
                    elif team_one.div == team_two.div_match:
                        c = repeatSchedDebug(team_one, team_two)
                        if c:
                            teams.remove(team_one)
                            teams.remove(team_two)
                    # Checks if team_two is out-of-division, in-conference, and has the same previous years division ranking
                    elif team_one.div != team_two.div_match and team_one.previous_div_rank == team_two.previous_div_rank:
                        dm = repeatSchedDebug(team_one, team_two)
                        if dm:
                            teams.remove(team_one)
                            teams.remove(team_two)
                elif team_one.conf != team_two.conf:
                    if team_one.div == team_two.div:
                        ooc = repeatSchedDebug(team_one, team_two)
                        if ooc:
                            teams.remove(team_one)
                            teams.remove(team_two)

team_checker()

for team in NFL:
    if team.name == 'Falcons':
        print(team.schedule)
