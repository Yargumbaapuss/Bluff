from random import randint
from random import choice



AIcount=1
#This global variable should roughly keep track of how many AI have been created so that they have different names.

def AIname(st=''):
    #This function names an AI. st represents a name to remember the AI by. 
    #The name is supplemented with a number corresponding to the AIcount so that no two AIs have the same name.
    #For instance if I want to name an AI "Abraham Lincoln" this function should return "Abrahm Lincoln 1".
    #Then this function should increase the AIcount so that if I again name an AI "Abraham Lincoln" its name will be "Abrahm Lincoln 2".
    #If I name a 3rd AI "George Washington" it will be named "George Wanshington 3". 
    global AIcount
    name=st+' '+str(AIcount)
    AIcount+=1
    return name




deck=[i for i in range(1,13)]
deck*=4
#The deck represents a deck of 48 cards. The kings are removed from the deck to make the number of cards divisible by 3.
#The suits are irrelevant so a card is represented by an integer between 1 and 12.

def deal(n):
    #This function deals a hand to n players.
    #If n does not divide the number of cards in the deck this will cause an error.
    hands=[]
    #Hands is a list of the players' hands
    for i in range(n):
        hands.append([])
    remaining=deck[:]
    #We don't want the global deck variable to be changed by this function.
    while len(remaining)>=n:
        for h in hands:
            x=choice(remaining)
            h.append(x)
            remaining.remove(x)
    return hands


class Player:
    #This object should be an AI that plays the game, or a human player.
    def __init__(self, name):
        self.hand=[]
        #The player's hand represents the cards in the player's hand. 
        self.name=name
        #Name should be a string stating the player's name
        self.nex=None
        #This represents the player to move after you in the game.

    def playChoice(self, gamestate):
        return [[],[]]
        #play should be a function that determines what a player does when it is their turn to play.
        #play should input a list of cards in the hand.
        #play should return a list of length 2. The first entry is a list of cards played. The second is a list of cards they claim to play.
        #By default a generic player passes; not playing any cards.

    def call(self, gamestate):
        return 0
        #call determines if the player wants to call bluff on another player.
        #If the player does not wish to call bluff on the other player call will return 0.
        #If the player wishes to call bluff, but first wait to see if other players have called bluff call will return 1.
        #If the player wishes to be the first to call bluff, call will return 2.
        #The default player never calls bluff and so always returns 0.
    def __bool__(self):
        return True
    #This is not necessary since it is the default, but it is included to clear up any ambiguity for the reader.


class Human(Player):



class GameState:
    #This should represent the information that is publicly avaliable to all players.
    def chooseStartingPlayer(self):
        #This will choose the starting player. It will also run the first turn which is different from other turns.
        #The player with the ace of spades starts. 
        #Since their are no suits in the game the probability of a player starting is proportional to the number of 1s in thier hand.
        candidates=[]
        for player in players:
            for card in player.hand:
                if card==1:
                    candidates.append(player)
        first=choice(candidates)
        self.play(first,1)
        self.player.current=first


    def __init__(self, players):
        self.players=players
        #This should be a list of the players.
        self.history=[]
        #This should be a record of who has played what in the past.
        self.discardPile=0
        #This should be an integer representing how 
        self.activeCards=[]
        #This should keep track of the cards which have been played face down this round.
        hands=deal(len(players))
        #Here we deal the players' hands
        for i in range(len(players)):
            players[i-1].nex=players[i]
            #Here we make each player point to the next player.
            player[i].hand=hands[i]
            #Here we actually assign the players' hand to the appropriate player.
        self.currentHist=[]
        #This represents who has played what this hand.
        self.current=None
        #This represents the player who is playing now.
        self.last=None
        #This represents the last player to pass.
        self.canPass=False
        #This variable represents whether or not the player can pass.
        self.lastPlay=None
        #This should represent the last play to be made.
        self.chooseStartingPlayer()
        #see above



    def turn(self):
        self.lastPlay=self.current.playChoice(self)
        honesty=self.lastPlay[0]==self.lastPlay[1]
        #This boolean should be True if the player is "telling the truth" and False otherwise
        fastCallers=[]
        #A list of other players who want to call bluff quicly.
        slowCallers=[]
        #A list of other players who want to call bluff slowly.
        for player in self.players:
            x=player.call(self)
            if x==2:
                fastCallers.append(player)
            elif x==1:
                slowCallers.append(player)
        if fastCallers:
            caller=choice(fastCallers)
        elif slowCallers:
            caller=choice(slowCallers)
        else:
            caller=False
        #The caller should be the player who calls bluff or False if no such player exists
        #If any player wants to call bluff quickly then a random player who calls bluff quickly will be the caller
        #Otherwise a random player who calls bluff slowly is the caller
        #If no one calls bluff then the caller is False.
        



    def play(self, player, card):
        #The player plays a card from their hand.
        if card in player.hand:
            player.hand.remove(card)
            self.activeCards.append(card)




def game(players):
    #This should be a game of bluff played by the players. "players" should be a list of player objects. This should return the index of the player who wins.
























