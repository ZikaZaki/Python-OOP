class Player:
    teamName = 'Liverpool'  # class variable
    teamMembers = []  # class variable

    def __init__(self, name):
        self.name = name  # instance variable
        self.formerTeams = []
        self.teamMembers.append(self.name)

    # creating class method
    @classmethod
    def getTeamName(cls):
        return cls.teamName

    # creating a static class method
    @staticmethod
    def demo():
        print("I am a static method.")


# calling class methods do not require an object
print(Player.getTeamName())

# calling static methods can be without an object
p0 = Player('Lol')
p0.demo()
Player.demo()

p1 = Player('Messi')
p1.formerTeams.append('Barcelona')
p2 = Player('Ronaldo')
p2.formerTeams.append('Real Madrid')


print("Name: ", p1.name)
print("Team Name: ", p1.teamName)
print("Former Teams: ", p1.formerTeams)
print("Team Members: ", p1.teamMembers)
print("**************************************")
print("Name: ", p2.name)
print("Team Name: ", p2.teamName)
print("Former Teams: ", p2.formerTeams)
print("Team Members: ", p2.teamMembers)
