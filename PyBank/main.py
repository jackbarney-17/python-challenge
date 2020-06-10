# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results

# Import dependencies
import os
import csv

# File path
pybank_csv_path = os.path.join("PyBank/Resources","budget_data.csv")

# Setting up lists to store data
profit = []
dates = []

# setting up variable counters
total_net_profit = 0
profit_change = 0
profit_value = 0
total_months = 0


with open(pybank_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    
    # reading first row to properly set up variables tracking profits/changes/counters
    first_row = next(csv_reader)
    total_months += 1
    total_net_profit += int(first_row[1])
    profit_value = int(first_row[1])

    for row in csv_reader:
        
        # storing dates in a list
        dates.append(row[0])
        
        # counting months
        total_months += 1

        # getting total profit over all months
        total_net_profit += int(row[1])

        # calculating changes and storing in list
        profit_change = int(row[1])-profit_value
        profit.append(profit_change)
        profit_value = int(row[1])
        
    # best profit increase from one month to next
    best_profit_increase = max(profit)
    best_date = dates[profit.index(best_profit_increase)]

    # worst profit decrease from one month to next
    worst_profit_decrease = min(profit)
    worst_date = dates[profit.index(worst_profit_decrease)]

    # average change calculation
    avg_change = sum(profit)/len(profit)


print('Financial Analysis')
print('---------------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total Profit: ${total_net_profit}')
print(f'Average Change: ${round(avg_change,2)}')
print(f'Greatest Increase in Profits: {best_date} ${best_profit_increase}')
print(f'Greatest Decrease in Profits: {worst_date} ${worst_profit_decrease}')

with open('output.txt', 'w') as text_file:
    text_file.write('Financial Analysis\n')
    text_file.write('---------------------------------------------------\n')
    text_file.write(f'Total Months: {total_months}\n')
    text_file.write(f'Total Profit: ${total_net_profit}\n')
    text_file.write(f'Average Change: ${round(avg_change,2)}\n')
    text_file.write(f'Greatest Increase in Profits: {best_date} ${best_profit_increase}\n')
    text_file.write(f'Greatest Decrease in Profits: {worst_date} ${worst_profit_decrease}\n')