import league_gen
import random

# Assign imported list of Team objects
NFL = league_gen.Team._registry

# Function for randomly assigning division opponents for each team
def divSched():
    for team in NFL:
        for opponent in NFL:
            if opponent.name not in team.schedule['Sched'] and team.name != opponent.name and team.div == opponent.div and team.conf == opponent.conf:
                x = random.choice(team.schedule['Weeks'])
                while x not in opponent.schedule['Weeks']:
                    x = random.choice(team.schedule['Weeks'])
                team.schedule['Weeks'].remove(x)
                team.schedule['Sched'][x] = opponent.name
                opponent.schedule['Weeks'].remove(x)
                opponent.schedule['Sched'][x] = team.name

# Function for randomly assigning inter-divisional opponents for each team. Don't have random assignment yet.
def inConfSched():
    for q in range(0,2):
        divMatchOne = ['North', 'South', 'East', 'West']
        divMatchTwo = []
        for i in range(0, 2):
            div = random.choice(divMatchOne)
            divMatchTwo.append(div)
            divMatchOne.remove(div)

        for z in range(0,2):
            for team in NFL:
                if q == 0:
                    if team.conf == 'NFC' and team.div == divMatchOne[z]:
                        for opponent in NFL:
                            if opponent.conf == 'NFC' and opponent.div == divMatchTwo[z]:
                                x = random.choice(team.schedule['Weeks'])
                                while x not in opponent.schedule['Weeks']:
                                    x = random.choice(team.schedule['Weeks'])
                                team.schedule['Weeks'].remove(x)
                                team.schedule['Sched'][x] = opponent.name
                                opponent.schedule['Weeks'].remove(x)
                                opponent.schedule['Sched'][x] = team.name
                if q == 1:
                    if team.conf == 'AFC' and team.div == divMatchOne[z]:
                        for opponent in NFL:
                            if opponent.conf == 'AFC' and opponent.div == divMatchTwo[z]:
                                x = random.choice(team.schedule['Weeks'])
                                while x not in opponent.schedule['Weeks']:
                                    x = random.choice(team.schedule['Weeks'])
                                team.schedule['Weeks'].remove(x)
                                team.schedule['Sched'][x] = opponent.name
                                opponent.schedule['Weeks'].remove(x)
                                opponent.schedule['Sched'][x] = team.name

divSched()
inConfSched()
for team in NFL:
    if team.conf == 'AFC' and team.div == 'South':
        print('Team:', team.name)
        for key in sorted(team.schedule['Sched']):
            print('%s: %s' % (key, team.schedule['Sched'][key]))
