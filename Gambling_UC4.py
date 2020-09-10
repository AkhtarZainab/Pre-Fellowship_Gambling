import random
def gambling():
    bet = 1
    total_win_amount = 0
    for day in range(20):
        stake = 100
        while (stake != 50 and stake != 150):
            random_value = random.randint(0, 1)
            if random_value == 0:
                stake = stake - bet
            else:
                stake = stake + bet

        day_win_amount = stake - 100
        print('Amount won for day', day+1, 'is', day_win_amount)
        total_win_amount = total_win_amount + day_win_amount
    return total_win_amount

print('Total amount won for 20 days is: ', gambling())
