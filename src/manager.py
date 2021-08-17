class Manager:
    def __init__(self, name):
        self.name = name

    def pay_salaries(self, musicians):
        for musician in musicians:
            musician.add_money(musician.salary)
    
    def calculate_payroll(self, musicians):
        total_payroll = 0
        for musician in musicians:
            total_payroll += musician.salary
        return total_payroll






    