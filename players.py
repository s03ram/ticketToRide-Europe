from draws import Trains, Tickets
from data import routes


class Player:

    def __init__(self, color: str, trains_draw, tickets_draw) -> None:
        """Represent a player

        Variables :
            - color           (str): identify the player
            - trains          (int): tiles the player can afford
            - stations        (int): stations the player can build
            - train_deck   (Trains): player's train cards deck
            - ticket_deck (Tickets): player's destination tickets deck

        Methods :
            - add_card(card)
                add the given card to the corresponding deck
                card (Trains or Tickets)
            - discard_ticket(Tickets)
                remove a ticket from the player's deck
            - discard_train_card(amount, color)
                remove cards from the player's trains deck
        """
        self.color = color

        self.trains = 45
        self.stations = 3

        self.train_deck = []
        for _ in range(4):
            self.train_deck.append(trains_draw.get_card())

        self.tickets_deck = []
        for _ in range(3):
            self.tickets_deck.append(tickets_draw.get_short_ticket())

        self.tickets_deck.append(tickets_draw.get_long_ticket())


    def add_card(self, card) -> None:
        """add a card in the appropriate player's deck

        Args:
            card (Trains or Tickets): card to add
        """
        assert type(card) == Trains or type(card) == Tickets, "Can add only Trains or Tickets type"
        if type(card) == Trains:
            self.train_deck.append(card)
        elif type(card) == Tickets:
            self.train_deck.append(card)


    def discard_ticket(self, rm_ticket: Tickets) -> None:
        i = 0
        while i < len(self.tickets):
            if self.tickets[i].city_a == rm_ticket.city_a and self.tickets[i].city_b == rm_ticket.city_b:
                self.tickets.pop(i)
            else:
                i += 1


    def discard_train_card(self, amount: int, color: str) -> None:
        """remove the right amount of cards by color

        Args:
            amount (int): quantity to remove
            color (str): concerned color
        """
        i = 0
        while i < len(self.train_deck) and amount > 0:
            if self.train_deck[i].color == color:
                self.train_deck.pop(i)
                amount -= 1
            else:
                i += 1


    def draw_train_from(self, draw, **kwargs) -> None:
        """draw a train card from the draw or the offer

        draw (Deck): were to take the card (trains draw or offer)
        keyword "color" (str): only for Offer
        """
        color = kwargs.get("color")
        if color:
            self.add_card(draw.get_card(color))
        else :
            self.add_card(draw.get_card())
            
    
    def draw_tickets(self, draw) -> None:
        """takes destination tickets 

        Args:
            draw (Tickets.Draw): tickest draw
        """
        for _ in range(3):
            self.add_card(draw.get_short_ticket())


    def claim_route(self, board, city_a, city_b, color="") -> None:
        """Claim a route between two cities

        Args:
            board (Board): board object
            city_a (str): first city (order do not matter)
            city_b (str): second city (order do not matter)
            color (str): color of the route ("" means no color)
        """
        for i in board[city_a][city_b]:
            if routes[i]["color"] == color and routes[i]["owner"] == "":
                board[city_a][city_b][i]["owner"] = self.color
                lenght = board[city_a][city_b][i]["lenght"]
                
    
    def build_station(self, board, city_a, city_b):
        """claims a station between two cities

        Args:
            board (Board): board object
            city_a (str): first city (order do not matter)
            city_b (str): second city (order do not matter)
        """
        stations = board[city_a][city_b][0]["stations"]
        assert len(stations) < 2 , "Can't build more than 2 stations"
        stations.append(self.color)
        
        



