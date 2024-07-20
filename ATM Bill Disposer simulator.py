'''
1st step is writing a function, which calculates the bills usage. 
Input: an amount of withdrawal.
Output: a dictionary with the bill denomination and how many bills to use.
'''

def calculate_bills_to_use(amount):
    bills_of_num = []
    bills = [500, 100, 50, 25, 10, 5, 1]
    for num in bills:
        bill_of_num = amount // num
        bills_of_num.append(bill_of_num)
        amount %= num

    bills_to_use = dict(zip(bills, bills_of_num))
    
    return bills_to_use


'''
2nd function calculates the required number of bills of each denomination for a certain amount.
Input: an amount of withdrawal and available bills in the ATM as a dictionary. 
Output: a dictionary with the bill denomination and how many bills to use taking into account the availability of bills. 
'''

def calculate_bills_to_use_advanced(amount, bills):
    bills_of_num = []
    for bill, available_bills in bills.items():
        bill_of_num = amount // bill
        if bill_of_num > available_bills:
            bill_of_num = available_bills
            amount -= bill * available_bills
        else: 
            amount %= bill
        bills_of_num.append(bill_of_num)

    bills_to_use_advanced = dict(zip(bills, bills_of_num))
    
    return bills_to_use_advanced
