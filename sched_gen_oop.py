import league_gen
import random

# Assign imported list of Team objects
NFL = league_gen.Team._registry

def inDivSched():
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

def outOfDiv_inConfSched():
    divMatchOne = ['North', 'South', 'East', 'West']
    divMatchTwo = []
    for i in range(0, 2):
        div = random.choice(divMatchOne)
        divMatchTwo.append(div)
        divMatchOne.remove(div)

    for team in NFL:
        for opponent in NFL:
            if team.div == divMatchOne[0]:
                if opponent.conf == team.conf and opponent.div == divMatchOne[1]:
                    x = random.choice(team.schedule['Weeks'])
                    while x not in opponent.schedule['Weeks']:
                        x = random.choice(team.schedule['Weeks'])
                    team.schedule['Weeks'].remove(x)
                    team.schedule['Sched'][x] = opponent.name
                    opponent.schedule['Weeks'].remove(x)
                    opponent.schedule['Sched'][x] = team.name
            if team.div == divMatchTwo[0]:
                if opponent.conf == team.conf and opponent.div == divMatchTwo[1]:
                    x = random.choice(team.schedule['Weeks'])
                    while x not in opponent.schedule['Weeks']:
                        x = random.choice(team.schedule['Weeks'])
                    team.schedule['Weeks'].remove(x)
                    team.schedule['Sched'][x] = opponent.name
                    opponent.schedule['Weeks'].remove(x)
                    opponent.schedule['Sched'][x] = team.name
            # if opponent.conf == team.conf and opponent.div not in team.schedule['Sched'] and opponent.div != team.div and team.previous_div_rank == opponent.previous_div_rank:
            #     x = random.choice(team.schedule['Weeks'])
            #     while x not in opponent.schedule['Weeks']:
            #         x = random.choice(team.schedule['Weeks'])
            #     team.schedule['Weeks'].remove(x)
            #     team.schedule['Sched'][x] = opponent.name
            #     opponent.schedule['Weeks'].remove(x)
            #     opponent.schedule['Sched'][x] = team.name


inDivSched()
outOfDiv_inConfSched()

# for team in NFL:
#     if team.conf == 'NFC' and team.div == 'South':
#         print('Team:', team.name)
#         for key in sorted(team.schedule['Sched']):
#             print('%s: %s' % (key, team.schedule['Sched'][key]))
