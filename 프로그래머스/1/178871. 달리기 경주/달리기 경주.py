def solution(players, callings):
    position = {player: i for i, player in enumerate(players)}
    position = {player: i for i , player in enumerate(players)}
    
    for player in callings:
        i = position[player]
        frontplayer = players[i -1]
        players[i -1], players[i] = players[i], players[i - 1]
        position[player] -= 1
        position[frontplayer] += 1
    return players
