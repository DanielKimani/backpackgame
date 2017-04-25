#create an empty list of players
players = []

#loop through to create players 
for i in range(2):
    #while looping append dictionary items to player
    players.append({
        "name": "",
        "score": 0,
        "backpack": []
    })
#use raw_input instead of input to get a string object
    players[i]["name"] = raw_input(" Enter the name of player "+ str(i+1)+ " : ")
    print("Enter four (4) items to put in your backpack.")
    for j in range(4):
        backpack_item = raw_input("Item name "+ str(j+1)+ ":")
        players[i]["backpack"].append(backpack_item)
        #print out the backpack items
    print(players[i]["backpack"])

#start game
game_on = True
while game_on:
    for i in range(2):
        player_choice = raw_input(players[i]["name"] + ", guess an item from " +str(players[(i+1)%2]["name"]) + " backpack: ")
        other_player = players[(i+1)%2]
        if player_choice in other_player["backpack"]:
            print("You guessed right")
            players[i]["score"] += 1
            print("your score is now " + str(players[i]["score"]) )  
        else:
            print("You guessed wrong")
  
    for player in players:
        print(player["name"] + "score: " +str(player["score"]))
  
            
    play_again = raw_input("Do you want to play again ?")
    if(play_again == "no"):
        game_on = False
    elif(play_again == "yes"):
        game_on = True
        

            
            
        