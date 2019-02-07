import league_gen
import random

NFL = league_gen.Team._registry

schedule = {}

for team in NFL:
    schedule[team.name] = {'Sched': {}, 'Weeks': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}

def divSched(NFL):
    for team in NFL:
        for opponent in NFL:
            if opponent.name not in schedule[team.name]['Sched'] and team.name != opponent.name and team.div == opponent.div and team.conf == opponent.conf:
                x = random.choice(schedule[team.name]['Weeks'])
                while x not in schedule[opponent.name]['Weeks']:
                    x = random.choice(schedule[team.name]['Weeks'])
                schedule[team.name]['Weeks'].remove(x)
                schedule[team.name]['Sched'][x] = opponent.name
                schedule[opponent.name]['Weeks'].remove(x)
                schedule[opponent.name]['Sched'][x] = team.name

divSched(NFL)
confSched(NFL)
print(schedule)
