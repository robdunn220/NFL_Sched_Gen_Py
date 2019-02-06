import league_gen

NFL = league_gen.Team

schedule = {}

def divSched(NFL):
    for team in NFL:
        schedule[team.name] = []
        for opponent in NFL:
            if team.name != opponent.name and team.div == opponent.div and team.conf == opponent.conf:
                schedule[team.name].append(opponent.name)
divSched(NFL)
print(schedule)
