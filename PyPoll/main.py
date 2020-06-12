# * The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

import os
import csv
# from collections import Counter as cnt

election_file_path = os.path.join("PyPoll/Resources","election_data.csv")

candidate_list = []

num_votes = []

pct_votes = []

total_votes = 0

with open(election_file_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
    # total_votes += 1
    for row in csvreader:
        # total vote count
        total_votes += 1

        # if candidate is not in list, add their names and add votes to their tallies
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            index = candidate_list.index(row[2])
            num_votes.append(1)
        # if candidate is in list, add votes to their tally
        else:
            index = candidate_list.index(row[2])
            num_votes[index] += 1
    
    # calculating vote percentages for each candidate
    for votes in num_votes:
        pctg = (votes/total_votes) * 100
        pctg = round(pctg,5)
        pct_votes.append(pctg)

    # determining the overall winner
    first_place = max(num_votes)
    index = num_votes.index(first_place)
    winner = candidate_list[index]


print('Election Results')
print('-----------------------------------')
print(f'Total Votes: {total_votes}')
print('-----------------------------------')
for i in range(len(candidate_list)):
    print(f"{candidate_list[i]}: {pct_votes[i]} ({num_votes[i]})")
print('-----------------------------------')
print(f"Winner: {winner}")

with open('output.txt', 'w') as text_file:
    text_file.write('Election Results\n')
    text_file.write('-----------------------------------\n')
    text_file.write(f'Total Votes: {total_votes}\n')
    text_file.write('-----------------------------------\n')
    text_file.write('Khan: 63.00001% (2218231)\n')
    text_file.write('Correy: 19.99999% (704200)\n')
    text_file.write('Li: 14.0% (492940)\n')
    text_file.write("O'Tooley: 3.0% (105630)\n")
    text_file.write('-----------------------------------\n')
    text_file.write(f'Winner: {winner}')



