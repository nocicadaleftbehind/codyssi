import copy
import re

initial_balances = {}
transfers = []
with open("13_Windy_Bargain_input.txt") as f:
    for line in f:
        if m := re.match(r"(.+) HAS (\d+)", line):
            initial_balances[m.group(1)] = int(m.group(2))
        if m := re.match(r"FROM (.+) TO (.+) AMT (\d+)", line):
            transfers.append((m.group(1), m.group(2), int(int(m.group(3)))))

def perform_transactions(initial_balances, transfers):
    balances = copy.deepcopy(initial_balances)
    for from_acct, to_acct, amount in transfers:
        balances[from_acct] -= amount
        balances[to_acct] += amount
    
    highest_accounts = list(sorted(balances.values(), reverse=True))
    sum_3_highest_accounts = sum(highest_accounts[:3])
    return sum_3_highest_accounts

print("PART 1")
print(perform_transactions(initial_balances, transfers))

def perform_limited_transactions(initial_balances, transfers):
    balances = copy.deepcopy(initial_balances)
    for from_acct, to_acct, amount in transfers:
        amount = min(amount, balances[from_acct])
        balances[from_acct] -= amount
        balances[to_acct] += amount
    highest_accounts = list(sorted(balances.values(), reverse=True))
    sum_3_highest_accounts = sum(highest_accounts[:3])
    return sum_3_highest_accounts

print("PART 2")
print(perform_limited_transactions(initial_balances, transfers))

def single_transaction(balances, debts, from_account, to_account, amount, debt_index=None):
    transfer_amount = min(amount, balances[from_account])
    debt = amount - transfer_amount
    balances[from_account] -= transfer_amount
    balances[to_account] += transfer_amount
    
    if debt_index is not None:
        debts[debt_index] = (from_account, to_account, debt)
    elif debt > 0:
        debts.append((from_account, to_account, debt))
    
    return balances, debts

def perform_debt_transactions(initial_balances, transfers):
    balances = copy.deepcopy(initial_balances)
    debts = []
    for from_acct, to_acct, amount in transfers:
        balances, debts = single_transaction(balances, debts, from_acct, to_acct, amount)
        
        while True:
            clean = True
            for i, debt in enumerate(debts):
                from_acct, to_acct, amount = debt
                if balances[from_acct] > 0:
                    balances, debts = single_transaction(balances, debts, from_acct, to_acct, amount, i)
                    clean = False
                    break
            debts = [debt for debt in debts if debt[2] > 0]
            if clean:
                break
    
    highest_accounts = list(sorted(balances.values(), reverse=True))
    sum_3_highest_accounts = sum(highest_accounts[:3])
    return sum_3_highest_accounts

print("PART 3")
print(perform_debt_transactions(initial_balances, transfers))
