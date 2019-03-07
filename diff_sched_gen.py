import new_league_gen
import random

NFL = new_league_gen.league

def divSchedGen():
    for conf, divs in NFL.items():
        for div, teams in divs.items():
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
    for conf, divs in NFL.items():
        if conf == 'NFC':
            divList = list(divs.keys())
            divMatchups = []
            for i in range(0,2):
                x = random.choice(divList)
                divList.remove(x)
                divMatchups.append(x)
            divMatchupsOne = [[], []]
            divMatchupsTwo = [[], []]
            for n in range(0,2):
                divMatchupsOne[n].append(NFL['NFC'][divList[n]])
                divMatchupsTwo[n].append(NFL['NFC'][divMatchups[n]])
            for m in range(0,1):
                for t in range(0,4):
                    for teams in divMatchupsOne[t]:
                        print(teams)
                        for opponents in divMatchupsTwo[t]:
                            for team in range(0,4):
                                x = random.choice(teams[team].schedule['Weeks'])
                                while x not in opponents[team].schedule['Weeks']:
                                    x = random.choice(teams[team].schedule['Weeks'])
                                teams[team].schedule['Weeks'].remove(x)
                                teams[team].schedule['Sched'][x] = opponents[team].name
                                opponents[team].schedule['Weeks'].remove(x)
                                opponents[team].schedule['Sched'][x] = teams[team].name

inConfGen()
