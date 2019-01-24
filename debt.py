def lend_money(debts, person, amount):
    if person in debts.keys():
        debts[person].append(amount)
    else:
        debts[person] = [amount]
def amount_owed_by(debts,person):
    if person in debts.keys():
        total = 0
        for i in debts[person]:
            total += i
        return total
    return 0
def total_amount_owed(debts):
    total = 0
    for person in debts.keys():
        for i in debts[person]:
            total += i
    return total
