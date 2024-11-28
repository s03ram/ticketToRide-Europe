import pygame as pg

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
pg.init()
window = pg.display.set_mode((0,0), pg.FULLSCREEN | pg.HWSURFACE)
x_window, y_window = pg.display.get_window_size()
# fancy background
window.fill((40,40,40))
# awesome title
pg.display.set_caption("Ticket to ride : Europe")
# unbelievable icon
ttr_icon = pg.image.load(MEDIAS_REPERTORY + TTR_ICON)
pg.display.set_icon(ttr_icon)


#######################
# Setting up the game #
board = Board()

######################
# Setting up players #
players = init_players(2, board.trains_draw.draw, board.tickets_draw.draw)

# text render
title = pg.font.Font(None, 28)
text = pg.font.Font(None, 24)

# display player's train cards
player_trains_cards = count_train_cards_color(players[0])
texte = title.render("Your train cards :", True, "white")
window.blit(texte, (5,10))
y = 40
for color, amount in player_trains_cards.items():
    texte = text.render(color + "  :  " + str(amount), True, "white")
    window.blit(texte, (20,y))
    y += 23
    
# display player's ticket cards
player_tickets = players[0].tickets_deck
texte = title.render("Your tickets :", True, "white")
window.blit(texte, (5,300))
y = 330
for ticket in player_tickets:
    texte = text.render(ticket.get_city_a() + " -->  " + ticket.get_city_b() + " : " + str(ticket.get_value()), True, "white")
    window.blit(texte, (20,y))
    y += 23

# display player's trains
player_trains = players[0].trains
texte = title.render("Remaining trains :  " + str(player_trains), True, "white")
window.blit(texte, (5,450))

# display player's stations
player_stations = players[0].stations
texte = title.render("Remaining stations :  " + str(player_stations), True, "white")
window.blit(texte, (5,475))

# display offer
texte = title.render("Offer :", True, "white")
window.blit(texte, (x_window-300,10))
y = 40
for card in board.trains_draw.offer.deck:
    texte = text.render( card.get_color(), True, "white")
    window.blit(texte, (x_window-300,y))
    y += 23


#############
# Game loop #
running  = True
while running:
    board.trains_draw.offer.check(board.trains_draw.draw, board.trains_draw.discard)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_ESCAPE:
                running = False
            
            if event.key == pg.K_w: # draw a random train card
                print(count_train_cards_color(players[0]))
                players[0].draw_train_from(board.trains_draw.draw)
            
            if event.key == pg.K_x: # draw a train card from the offer
                print(count_train_cards_color(players[0]))
                players[0].draw_train_from(board.trains_draw.draw)


    pg.display.flip()

