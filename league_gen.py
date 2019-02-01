import json
# This block is for the creation of the team class, and the initialization of each Team
# in the League.
class Team:
    def __init__(self, name, city, div, conf, win, loss, gp):
        self.name = name
        self.city = city
        self.div = div
        self.conf = conf
        self.win = win
        self.loss = loss
        self.gp = gp

# ATL = Team("Falcons", "Atlanta", "South", "NFC", 0, 0, 0)
# NO = Team("Saints", "New Orleans", "South", "NFC", 0, 0, 0)
# CAR = Team("Panthers", "Carolina", "South", "NFC", 0, 0, 0)
# TB = Team("Buccaneers", "Tampa Bay", "South", "NFC", 0, 0, 0)
# GB = Team("Packers", "Green Bay", "North", "NFC", 0, 0, 0)
# DET = Team("Lions", "Detroit", "North", "NFC", 0, 0, 0)
# CHI = Team("Bears", "Chicago", "North", "NFC", 0, 0, 0)
# MN = Team("Vikings", "Minnesota", "North", "NFC", 0, 0, 0)

conf = {'NFC': {},
        'AFC': {}}

conf['NFC'] = {'S': {'ATL': {'Divison': 'S', 'Record': {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Div': 0}}}}

json_conf = json.dumps(conf)

# print(div['S']['ATL'].name)
print(json_conf)
