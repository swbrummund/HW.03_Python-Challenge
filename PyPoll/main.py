import os
import csv

csv_path = os.path.join("election_data.csv")

Total_Votes = 0
Candidates = {}

with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader,None)

#Count total number of votes cast
    for row in csv_reader:
        Total_Votes += 1
  
#List of candidates who received votes
#Total Votes per Candidate
        Candidate_Name = row[2]
        if Candidate_Name in Candidates:
            Candidates[Candidate_Name] = Candidates[Candidate_Name] + 1
        else:
            Candidates[Candidate_Name] = 1

#Change key name in dictionary
    Candidates["OTooley"] = Candidates.pop(OTooley)

#Percentage of votes each candidate receieved
    Percent_Khan = ((Candidates['Khan'])/Total_Votes)*100
    Percent_Correy = (Candidates['Correy']/Total_Votes)*100
    Percent_Li = (Candidates['Li']/Total_Votes)*100
    Percent_OTooley = (Candidates["OTooley"]/Total_Votes)*100
    
#Winner of election based on popular vote
    Winner = max(Candidates['Khan'],Candidates['Correy'],Candidates['Li'],Candidates["OTooley"])
#Print analysis to terminal
print(f'Election Results')
print(f'---------------------')
print(f'Total Votes: {Total_Votes}')
print(f'---------------------')
print(f'{Candidates}')
print(f'Khan: {Candidates["Khan"]} ({Percent_Khan}%)')
print(f'Correy: {Candidates["Correy"]} ({Percent_Correy}%)')
print(f'Li: {Candidates["Li"]} ({Percent_Li}%)')
print(f"O'Tooley: {Candidates["OTooley"]} ({Percent_OTooley}%)")
print(f'---------------------')
print(f'Winner: Khan')
#Create a text file with results