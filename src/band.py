class Band:
    def __init__(self, name, guitarist, bassist, singer, manager):
        self.name = name
        self.guitarist = guitarist
        self.bassist = bassist
        self.singer = singer
        self.manager = manager

    def play(self):
        return f"{self.guitarist.play()}\n{self.bassist.play()}\n{self.singer.play()}\n"

    def calculate_payroll(self, musicians):
        return self.manager.calculate_payroll(musicians)
    
    def pay_salaries(self, musicians):
        self.manager.pay_salaries(musicians)