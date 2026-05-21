import json


def addUser(user,password):
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

 
def userList():     #timle eauta user name ko dict pauchau just loop over it#
  with open('data/users.json',"r") as f:
    users = json.load(f)
    return users.keys()
  with open("data/users.json","w") as f:
    json.dump(users,f,indent =4)


def usersNdcredentials():
  with open('data/users.json','r') as f:
    user = json.load(f);
    return user;
  with open("data/users.json","w") as f:
    json.dump(users,f,indent =4)



def save_score(game,score,username):
  with open('data/games.json','r') as f:
    games=json.load(f);
    games[username][game]=score;
  with open("data/games.json","w") as f:
    json.dump(games,f,indent =4)

 

def get_user_scores(username):
  with open('data/games.json','r') as f:
    games = json.load(f);
    return games[username]
  with open("data/games.json","w") as f:
    json.dump(games,f,indent =4)
 

def allUserWithScore():
  with open('data/games.json','r') as f:
    games = json.load(f);
    return games;


