class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return (self.__username)


Zika = User('Zika')
print('Before setting: ', Zika.getUsername())
Zika.setUsername('Zack')
print('After setting: ', Zika.getUsername())
