balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def minMonthlyPayment (balance, min_rate):
    '''
    balance (int) -- the current unpaid balance in the account
    min_rate (float) -- the minimum monthly payment rate
    returns the minimum monthly payment to 2 decimal places
    '''
    return balance * min_rate
    
def monthlyUnpaidBalance (balance, min_payment):
    return balance - min_payment
    
def newBalance (unpaid_balance, monthly_interest_rate):
    return unpaid_balance + (monthly_interest_rate * unpaid_balance)


monthlyInterestRate = annualInterestRate / 12

sum_payment = 0

for month in range(12):
    print 'Month: ' + str(month+1)
    min_payment = minMonthlyPayment(balance, monthlyPaymentRate)
    sum_payment += min_payment
    print 'Minimum monthly payment: ' + str(round(min_payment, 2))
    unpaid_balance = monthlyUnpaidBalance(balance, min_payment)
    balance = newBalance(unpaid_balance, monthlyInterestRate)
    print 'Remaining balance: ' + str(round(balance, 2))
    
print 'Total paid: ' + str(round(sum_payment, 2))
print 'Remaining balance: ' + str(round(balance, 2))