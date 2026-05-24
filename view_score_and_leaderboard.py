from dataManager.dataManager import *

import json

def save_high_score(game, score, username):

    with open("data/games.json", "r") as f:
        games = json.load(f)

    current_score = games[username][game]

    if score > current_score:

        games[username][game] = score

        with open("data/games.json", "w") as f:
            json.dump(games, f, indent=4)

        print("New High Score Saved!")

    else:
        print("High Score Not Beaten")