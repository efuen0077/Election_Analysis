#import csv

#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
    # print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1.Initialize total vote counter
total_votes = 0

# Declare a new list
candidate_options = []

# 1. Declare empty dictionary (we are using this to find total votes for each candidate)
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1
        
        #can also be written as total_votes = total_votes + 1
        
        #Print the candidate name from each row
        candidate_name = row[2]

        #We need ONLY unique candidate names
        if candidate_name not in candidate_options:
        #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #2. Begin tracking candidate vote count
            # name_of_dictionary[key] = 0
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    #the value associated with our key in the dictionary
    votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate}: received {vote_percentage: .1f}% of the vote.") 

   # To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     #vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate  

winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)


#Print candidate vote dictionary
#print(candidate_votes)
#Print the candidate list
#print(candidate_options)

# 3. Print the total votes
#print(total_votes)



    # Print the file object.
    # print(election_data)
# --------------------------------------------------------

# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
# Close the file
#outfile.close()

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")
    

#txt_file.close()