class Musician():
    def __init__(self, name, salary, bank):
        self.name = name
        self.salary = salary
        self.bank = bank
    
    def add_money(self, money):
        self.bank += money

    def play(self):
        return f"{self.name} is playing"
    
    def get_salary(self):
        return self.salary
    
    def get_bank(self):
        return self.bank
