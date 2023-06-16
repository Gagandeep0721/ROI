#OOP Calculation of Rental Income
class Income:
    def __init__(self,rental_income,misc ):
        self.rental_income = rental_income
        self.misc = misc


    def total_income(self):
        return self.rental_income + self.misc

rental_property = Income(2000, 1500)
print(rental_property.total_income()) 

class Expenses:
    def __init__(self, mortgage, insurance, taxes, repairs, utilities):
        self.mortgage = mortgage
        self.insurance = insurance
        self.taxes = taxes
        self.repairs = repairs
        self.utilities = utilities

    def total_expenses(self):
        return self.mortgage + self.insurance + self.taxes + self.repairs + self.utilities

property1 = Expenses(1000, 200, 300, 400, 500)
print(property1.total_expenses())  

class Cash_flow:    
   def __init__(self, income, expenses, mortgage_payment):
       self.income = income
       self.expenses = expenses
       self.mortgage_payment = mortgage_payment

    #def total_monthly_cash_flow(self):
     #   return self.income - self.expenses
   
#p = Cash_flow(3500,2400)
#print(p.total_monthly_cash_flow)


income = 3500
expenses = 2400
mortgage_payment = 1000

cash_flow = income - expenses - mortgage_payment

print("Cash flow is:", cash_flow)

def cash_on_cash_ROI(rental_income, operating_expenses, initial_investment):
    net_operating_income = rental_income - operating_expenses
    cash_on_cash_roi = (net_operating_income / initial_investment) * 100
    return cash_on_cash_roi

rental_income = 3500 # monthly rental income
operating_expenses = 2400 # monthly operating expenses
initial_investment = 100000 # initial investment

cash_on_cash_roi = cash_on_cash_ROI(rental_income, operating_expenses, initial_investment)
Yearly_cash_on_cash_roi = (cash_on_cash_roi)*12
print("Cash on Cash ROI: {:.2f}%".format(cash_on_cash_roi))
print("Yearly cash on cash ROI: {:.2f}%".format(Yearly_cash_on_cash_roi))

     



