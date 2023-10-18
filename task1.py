#!python3

"""
This list represents the amounts of money deposited into a bank account in each month for a year.
At the end of each month, 0.5% interest on the opening balance (the amount of money at the start of the month)
is added to the account.
Determine the amount of money in the account at the end of the year.

Use a for loop to iterate through the list to retrieve the inputs/deposits for each month


Note: you will want to make use of the round() function to keep your data to only 2 decimal places
You should try to not use it and see how sometimes Python has issues with decimal numbers

round(number, digits)
number: the number to be rounded
digits: optional. The number of decimal places to keep
round(103.2221,2) -> 103.22
"""

openBalance = 1000
deposits = [200,200,200,200,200,200,200,200,200,200,200,200]            # final: 3328.8
#deposits = [500,1000,300,-250,500,185,-500,205,1200,-550,125,200]      # final: 3887.71
#deposits = [1000,542,221.52,983,29.75,-10,982.23,10988,287,198,32,100]  # final: 16702.93

    