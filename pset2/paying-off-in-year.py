balance = 3926
annualInterestRate = 0.2

cur_balance = balance
monthly_interest = annualInterestRate / 12

payment = 0

increment = 10
while (cur_balance > 0):
    cur_balance = balance
    payment += increment
    for month in range(12):
        unpaid = cur_balance - payment
        cur_balance = unpaid + (unpaid * monthly_interest)
        
print 'Lowest Payment: ' + str(payment)