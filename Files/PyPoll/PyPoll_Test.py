import os
import csv
# Establishing lists
ballotid_list = []
county_list = []
candidate_list = []
# Designating the file that I want to use and the path to it 
csvpath = os.path.join("Resources","election_data.csv")
# Read data from CSV and populate ballotid_list and candidate_list
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skipping the header row
    csv_header = next(csvreader)
    # Establishing a loop that goes through each row of the file
    for row in csvreader:
        ballotid_list.append(row[0])
        candidate_list.append(row[2])
# Counting the number of items in the ballotid_list
len(ballotid_list)
print("Election Results")
print("Total Votes:", len(ballotid_list))
# Count the votes for each candidate
vote_counts = {}
for candidate in candidate_list:
    if candidate in vote_counts:
        vote_counts[candidate] += 1
    else:
        vote_counts[candidate] = 1
# Calculate total number of votes
total_votes = len(candidate_list)
# Print the results
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    print("{}: {:.2f}% ({})".format(candidate, percentage, votes))
# Find the winner
max_votes = 0
winner = None
for candidate in vote_counts:
    if vote_counts[candidate] > max_votes:
        max_votes = vote_counts[candidate]
        winner = candidate
# Print the winner
print("Winner:", winner)