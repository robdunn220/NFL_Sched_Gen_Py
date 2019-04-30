team_one = random.choice(teams)
        team_two = random.choice(teams)

        if team_one.name != team_two.name:
            if team_one.conf == team_two.conf:
                # Checks if team_two is in-division
                if team_one.div == team_two.div:
                    d = repeatSchedDebug(team_one, team_two, True)
                    if d:
                        teams.remove(team_one)
                        teams.remove(team_two)
                # Checks if team_two is out-of-division, in-conference, and has been assigned as divisional team_two
                elif team_one.div == team_two.div_match:
                    c = repeatSchedDebug(team_one, team_two)
                    if c:
                        teams.remove(team_one)
                        teams.remove(team_two)
                # Checks if team_two is out-of-division, in-conference, and has the same previous years division ranking
                elif team_one.div != team_two.div_match and team_one.previous_div_rank == team_two.previous_div_rank:
                    dm = repeatSchedDebug(team_one, team_two)
                    if dm:
                        teams.remove(team_one)
                        teams.remove(team_two)
            elif team_one.conf != team_two.conf:
                if team_one.div == team_two.div:
                    ooc = repeatSchedDebug(team_one, team_two)
                    if ooc:
                        teams.remove(team_one)
                        teams.remove(team_two)