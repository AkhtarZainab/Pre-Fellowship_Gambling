import random


def gambling():
    # stake = 100
    bet = 1
    # win_count = 0
    # loss_count = 0
    days_in_month = 31
    index_luckiest = 0
    index_unluckiest = 0
    # win = [None]*days_in_month
    # loss = [None]*days_in_month

    win = []
    loss = []

    for day in range(days_in_month):
        win_count = 0
        loss_count = 0
        stake = 100
        print('Loop ', day + 1)
        while (stake != 50 and stake != 150):
            random_value = random.randint(0, 1)
            if random_value == 0:
                stake = stake - bet
                loss_count = loss_count + 1
            else:
                stake = stake + bet
                win_count = win_count + 1

        print('Wins for Day ', day + 1, ': ', win_count)
        print('Losses for Day ', day + 1, ': ', loss_count)

        #Exception condition to exclude 1st loop data points for comparsison since no value has been appended yet to the win and loss lists
        if day > 0:
            if loss_count > max(loss):
                index_unluckiest = day
            if win_count > max(win):
                index_luckiest = day

        # loss[day] = loss_count
        # win[day] = win_count
        loss.append(loss_count)
        win.append(win_count)
    print('Luckiest day is - Day ', index_luckiest + 1, ' with ', win[index_luckiest], ' Wins')
    print('Unluckiest day is - Day ', index_unluckiest + 1, ' with ', loss[index_unluckiest], ' Losses')


gambling()