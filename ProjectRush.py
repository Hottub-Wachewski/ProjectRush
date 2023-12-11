import time
import random
class PlayerUser:
    def __init__(self, cardDeck):
        self._mainDeck = cardDeck
        self._hand = []
        self._battleField = []
        self._trainingField = []
        self._grave = []
        self._life = []
        self._deck = 0
        self._energy = 0
        self._battleGround = []
    def resetPlayer(self):
        self._battleField = ["Empty", 0, "Empty", 0, "Empty", 0, "Empty", 0, "Empty", 0]
        self._trainingField = ["Empty", 0, "Empty", 0, "Empty", 0, "Empty", 0, "Empty", 0]
        self._battleGround = ["You Have No Battle Ground"]
        i = 0
        while i < 500:
            roll = random.randint(0, 5)
            card = self._mainDeck[roll]
            self._mainDeck.pop(roll)
            self._mainDeck.insert(-1, card)
            i += 1
        i = 0
        while i < 5:
            self._life.insert(0, self._mainDeck[0])
            self._mainDeck.pop(0)
            i += 1