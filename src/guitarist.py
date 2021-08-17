from src.musician import Musician


class Guitarist(Musician):
    def __init__(self, name, salary, bank):
        super().__init__(name, salary, bank)

    def play(self):
        return f"{self.name} is playing guitar"
