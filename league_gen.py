# This block is for the creation of the team class, and the initialization of each Team
# in the League.
class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class Team(metaclass=IterRegistry):
    _registry = []

    def __init__(self, name, city, div, conf, win, loss, gp):
        self._registry.append(self)
        self.name = name
        self.city = city
        self.div = div
        self.conf = conf
        self.win = win
        self.loss = loss
        self.gp = gp

GB = Team("Packers", "Green Bay", "North", "NFC", 0, 0, 0)
DET = Team("Lions", "Detroit", "North", "NFC", 0, 0, 0)
CHI = Team("Bears", "Chicago", "North", "NFC", 0, 0, 0)
MN = Team("Vikings", "Minnesota", "North", "NFC", 0, 0, 0)
WAS = Team("Redskins", "Washington", "East", "NFC", 0, 0, 0)
PHI = Team("Eagles", "Philadelphia", "East", "NFC", 0, 0, 0)
NYG = Team("Giants", "New York", "East", "NFC", 0, 0, 0)
DAL = Team("Cowboys", "Dallas", "East", "NFC", 0, 0, 0)
ATL = Team("Falcons", "Atlanta", "South", "NFC", 0, 0, 0)
NO = Team("Saints", "New Orleans", "South", "NFC", 0, 0, 0)
CAR = Team("Panthers", "Carolina", "South", "NFC", 0, 0, 0)
TB = Team("Buccaneers", "Tampa Bay", "South", "NFC", 0, 0, 0)
SEA = Team("Seahawks", "Seattle", "West", "NFC", 0, 0, 0)
LAR = Team("Rams", "Los Angeles", "West", "NFC", 0, 0, 0)
ARI = Team("Cardinals", "Arizona", "West", "NFC", 0, 0, 0)
SF = Team("49ers", "San Francisco", "West", "NFC", 0, 0, 0)

BAL = Team("Ravens", "Baltimore", "North", "AFC", 0, 0, 0)
CLE = Team("Browns", "Cleveland", "North", "AFC", 0, 0, 0)
CIN = Team("Bengals", "Cincinnati", "North", "AFC", 0, 0, 0)
PIT = Team("Steelers", "Pittsburgh", "North", "AFC", 0, 0, 0)
BUF = Team("Bills", "Buffalo", "East", "AFC", 0, 0, 0)
MIA = Team("Dolphins", "Miami", "East", "AFC", 0, 0, 0)
NE = Team("Patriots", "New England", "East", "AFC", 0, 0, 0)
NYJ = Team("Jets", "New York", "East", "AFC", 0, 0, 0)
HOU = Team("Texans", "Houston", "South", "AFC", 0, 0, 0)
IND = Team("Colts", "Indianapolis", "South", "AFC", 0, 0, 0)
TEN = Team("Titans", "Tennessee", "South", "AFC", 0, 0, 0)
JAC = Team("Jaguars", "Jacksonville", "South", "AFC", 0, 0, 0)
KC = Team("Chiefs", "Kansas City", "West", "AFC", 0, 0, 0)
LAC = Team("Chargers", "Los Angeles", "West", "AFC", 0, 0, 0)
DEN = Team("Broncos", "Denver", "West", "AFC", 0, 0, 0)
OAK = Team("Raiders", "Oakland", "West", "AFC", 0, 0, 0)
