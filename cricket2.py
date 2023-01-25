class Player:
    def __init__(self,name,position,batting,bowling,fielding,points) :
        self.name = name
        self.positon = position
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.points = points
        
    def playerStats(self):
        print("Name: " + self.name)
        print("Position: " + self.positon)
        self.battingStats()
        self.bowlingStats()
        self.fieldingStats()
        print("Player Points: ",self.points)
        print(" ")
    
    def battingStats(self):
        print("Batting Stats: ")
        print("        Runs: ",self.batting["runs"])
        print("        Fours: ",self.batting["fours"])
        print("        Sixes: ",self.batting["sixes"])
        print("        Strike Rate: ",self.batting["strikeRate"])
        
    def bowlingStats(self):
        print("Bowling Stats: ")
        print("        Wickets: ",self.bowling["wickets"])
        print("        Economy Rate: ",self.bowling["economyRate"])
        
    def fieldingStats(self):
        print("Fielding Stats: ")
        print("        Run Outs: ",self.fielding["runOuts"])
        print("        Catches: ",self.fielding["catches"])
          
def addPlayer() :
    name = input("Enter player name: ")
    position = input("Enter player position: ")
    points = 0
    batting = {
                    "runs" : int(input("Enter the no. of runs scored: ")),
                    "fours" : int(input("Enter the no. of 4s hit: ")),
                    "sixes" : int(input("Enter the no. of 6s hit: ")),
                    "strikeRate" : int(input("Enter the strike rate: "))
              }
    points = points + (batting["runs"]/2)
    if batting["runs"] >= 100:
        points = points + 10
    if batting["runs"] >= 50:
        points = points + 5
    if batting["strikeRate"] >= 80 and batting["strikeRate"] <= 100:
        points = points + 2
    if batting["strikeRate"] > 100:
        points = points + 4
    points = points + batting["fours"] + (2 * batting["sixes"])
    
    bowling = {
                    "wickets" : int(input("Enter the no. of wickets: ")),
                    "economyRate" : float(input("Enter the economy rate: ")),
              }
    
    points = points +  bowling["wickets"]
    if bowling["wickets"] > 3:
        points = points + 5
    if bowling["wickets"] > 5:
        points = points + 10
    if bowling["economyRate"] >= 3.5 and bowling["economyRate"] <= 4.5:
        points = points + 4
    if bowling["economyRate"] >= 2 and bowling["economyRate"] <= 3.5:
        points = points + 7
    if bowling["economyRate"] < 2:
        points = points + 10      
                
    fielding = {
                    "catches" : int(input("Enter the no. of catches: ")),
                    "runOuts" : int(input("Enter the no. of run outs: ")),
               }
    points = points + 10 * (fielding["catches"] + fielding["runOuts"])
             
    player = Player(name,position,batting,bowling,fielding,points)
    return player

def display(players) :
    for player in players:
        player.playerStats()

# Main 
ch = 'y'
players = []
for i in range(1,5):
    players.append(addPlayer())    
display(players)
