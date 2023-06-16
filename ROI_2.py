class ROI():
    def __init__(self, income = 0, expenses = 0, cash_flow = 0, roi = 0):
        self.income = income 
        self.expenses = expenses 
        self.cash_flow = cash_flow 
        self.roi = roi

    def monthly_Income(self):    
        
        rental_income = input("Please enter your monthy income: ")       
        extra = input("Is there any other extra income you have? y/n ")
        if extra.lower() == 'y':
            other_charge = input("How much extra are you making?")
            self.income = (int(rental_income) + int(other_charge))
            ROI.monthly_Expenses(self)
        elif extra.lower() == 'n':
            self.income = int(rental_income)
            ROI.monthly_Expenses(self)
    
    def monthly_Expenses(self):
        #expense = input("Do you have any expenses? y/n")
        
        tax_expense = input("How much would the monthly tax be on the property?")
        insurance = input("How much is monthly insurance for the property?")
        mortgage = input("What is the approximate mortgage on the proprety?")
        utilities = input("Do you pay for utilities? y/n ")
        if utilities.lower() == 'n':
            your_util_cost = 0
        elif utilities.lower() == 'y':
            your_util_cost = input("Estimate the monthly utitliy cost of the property:")
        owner = input("Do you own this property? y/n ")
        if owner.lower() == 'n':
           manager_cost = .1 * self.income
           self.expenses = int(tax_expense) + int(insurance) + int(mortgage) + int(your_util_cost) + int(manager_cost)
           ROI.cashFlow(self)
        elif owner.lower() == 'y':
            self.expenses = int(tax_expense) + int(insurance) + int(mortgage) + int(your_util_cost)
           
            ROI.cashFlow(self)

    def cashFlow(self):
        monthly_cashflow = self.income - self.expenses
        self.cash_flow = monthly_cashflow * 12
        ROI.cashOnCashROI(self)

    def cashOnCashROI(self):
        down_payment = input("What is your down payment for your property?")
        closing_cost = input("How much is the closing cost for the property?")
        rehab_budget = input("Do you have any rehab_budget?")
        other = input(" Do you have any other cost?")
        total_investment = int(down_payment) + int(closing_cost) + int(rehab_budget) + int(other)
        self.roi = (self.cash_flow / total_investment) * 100
        newROI = str(self.roi)
        print(f"{newROI[:2]}% ROI")


def runROI():
    my_roi = ROI()
    my_roi.monthly_Income()

runROI()