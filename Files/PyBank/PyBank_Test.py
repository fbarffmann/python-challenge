import os
import csv
# Establishing lists
date_list = []
profitlosses_list = []
# Designating the file that I want to use and the path to it
csvpath = os.path.join("Resources","budget_data.csv")
# Read data from CSV and populate date_list and profitlosses_list
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        date_list.append(row[0])
        profitlosses_list.append(int(row[1]))
# Calculate total number of months
print("Financial Analysis")
total_months = len(date_list)
print("Total Months:", total_months)
# Calculate total profit/losses
total_profitlosses = sum(profitlosses_list)
print("Total: ${:.2f}".format(total_profitlosses))
# Calculate changes in profit/losses
changes = [profitlosses_list[i+1] - profitlosses_list[i] for i in range(len(profitlosses_list)-1)]
# Calculate average change
average_change = sum(changes) / len(changes)
print("Average Change: ${:.2f}".format(average_change))
# Find greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
# Find corresponding dates for greatest increase and decrease
index_of_greatest_increase = changes.index(greatest_increase) + 1
index_of_greatest_decrease = changes.index(greatest_decrease) + 1
date_of_greatest_increase = date_list[index_of_greatest_increase]
date_of_greatest_decrease = date_list[index_of_greatest_decrease]
# Output results
print("Greatest Increase in Profits: {} (${:.2f})".format(date_of_greatest_increase, greatest_increase))
print("Greatest Decrease in Profits: {} (${:.2f})".format(date_of_greatest_decrease, greatest_decrease))