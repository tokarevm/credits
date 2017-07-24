#!/usr/bin/python

# Loan calculator (annuity)

def calc(rate, l_amount, l_term):
    pay = l_amount*(rate+(rate/((1+rate)**l_term-1)))
    return pay

if __name__ == "__main__":
    loan_amount = input("Input required loan amount: ")
    _rate_percent = input("Input rate per year: ")
    _rate = _rate_percent/100.0
    loan_term = input("Input term in months: ")
    per_in_month = _rate/12.0
    month_pay = round(calc(per_in_month, loan_amount, loan_term), 2)
    total_pay = round(month_pay*loan_term, 2)
    print("Credit total value: {:.2f}".format(total_pay))

    debt = loan_amount
    periods = loan_term+1
    
    print("Period\tBalance\tInterest\tPrincipal\tPayment")    
    for i in range(1, periods):
        per_pay = round(debt*per_in_month, 2)
        debt_pay = round(month_pay - per_pay, 2)
        if i == loan_term:
            month_pay = total_pay - (month_pay*(loan_term-1))
        print("{:d}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(i, debt, per_pay, debt_pay, month_pay))
        debt -= round(debt_pay, 2)

    print("Program is finished")
