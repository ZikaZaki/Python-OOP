class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName


class Team:
    def __init__(self, name):
        self.name = name
        self.players = list()

    def addPlayer(self, player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)


class School:
    def __init__(self, name):
        self.name = name
        self.teams = list()

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        count = 0
        for team in self.teams:
            count += team.getNumberOfPlayers()
        return count


p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

t1 = Team("Red")
t1.addPlayer(p1)
t1.addPlayer(p2)
print(t1.getNumberOfPlayers())

print("*" * 20)

t2 = Team("Blue")
t2.addPlayer(p3)
t2.addPlayer(p4)
print(t2.getNumberOfPlayers())

sc1 = School("My School")
sc1.addTeam(t1)
sc1.addTeam(t2)
print("*" * 20)
print(sc1.getTotalPlayersInSchool())
