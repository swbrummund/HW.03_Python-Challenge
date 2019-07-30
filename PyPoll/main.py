import os
import csv
from collections import Counter

csv_path = os.path.join("election_data.csv")

Votes = 0
Candidate_List = []
Candidates = {}

with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader,None)

#Count total number of votes cast
    for row in csv_reader:
        Votes += 1
    print(f'Total Votes: {Votes}')

#List of candidates who received votes
    for row in csv_reader:
        Candidate_List.append(float(row[2]))

    for candidate in Candidate_List:
        if candidate in Candidates:
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1
    print(Candidates)

#Total number of votes each candidate received
    Khan_Votes = 0
    Correy_Votes = 0
    Li_Votes = 0
    OTooley_Votes = 0

    for row in csv_reader:
        if row[2] == 'Khan':
            Khan_Votes += 1
        elif row[2] == 'Correy':
            Correy_Votes += 1
        elif row[2] == 'Li':
            Li_Votes += 1
        elif row[2] == "O'Tooley":
            OTooley_Votes += 1
            
#Percentage of votes each candidate receieved
    Percent_Khan = Khan_Votes/Votes
    Percent_Correy = Correy_Votes/Votes
    Percent_Li = Li_Votes/Votes
    Percent_OTooley = OTooley_Votes/Votes
    
#Winner of election based on popular vote

#Print analysis to terminal

#Create a text file with results