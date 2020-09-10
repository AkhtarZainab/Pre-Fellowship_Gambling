import random
def gambling():
    stake = 100
    bet = 1
    bet_number = 0
    while (stake != 50 and stake != 150):
        bet_number = bet_number+1
        print('Current Bet number is: ', bet_number)
        random_value = random.randint(0, 1)
        if random_value == 0:
            stake = stake - bet
            print('Bet outcome is: Loss')
        else:
            stake = stake + bet
            print('Bet outcome is: Win')
        print("Stake value is", stake)

    return stake

print('Final stake at Resignation for the day is: ',gambling())