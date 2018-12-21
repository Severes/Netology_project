class Animals:
    color = None
    wool = None

    def __init__(self, color, wool):
        self.color = color
        self.wool = wool


class Cow(Animals):
    wheight = None

    def __init__(self, color, wool, wheight):
        self.weight = wheight
        super().__init__(color, wool)


cow_1 = Cow("white", "Да", 1000)
print(cow_1.__dict__)
