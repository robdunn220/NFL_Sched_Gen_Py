import league_gen
import random

weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Assign imported list of Team objects
NFL = league_gen.Team._registry
# NFL = random.sample(NFL, len(NFL))

teams = list(NFL)

def scheduler(team, opponent, week):
    team.schedule.append({opponent.name: opponent})
    opponent.schedule.append({team.name: team})

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

for x in range(1,17):
    while len(teams) > 0:
        team_one = random.choice(teams)
        teams.remove(team_one)
        team_two = random.choice(teams)
        teams.remove(team_two)

        if team_one.name != team_two.name:
            if team_one.conf == team_two.conf:
                # Checks if team_two is in-division
                if team_one.div == team_two.div:
                    team_one.schedule.append({x: {team_two.name: team_two}})
                    team_two.schedule.append({x: {team_one.name: team_one}})
                # Checks if team_two is out-of-division, in-conference, and has been assigned as divisional team_two
                elif team_one.div == team_two.div_match:
                    team_one.schedule.append({x: {team_two.name: team_two}})
                    team_two.schedule.append({x: {team_one.name: team_one}})
                # Checks if team_two is out-of-division, in-conference, and has the same previous years division ranking
                elif team_one.div != team_two.div_match and team_one.previous_div_rank == team_two.previous_div_rank:
                    team_one.schedule.append({x: {team_two.name: team_two}})
                    team_two.schedule.append({x: {team_one.name: team_one}})
            elif team_one.conf != team_two.conf:
                if team_one.div == team_two.div:
                    team_one.schedule.append({x: {team_two.name: team_two}})
                    team_two.schedule.append({x: {team_one.name: team_one}})
    teams = list(NFL)

for team in NFL:
    if team.name == 'Falcons':
        print(team.schedule)
