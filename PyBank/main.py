import os
import csv
from collections import Counter

csv_path = os.path.join("budget_data.csv")

def PyBank(Budget):
    Month = 0
    Profit_Losses = []
    Average_List = []

    #Count the number of months
    for row in csv_reader:
        Month += 1
        
        #Add Profit/Losses to a list
        Profit_Losses.append(float(row[1]))

        #Add Changes of each month to a list
        a = row[1]
        

        #Greatest Increase in Profits
        Date_I = row[0]
        Greatest_Increase = float(row[1])
        
        if float(row[1]) > Greatest_Increase:
            Greatest_Increase = float(row[1])
            Date_I = row[0]
        else:
            Greatest_Increase = Greatest_Increase
            Date_I = Date_I
        
        #Greatest Decrease in Profits
        Greatest_Decrease = float(row[1])
        Date_D = row[0]
        
        
        if float(row[1]) < Greatest_Decrease:
            Greatest_Decrease = float(row[1])
            Date_D = row[0]
        else:
            Greatest_Decrease = Greatest_Decrease
            Date_D = Date_D

    #Count Total Profit/Losses
    #Average Change Each Month
    Total_Profit_Losses = sum(Profit_Losses)
    Average_Change = len(Profit_Losses)/86
    
   
        

   
    

    #print(Profit_Losses)
    print(f'Financial Analysis')
    print(f'------------------------')
    print(f'Total Months: {Month}')
    print(f'Total Profit/Losses: ${Total_Profit_Losses}')
    print(f'Average Change: ${Average_Change}')
    print(f'Greatest Increase: {Date_I} with ${Greatest_Increase}')
    print(f'Greatest Decrease: {Date_D} with ${Greatest_Decrease}')

with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #print(csv_file)

    next(csv_reader,None)

    PyBank(csv_reader)