import os
import csv

csv_path = os.path.join("election_data.csv")

with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader,None)

#Count total number of votes cast
    Votes = 0  
    for row in csv_reader:
        Votes += 1
    print(f'Total Votes: {Votes}')
#List of candidates who received votes

#Percentage of votes each candidate receieved

#Total number of votes each candidate received

#Winner of election based on popular vote

#Print analysis to terminal

#Create a text file with results