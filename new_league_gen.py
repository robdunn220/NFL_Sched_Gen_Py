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

def divSchedGen():
    for team in NFL:
        teamList = []
        for opponent in NFL:
            # Checks if opponent is in-conference
            if team.name == 'Falcons' and team.conf == opponent.conf and team.name != opponent.name:
                # Checks if team is in-division
                if team.div == opponent.div:
                    scheduler(team, opponent)
                elif opponent.name == 'Saints':
                    scheduler(team, opponent)

divSchedGen()

for team in NFL:
    for opponent in NFL:
        if team.name == 'Falcons':
            for t in list(team.schedule['Sched'].items()):
                print(t[1].name)
