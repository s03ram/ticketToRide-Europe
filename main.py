import dearpygui.dearpygui as dpg

from random import shuffle
from boards import Board
from players import Player
from data import players_colors, MEDIAS_REPERTORY, train_colors


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


def init_gameplay_elements():
    # map
    map_img = pg.image.load(MEDIAS_REPERTORY + MAP_IMG)
    x_map, _ = map_img.get_size()
    window.blit(map_img, ((x_window/2-x_map/2),0))
    
    # train cards
    train_cards = {}
    train_cards["yellow"] = pg.image.load(TRAINS_REPERTORY + "yellow.png")
    train_cards["white"] = pg.image.load(TRAINS_REPERTORY + "white.png")
    train_cards["red"] = pg.image.load(TRAINS_REPERTORY + "red.png")
    train_cards["pink"] = pg.image.load(TRAINS_REPERTORY + "pink.png")
    train_cards["orange"] = pg.image.load(TRAINS_REPERTORY + "orange.png")
    train_cards["green"] = pg.image.load(TRAINS_REPERTORY + "green.png")
    train_cards["blue"] = pg.image.load(TRAINS_REPERTORY + "blue.png")
    train_cards["black"] = pg.image.load(TRAINS_REPERTORY + "black.png")
    train_cards["locomotive"] = pg.image.load(TRAINS_REPERTORY + "locomotive.png")
    
    x_trains_cards, y_trains_cards = train_cards["yellow"].get_size()
    x = 0
    for _, surface in train_cards.items():
        window.blit(surface, (x, y_window-y_trains_cards))
        x += x_trains_cards


def count_train_cards_color(player) -> dict:
    """Returns a dictionnary with as key the color of the card
    and as value the amount of cards of this color
    """
    result = {}
    for color in train_colors:
        result[color] = 0
    for card in player.train_cards_deck:
        result[card.color] += 1
    return result




TTR_ICON = "icon_ticketToRide.png"
MAP_IMG = "map.jpg"
TRAINS_REPERTORY = MEDIAS_REPERTORY + "train_cards/"

#########################
# Setting up the window #



#######################
# Setting up the game #
board = Board()

######################
# Setting up players #
players = init_players(2, board.trains_draw.draw, board.tickets_draw.draw)


# display player's train cards
player_trains_cards = count_train_cards_color(players[0])

for color, amount in player_trains_cards.items():
    pass
    
# display player's ticket cards
player_tickets = players[0].tickets_deck
for ticket in player_tickets:
    pass

# display player's trains
player_trains = players[0].trains

# display player's stations
player_stations = players[0].stations

# display offer
for card in board.trains_draw.offer.deck:
    pass

#############
# Game loop #



