import league_gen
import random

# Assign imported list of Team objects
NFL = league_gen.Team._registry
NFL = random.sample(NFL, len(NFL))

def scheduler(team, opponent, week):
    weekMatch = sorted(set(team.weeks) & set(opponent.weeks))
    if len(weekMatch) > 0:
        x = random.choice(weekMatch)
        if x:
            team.weeks.remove(x)
            opponent.weeks.remove(x)
            team.schedule.append({x: {opponent.name: opponent}})
            opponent.schedule.append({x: {team.name: team}})

def repeatSchedDebug(team, opponent, week):
    listOfOpp = []
    # Creates a list of opponent names in team schedule
    for x in team.schedule:
        for week, matchup in x.items():
            for oppname, opp in matchup.items():
                listOfOpp.append(oppname)
    # Uses created list to check if opponent is already on schedule to stop double-scheduling issue
    if opponent.name not in listOfOpp:
        scheduler(team, opponent, week)

def divSchedGen():
    for team_one in NFL:
        match = False
        week = 1
        while match == False:
            for team_two in NFL:
                if team_one.name != team_two.name:
                    if team_one.conf == team_two.conf:
                        # Checks if team_two is in-division
                        if team_one.div == team_two.div:
                            match = True
                            week += 1
                            scheduler(team_one, team_two, week)
                        # Checks if team_two is out-of-division, in-conference, and has been assigned as divisional team_two
                        elif team_one.div == team_two.div_match:
                            match = True
                            week += 1
                            repeatSchedDebug(team_one, team_two, week)
                        # Checks if team_two is out-of-division, in-conference, and has the same previous years division ranking
                        elif team_one.div != team_two.div_match and team_one.previous_div_rank == team_two.previous_div_rank:
                            match = True
                            week += 1
                            repeatSchedDebug(team_one, team_two, week)
                    elif team_one.conf != team_two.conf:
                        if team_one.div == team_two.div:
                            match = True
                            week += 1
                            repeatSchedDebug(team_one, team_two, week)

divSchedGen()

for team in NFL:
    if team.name == 'Packers':
        print(len(team.schedule))
        for x in team.schedule:
            for week, matchup in x.items():
                for oppname, opp in matchup.items():
                    y = 1
