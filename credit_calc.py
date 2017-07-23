#!/usr/bin/python

# Credit calculator (annuity)

def calc(rate, req_sum, num_period):
    pay = req_sum*(rate+(rate/((1+rate)**num_period-1)))
    return pay

if __name__ == "__main__":
    _rate_percent = input("Input rate: ")
    _rate = _rate_percent/100.0
    _req_sum = input("Input required sum of credit: ")
    _num_period = input("Input credit period: ")
    per_in_month = _rate/12.0
    month_pay = round(calc(per_in_month, _req_sum, _num_period), 2)
    total_pay = round(month_pay*_num_period, 2)
    print("Credit total value: {:.2f}".format(total_pay))

    debt = _req_sum
    periods = _num_period+1
    
    print("Period   Debt_Rest    Percents_Pay    Debt_Pay   Sum_Pay")    
    for i in range(1, periods):
        per_pay = round(debt*per_in_month, 2)
        debt_pay = round(month_pay - per_pay, 2)
        if i == _num_period:
            month_pay = total_pay - (month_pay*(_num_period-1))
        print("{:d}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(i, debt, per_pay, debt_pay, month_pay))
        debt -= round(debt_pay, 2)

    print("Program is finished")
