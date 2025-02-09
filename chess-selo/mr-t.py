import csv
def load_players():
    try:
        with open("chess-selo\\players.csv", "r", encoding="UTF-8") as file:
            playerData = list(csv.reader(file))
            playerData = playerData[1:]
        return playerData
    except OSError as e:
        exit(f"OSError: {e}")

def load_games():
    try:
        with open("chess-selo\\games.csv", "r", encoding="UTF-8") as file:
            gameData = list(csv.reader(file))
            gameData = gameData[1:]
        return gameData
    except OSError as e:
        exit(f"OSError: {e}")

def calculate(player_a, player_b, result, playerDict):
    if player_a in playerDict and player_b in playerDict:
        delta = 1 / (1 + ((pow(2, (playerDict[player_a] - playerDict[player_b]) / 100))))
        if result == "1-0":
            playerDict[player_a] += round(200 * delta)
            playerDict[player_b] -= round(200 * delta)
        elif result == "0-1":
            playerDict[player_a] -= round(200 * delta)
            playerDict[player_b] += round(200 * delta)
        elif result == "1/2-1/2":
            pass

    elif player_a in playerDict and player_b not in playerDict:
        delta = 1 / (1 + ((pow(2, (playerDict[player_a] - 1500) / 100))))
        if result == "1-0":
            playerDict[player_a] += round(200 * delta)
        elif result == "0-1":
            playerDict[player_a] -= round(200 * delta)
        elif result == "1/2-1/2":
            pass

    elif player_a not in playerDict and player_b in playerDict:
        delta = 1 / (1 + ((pow(2, (1500 - playerDict[player_b]) / 100))))
        if result == "1-0":
            playerDict[player_b] += round(200 * delta)
        elif result == "0-1":
            playerDict[player_b] -= round(200 * delta)
        elif result == "1/2-1/2":
            pass

    return playerDict

def main():
    gameData = load_games()
    playerDict = {}
    playerData = load_players()
    for row in playerData:
        player, score = row[0], int(row[1])
        playerDict[player] = score
    for game in gameData:
        player_a, player_b, result = game[0], game[1], game[2]
        calculate(player_a, player_b, result, playerDict)

    for player, score in sorted(playerDict.items(), key=lambda x: x[1], reverse=True):
        print(f"{player}: {score}")

main()