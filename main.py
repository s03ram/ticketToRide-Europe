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
MAP_IMAGE = "map.jpg"
TRAINS_IMAGES = MEDIAS_REPERTORY + "train_cards/"


#######################
# Setting up the game #
board = Board()

######################
# Setting up players #
players = init_players(2, board.trains_draw.draw, board.tickets_draw.draw)

############
# Graphics #
dpg.create_context()
dpg.create_viewport(title='Ticket To Ride : Europe')


# Player's Deck
player_trains_cards = count_train_cards_color(players[0])
player_tickets = players[0].tickets_deck
player_trains = players[0].trains
player_stations = players[0].stations

with dpg.window(label="Your trains deck", autosize=True):
    # display player's train cards
    for color, amount in player_trains_cards.items():
        dpg.add_text(f"{color} : {amount}")

with dpg.window(label="Your tickets deck", autosize=True):
    # display player's ticket cards
    for ticket in player_tickets:
        dpg.add_text(f"{ticket.get_city_a()} -->  {ticket.get_city_b()} : {ticket.get_value()}")

with dpg.window(label="Your pawn deck", autosize=True):
    # display player's trains
    dpg.add_text("trains : " + str(player_trains))    
    # display player's stations
    dpg.add_text("stations : " + str(player_stations))

with dpg.window(label="Trains offer", autosize=True):
    # display trains offer
    dpg.add_button(label= "random")
    for card in board.trains_draw.offer.deck:
        dpg.add_button(label= card.get_color())
        
with dpg.window(label="Tickets offer", autosize=True):
    # display ticket offer
    dpg.add_button(label= "3 random cards")
        



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.toggle_viewport_fullscreen()

dpg.start_dearpygui()
dpg.destroy_context()



#############
# Game loop #

