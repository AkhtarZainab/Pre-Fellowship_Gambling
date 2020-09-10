import random
def gambling():
    stake = 100
    bet = 1
    random_value = random.randint(0, 1)
    if random_value == 0:
        print("Lost amount is", bet, "$", "and stake is", stake-bet, "$")
    else:
        print("Win amount is", bet, "$","and stake is", stake+bet, "$")

gambling()

