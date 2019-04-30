# This block is for the creation of the team class, and the initialization of each Team
# in the League.
# class IterRegistry(type):
#     def __iter__(cls):
#         return iter(cls._registry)

class Team():
    _registry = []

    def __init__(self, name, city, div, conf, win, loss, gp, previous_div_rank, div_match):
        self._registry.append(self)
        self.name = name
        self.city = city
        self.div = div
        self.conf = conf
        self.win = win
        self.loss = loss
        self.gp = gp
        self.previous_div_rank = previous_div_rank
        self.div_match = div_match
        self.schedule = []
        self.weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

GB = Team("Packers", "Green Bay", "North", "NFC", 0, 0, 0, 1, 'South')
DET = Team("Lions", "Detroit", "North", "NFC", 0, 0, 0, 2, 'South')
CHI = Team("Bears", "Chicago", "North", "NFC", 0, 0, 0, 3, 'South')
MN = Team("Vikings", "Minnesota", "North", "NFC", 0, 0, 0, 4, 'South')
WAS = Team("Redskins", "Washington", "East", "NFC", 0, 0, 0, 1, 'West')
PHI = Team("Eagles", "Philadelphia", "East", "NFC", 0, 0, 0, 2, 'West')
NYG = Team("Giants", "New York", "East", "NFC", 0, 0, 0, 3, 'West')
DAL = Team("Cowboys", "Dallas", "East", "NFC", 0, 0, 0, 4, 'West')
ATL = Team("Falcons", "Atlanta", "South", "NFC", 0, 0, 0, 1, 'North')
NO = Team("Saints", "New Orleans", "South", "NFC", 0, 0, 0, 2, 'North')
CAR = Team("Panthers", "Carolina", "South", "NFC", 0, 0, 0, 3, 'North')
TB = Team("Buccaneers", "Tampa Bay", "South", "NFC", 0, 0, 0, 4, 'North')
SEA = Team("Seahawks", "Seattle", "West", "NFC", 0, 0, 0, 1, 'East')
LAR = Team("Rams", "Los Angeles", "West", "NFC", 0, 0, 0, 2, 'East')
ARI = Team("Cardinals", "Arizona", "West", "NFC", 0, 0, 0, 3, 'East')
SF = Team("49ers", "San Francisco", "West", "NFC", 0, 0, 0, 4, 'East')
BAL = Team("Ravens", "Baltimore", "North", "AFC", 0, 0, 0, 1, 'West')
CLE = Team("Browns", "Cleveland", "North", "AFC", 0, 0, 0, 2, 'West')
CIN = Team("Bengals", "Cincinnati", "North", "AFC", 0, 0, 0, 3, 'West')
PIT = Team("Steelers", "Pittsburgh", "North", "AFC", 0, 0, 0, 4, 'West')
BUF = Team("Bills", "Buffalo", "East", "AFC", 0, 0, 0, 1, 'South')
MIA = Team("Dolphins", "Miami", "East", "AFC", 0, 0, 0, 2, 'South')
NE = Team("Patriots", "New England", "East", "AFC", 0, 0, 0, 3, 'South')
NYJ = Team("Jets", "New York", "East", "AFC", 0, 0, 0, 4, 'South')
HOU = Team("Texans", "Houston", "South", "AFC", 0, 0, 0, 1, 'East')
IND = Team("Colts", "Indianapolis", "South", "AFC", 0, 0, 0, 2, 'East')
TEN = Team("Titans", "Tennessee", "South", "AFC", 0, 0, 0, 3, 'East')
JAC = Team("Jaguars", "Jacksonville", "South", "AFC", 0, 0, 0, 4, 'East')
KC = Team("Chiefs", "Kansas City", "West", "AFC", 0, 0, 0, 1, 'North')
LAC = Team("Chargers", "Los Angeles", "West", "AFC", 0, 0, 0, 2, 'North')
DEN = Team("Broncos", "Denver", "West", "AFC", 0, 0, 0, 3, 'North')
OAK = Team("Raiders", "Oakland", "West", "AFC", 0, 0, 0, 4, 'North')
