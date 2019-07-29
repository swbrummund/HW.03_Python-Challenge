import os
import csv

csv_path = os.path.join("budget_data.csv")

Month = 0
Profit_Losses = 0
Average_Change = 0
Greatest_Increase = 0
Greatest_Decrease = 0
Date_I = "date"
Date_D = "date"

with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader,None)

    print(row[1])

    #Count the number of months
    for row in csv_reader:
        Month += 1

    #Count Total Profit/Losses
    for row in csv_reader:
        Profit_Losses += float(row[1])

    #Average Change Each Month
    Average_Change = Profit_Losses/Month

    #Greatest Increase in Profits
    Date_I = row[0]
    Greatest_Increase = float(row[1])
    for row in csv_reader:
        if float(row[1]) > Greatest_Increase:
            Greatest_Increase = float(row[1])
            Date_I = row[0]
        else:
            Greatest_Increase = Greatest_Increase
            Date_I = Date_I

    #Greatest Decrease in Profits
    Greatest_Decrease = float(row[1])
    Date_D = row[0]
    for row in csv_reader:
        if float(row[1]) < Greatest_Decrease:
            Greatest_Decrease = float(row[1])
            Date_D = row[0]
        else:
            Greatest_Decrease = Greatest_Decrease
            Date_D = Date_D

    print(f'Financial Analysis')
    print(f'------------------------')
    print(f'Total Months: {Month}')
    print(f'Total Profit/Losses: ${Profit_Losses}')
    print(f'Average Change: ${Average_Change}')
    print(f'Greatest Increase: {Date_I} with ${Greatest_Increase}')
    print(f'Greatest Decrease: {Date_D} with ${Greatest_Decrease}')