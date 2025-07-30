class SimpleInterest:
    def input_values(self):
        self.principal_amount=int(input("Enter Principal amount:"))
        self.rate_of_interest=float(input("Enter Principal amount:"))
        self.time_in_years=int(input("Enter time in years:"))

    def find_simple_interest(self):
        self.simple_interest=self.principal_amount*self.rate_of_interest*self.time_in_years/100

    def print_simple_interest(self):
        print("Simple Interest:",self.simple_interest)


si=SimpleInterest()
si.input_values()
si.find_simple_interest()
si.print_simple_interest()
