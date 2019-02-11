import league_gen
import random

NFL = league_gen.Team._registry

# def byeWeeks():


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

def inConfSched():
    for team in NFL:
        for opponent in NFL:
            if team.conf == 'NFC' and team.div == 'South':
                if opponent.name not in team.schedule['Sched'] and opponent.div == 'North' and opponent.conf == 'NFC':
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
    print('Team:', team.name)
    for key in sorted(team.schedule['Sched']):
        print('%s: %s' % (key, team.schedule['Sched'][key]))
