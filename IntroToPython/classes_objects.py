lottery_player_dict = {
    "name": "Rolf",
    "numbers": (5, 9, 12, 3, 1, 21)
}


class LotteryPlayer:
    def __init__(self, name: str, numbers: tuple):
        self._name = name.capitalize(),
        self._numbers = numbers
        print("A new player created: {0}. The player has following numbers: {1}. Total: {2}.".format(
            self.name, self.numbers, self.total))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name.capitalize()

    @property
    def numbers(self):
        return self._numbers

    @property
    def total(self):
        return sum(self._numbers)

    @numbers.setter
    def numbers(self, numbers: tuple):
        self._numbers = numbers


player = LotteryPlayer("rolf", (5, 9, 12, 3, 1, 21))
print(player.name)
player_two = LotteryPlayer("max", (87, 99, 12, 3, 31, 21))
player.name = "golf"
print(player.name)

