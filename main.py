from random import shuffle
from boards import Board
from players import Player
from data import players_colors


def init_players(players_amount:int, trains_draw, tickets_draw):
    """initialize a list of players classes
    Min 2 and Max 5

    Args:
        players_amount (int): number of players
    """
    assert 2 <= players_amount <= 5, "Between 2 and 5 players required"
    
    shuffle(players_colors)
    players = []
    for i in range(players_amount):
        players.append(Player(players_colors[i], trains_draw, tickets_draw))
    return players


board = Board()

players = init_players(2, board.trains_draw.draw, board.tickets_draw.draw)
