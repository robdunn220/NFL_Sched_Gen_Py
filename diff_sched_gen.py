import league_gen
import random

# Assign imported list of Team objects
NFL = league_gen.Team._registry
random.shuffle(NFL)

def scheduler(team, opponent):
    x = random.choice(team.schedule['Weeks'])
    while x not in opponent.schedule['Weeks']:
        x = random.choice(team.schedule['Weeks'])
    team.schedule['Weeks'].remove(x)
    team.schedule['Sched'][x] = opponent
    opponent.schedule['Weeks'].remove(x)
    opponent.schedule['Sched'][x] = team

def repeatSchedDebug(team, opponent, prev=False):
    listOfOpp = []
    if prev == True:
        print('Team:', team.name)
        print('Opp:', opponent.name)
    # Creates a list of opponent names in team schedule
    for opp in list(team.schedule['Sched'].items()):
        listOfOpp.append(opp[1].name)
    # Uses created list to check if opponent is already on schedule to stop double-scheduling issue
    if opponent.name not in listOfOpp:
        scheduler(team, opponent)

def divSchedGen():
    for team in NFL:
        for opponent in NFL:
        # Checks if opponent is in-conference
            if team.conf == opponent.conf and team.name != opponent.name:
                # Checks if opponent is in-division
                if team.div == opponent.div:
                    scheduler(team, opponent)
                # Checks if opponent is out-of-division, in-conference
                elif team.div == opponent.div_match:
                    repeatSchedDebug(team, opponent)
                elif team.div != opponent.div_match and team.previous_div_rank == opponent.previous_div_rank:
                    repeatSchedDebug(team, opponent, True)


# def test():
#     for team in NFL:
#         listOfOpp = []
#         for opponent in NFL:

divSchedGen()
# test()

for team in NFL:
    if team.name == 'Cowboys':
        print(len(team.schedule['Sched'].items()))
        for opp in list(team.schedule['Sched'].items()):
            print(opp[1].name)
