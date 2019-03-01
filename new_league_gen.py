class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class Team(metaclass=IterRegistry):
    _registry = []

    def __init__(self, name, city, div, conf, win, loss, gp, previous_div_rank):
        self._registry.append(self)
        self.name = name
        self.city = city
        self.div = div
        self.conf = conf
        self.win = win
        self.loss = loss
        self.gp = gp
        self.previous_div_rank = previous_div_rank
        self.schedule = {'Sched': {}, 'Weeks': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]}

GB = Team("Packers", "Green Bay", "North", "NFC", 0, 0, 0, 1)
DET = Team("Lions", "Detroit", "North", "NFC", 0, 0, 0, 2)
CHI = Team("Bears", "Chicago", "North", "NFC", 0, 0, 0, 3)
MN = Team("Vikings", "Minnesota", "North", "NFC", 0, 0, 0, 4)
WAS = Team("Redskins", "Washington", "East", "NFC", 0, 0, 0, 1)
PHI = Team("Eagles", "Philadelphia", "East", "NFC", 0, 0, 0, 2)
NYG = Team("Giants", "New York", "East", "NFC", 0, 0, 0, 3)
DAL = Team("Cowboys", "Dallas", "East", "NFC", 0, 0, 0, 4)
ATL = Team("Falcons", "Atlanta", "South", "NFC", 0, 0, 0, 1)
NO = Team("Saints", "New Orleans", "South", "NFC", 0, 0, 0, 2)
CAR = Team("Panthers", "Carolina", "South", "NFC", 0, 0, 0, 3)
TB = Team("Buccaneers", "Tampa Bay", "South", "NFC", 0, 0, 0, 4)
SEA = Team("Seahawks", "Seattle", "West", "NFC", 0, 0, 0, 1)
LAR = Team("Rams", "Los Angeles", "West", "NFC", 0, 0, 0, 2)
ARI = Team("Cardinals", "Arizona", "West", "NFC", 0, 0, 0, 3)
SF = Team("49ers", "San Francisco", "West", "NFC", 0, 0, 0, 4)
BAL = Team("Ravens", "Baltimore", "North", "AFC", 0, 0, 0, 1)
CLE = Team("Browns", "Cleveland", "North", "AFC", 0, 0, 0, 2)
CIN = Team("Bengals", "Cincinnati", "North", "AFC", 0, 0, 0, 3)
PIT = Team("Steelers", "Pittsburgh", "North", "AFC", 0, 0, 0, 4)
BUF = Team("Bills", "Buffalo", "East", "AFC", 0, 0, 0, 1)
MIA = Team("Dolphins", "Miami", "East", "AFC", 0, 0, 0, 2)
NE = Team("Patriots", "New England", "East", "AFC", 0, 0, 0, 3)
NYJ = Team("Jets", "New York", "East", "AFC", 0, 0, 0, 4)
HOU = Team("Texans", "Houston", "South", "AFC", 0, 0, 0, 1)
IND = Team("Colts", "Indianapolis", "South", "AFC", 0, 0, 0, 2)
TEN = Team("Titans", "Tennessee", "South", "AFC", 0, 0, 0, 3)
JAC = Team("Jaguars", "Jacksonville", "South", "AFC", 0, 0, 0, 4)
KC = Team("Chiefs", "Kansas City", "West", "AFC", 0, 0, 0, 1)
LAC = Team("Chargers", "Los Angeles", "West", "AFC", 0, 0, 0, 2)
DEN = Team("Broncos", "Denver", "West", "AFC", 0, 0, 0, 3)
OAK = Team("Raiders", "Oakland", "West", "AFC", 0, 0, 0, 4)

league = {'NFC': {'North': [], 'East': [], 'South': [], 'West': []}, 'AFC': {'North': [], 'East': [], 'South': [], 'West': []}}

for team in Team._registry:
    if team.conf == 'NFC':
        if team.div == 'North':
            league['NFC']['North'].append(team)
        elif team.div == 'East':
            league['NFC']['East'].append(team)
        elif team.div == 'South':
            league['NFC']['South'].append(team)
        elif team.div == 'West':
            league['NFC']['West'].append(team)
    elif team.conf == 'AFC':
        if team.div == 'North':
            league['AFC']['North'].append(team)
        elif team.div == 'East':
            league['AFC']['East'].append(team)
        elif team.div == 'South':
            league['AFC']['South'].append(team)
        elif team.div == 'West':
            league['AFC']['West'].append(team)
