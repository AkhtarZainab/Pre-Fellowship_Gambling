import random
def gambling():
    bet = 1

    days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    name_of_months = ['Jan','Feb','Mar','Apr','May', 'Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    for i in range(len(days_of_months)): #loop for a month at a time
        month_win_amount = 0   # initializing value for ith month
        month_win_days = 0
        month_loss_days = 0
        for day in range(days_of_months[i]):
        # Looping for number of days in month i, using the array index i in the array days_of_months
            stake = 100
            while (stake != 50 and stake != 150):
                random_value = random.randint(0, 1)
                if random_value == 0:
                    stake = stake - bet
                else:
                    stake = stake + bet


            day_win_amount = stake - 100
            print('Amount for day', day+1, 'is', day_win_amount)


            if day_win_amount < 0:
                month_loss_days = month_loss_days + 1
            else:
                month_win_days = month_win_days + 1

            month_win_amount = month_win_amount + day_win_amount

        print("For ", name_of_months[i],": Total win days is: ", month_win_days, "and Total loss days is: ", month_loss_days)
        print("The difference between the no. of days won and lost is: ", month_win_days - month_loss_days)
        print("For ", name_of_months[i],": Total win amount is: ", month_win_amount)


gambling()