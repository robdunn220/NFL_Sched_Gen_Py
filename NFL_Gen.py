import league_gen
import random

# Assign imported list of Team objects
NFL = league_gen.Team._registry
NFL = random.sample(NFL, len(NFL))
teams = NFL

# Method for scheduling teams. Redundant/ unnecessary?
def scheduler(team, opponent, week):
    team.schedule.append({week: {opponent.name: opponent}})
    opponent.schedule.append({week: {team.name: team}})

def repeatSchedDebug(team, opponent, week):
    listOfOpp = []
    # Creates a list of opponent names in team schedule
    for match in team.schedule:
        for name, obj in match.items():
            listOfOpp.append(name)
    # Uses created list to check if opponent is already on schedule to stop double-scheduling issue
    if opponent.name not in listOfOpp:
        scheduler(team, opponent, week)

def divSchedGen():
    for week in range(1,17):
        for team_one in NFL:
                for team_two in NFL:
                    if team_one.name != team_two.name:
                        if team_one.conf == team_two.conf:
                            # Checks if team_two is in-division
                            if team_one.div == team_two.div:
                                scheduler(team_one, team_two, week)
                            # Checks if team_two is out-of-division, in-conference, and has been assigned as divisional team_two
                            elif team_one.div == team_two.div_match: 
                                repeatSchedDebug(team_one, team_two, week)
                            # Checks if team_two is out-of-division, in-conference, and has the same previous years division ranking
                            elif team_one.div != team_two.div_match and team_one.previous_div_rank == team_two.previous_div_rank:
                                repeatSchedDebug(team_one, team_two, week)
                        elif team_one.conf != team_two.conf:
                            if team_one.div == team_two.div:
                                repeatSchedDebug(team_one, team_two, week)
                    continue
                continue

divSchedGen()
