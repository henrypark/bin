#!/usr/bin/env python
#Problem Set #1

outstanding_balance = float(raw_input("What's the outstanding balance on the credit card? "))
annual_interest_rate =float(raw_input("What's the annual interest rate? "))
min_month_rate = float(raw_input("What's the minimum monthly payment rate? "))

numMonths = 1
totalAmtPaid = 0

for numMonths in range(0, 12):
    min_payment = round(min_month_rate * outstanding_balance,2)
    
    totalAmtPaid += min_payment
    
    int_paid =round((annual_interest_rate / 12) * outstanding_balance,2)
    principle_paid = round(min_payment - int_paid,2)
    
    outstanding_balance -= principle_paid  
    
    print "Month: %s" % (numMonths)
    print "Minimum monthly payment: %s" % (min_payment)
    print "Principle paid: %s" % (principle_paid)
    print "Remaining balance: %s" % (outstanding_balance)
    
    numMonths += 1

print "Result"
print "Total amount paid:",totalAmtPaid
print "Remaining Balance",outstanding_balance
