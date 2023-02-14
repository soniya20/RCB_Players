import json

# This function will open and load data of the JSON file and also runs the below functions:
def readJsonData():
    with open("example.json") as f:
        # Load the JSON data from the file
        data = json.load(f)
        players = data["player"]
        #print("player", players)
        #Calling below Functions 
        PlayersCountry(players)
        PlayerRole(players)


# This function will verify the country of the players: is India        
def PlayersCountry(players):
    PC_count = 0
    for player in players:
        if player["country"].lower() != "india":
            PC_count += 1
    if PC_count == 4:
        print("Team have only 4 Foreign Players")
    else:
        print("Team have ", PC_count, "Foreign Player")
        
        

# This function will verify that the team have atleast one wicket-keeper
def PlayerRole(players):
    Rcount = 0
    for player in players:
        if player["role"].lower() == "wicket-keeper":
            Rcount += 1
    if Rcount >= 1:
        print("Team have atleast", Rcount, "Wicket Keeper")
    else:
        print("Team have no Wicket keeper")

readJsonData()
