from boards import Board
from players import Player


def init_players(players):
    """initialize a list of players classes
    Min 2 and Max 5

    Args:
        players (list): eg. ["red", "blue", ...]
    """
    players_classes = []
    assert 2 <= len(players) <= 5, "Between 2 and 5 players required"
    for player in players :
        players_classes.append(Player(player))
    return players_classes


players = init_players(["red", "blue"])
board = Board()

print(players[0].train_deck)