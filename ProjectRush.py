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
        self._energy = 0
        self._battleGround = []
    def resetPlayer(self):
        self._battleField = ["Empty", 0, "Empty", 0, "Empty", 0, "Empty", 0, "Empty", 0]
        self._trainingField = ["Empty", 0, "Empty", 0, "Empty", 0, "Empty", 0, "Empty", 0]
        self._battleGround = ["You Have No Battle Ground"]
        i = 0
        while i < 500:
            roll = random.randint(0, len(self._mainDeck))
            card = self._mainDeck[roll]
            self._mainDeck.pop(roll)
            self._mainDeck.insert(-1, card)
            i += 1
        i = 0
        while i < 5:
            self._life.insert(0, self._mainDeck[0])
            self._mainDeck.pop(0)
            i += 1
    def explainCards(self, choice):
        print("name", self._hand[choice + 1].get_name)
        print("classes", self._hand[choice + 1].get_properties)
        print("power", self._hand[choice + 1].get_power)
        print("cost", self._hand[choice + 1].get_cost)
        print(self._hand[choice + 1].get_effects)
class PlayingCards:
    def __init__(self, name, power, cost, properties, effect):
        self._name = name
        self._power = power
        self._cost = cost
        self._properties = properties
        self._effect = effect
    def get_name(self):
        return self._name
    def get_power(self):
        return self._power
    def get_cost(self):
        return self._cost
    def get_properties(self):
        return self._properties
    def get_effects(self):
        return self._effect