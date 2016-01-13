balance = 999999
annualInterestRate = 0.18

cur_balance = balance
monthly_interest = annualInterestRate / 12.0

# a guess at what the lowest payment will be
payment_lower_bound = balance / 12
# lowest payment to pay off balance upper bound
payment_upper_bound = (balance * (1 + monthly_interest) ** 12) / 12.0

epsilon = .001
while (abs(cur_balance - 0.0) > epsilon):
    cur_balance = balance
    payment = (payment_upper_bound + payment_lower_bound) / 2.0
    for month in range(12):
        unpaid = cur_balance - payment
        cur_balance = unpaid + (unpaid * monthly_interest)
    
    if (cur_balance < 0):
        payment_upper_bound = payment
    elif (cur_balance > 0):
        payment_lower_bound = payment
        
print 'Lowest Payment: ' + str(round(payment, 2))