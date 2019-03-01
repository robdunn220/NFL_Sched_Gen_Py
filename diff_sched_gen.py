import new_league_gen
import random

NFL = new_league_gen.league

def divSchedGen():
    for conf, div in NFL.items():
        for div, teams in div.items():
            for team in teams:
                for opp in teams:
                    if opp.name not in team.schedule['Sched'] and team.name != opp.name:
                        x = random.choice(team.schedule['Weeks'])
                        while x not in opp.schedule['Weeks']:
                            x = random.choice(team.schedule['Weeks'])
                        team.schedule['Weeks'].remove(x)
                        team.schedule['Sched'][x] = opp.name
                        opp.schedule['Weeks'].remove(x)
                        opp.schedule['Sched'][x] = team.name

def inConfGen():
    pass


for conference, divisions in NFL.items():
    x = random.choice(list(divisions.keys()))
    print(x)
