import random


def gambling():
    # stake = 100
    bet = 1
    # win_count = 0
    # loss_count = 0
    days_in_month = 31
    #index_luckiest = 0
    #index_unluckiest = 0
    # win = [None]*days_in_month
    # loss = [None]*days_in_month
    days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    name_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_result = 'Win'
    usr_input = 'Y'
    month_number = 0
    while (month_result == 'Win') and ((month_number+1) < len(days_of_months)) and (usr_input == 'Y' or usr_input == 'Y'):
        """ Begin While Loop till win at Month level"""
        win_in_month = []
        loss_in_month = []

        for day in range(days_of_months[month_number]):
            win_count = 0
            loss_count = 0
            stake = 100
            #print('Loop ', day + 1)
            while (stake != 50 and stake != 150):
                random_value = random.randint(0, 1)
                if random_value == 0:
                    stake = stake - bet
                    loss_count = loss_count + 1
                else:
                    stake = stake + bet
                    win_count = win_count + 1

            print('Wins for Day ', day + 1, ' of ',name_of_months[month_number],' Month: ', win_count)
            print('Losses for Day ', day + 1, ': ', loss_count)

            # loss[day] = loss_count
            # win[day] = win_count
            loss_in_month.append(loss_count)
            win_in_month.append(win_count)

        net_result_in_month = sum(win_in_month) - sum(loss_in_month)
        print ('Net result for ', name_of_months[month_number],' Month: ', net_result_in_month)
        if (net_result_in_month) > 0:
            month_result = 'Win'
            usr_input = input("Do you wish to continue (Y/N)?")
        else:
            month_result = 'Loss'

        month_number = month_number + 1
    """ End While Loop till win at Month level """
gambling()
