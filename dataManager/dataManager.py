import json

def addUser(user,password):  #for adding username and password
  with  open("data/users.json","r") as f:
    users = json.load(f)
    users[user] = {"password": password}
    with open("data/games.json","r") as file:
      scores = json.load(file)
      scores[user] ={
           "rps": 0,
           "wordle": 0,
           "ttt": 0,
           "quiz": 0,
           "guess_number": 0
      }

    with open("data/games.json","w") as file:
      json.dump(scores,file,indent=4);
  with open("data/users.json","w") as f:
    json.dump(users,f,indent =4)

 
def userList():     #timle eauta user name ko dict pauchau just loop over it (For displaying username)
  with open('data/users.json',"r") as f:
    users = json.load(f)
    print(users.keys())
    return users.keys()


def usersNdcredentials():  #for verifying
  with open('data/users.json','r') as f:
    user = json.load(f);
    return user;
  with open("data/users.json","w") as f:
    json.dump(users,f,indent =4)


def save_score(game,score,username): #for saving score of a game
  with open('data/games.json','r') as f:
    games=json.load(f);
    games[username][game]=score;
  with open("data/games.json","w") as f:
    json.dump(games,f,indent =4)

 
def get_user_scores(username):  #showing score for leaderborad
  with open('data/games.json','r') as f:
    games = json.load(f);
    return games[username]
  with open("data/games.json","w") as f:
    json.dump(games,f,indent =4)
 

def allUserWithScore():  #for profile use
  with open('data/games.json','r') as f:
    games = json.load(f);
    return games;
