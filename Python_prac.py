#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
    #print(counties[1])

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
  #  print("Turn on the AC.")
#else:
 #   print("Open the windows.")

#What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
   # print('Your grade is an A.')
#elif score >= 80:
    #print('Your grade is a B.')
#elif score >= 70:
    #print('Your grade is a C.')
#elif score >= 60:
    #print('Your grade is a D.')
#else:
    #print('Your grade is an F.')

#if "El Paso" in counties:
   # print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not the list of counties.")



#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
   # f"You received {candidate_votes} number of votes. "
   # f"The total number of votes in the election was {total_votes}. "
   # f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)
#message_to_candidate = (
  #  f"You received {candidate_votes:,} number of votes. "
  #  f"The total number of votes in the election was {total_votes:,}. "
  #  f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#Below is how I would find the path to a file
#Resources/election_analysis.csv

# WORKING WITH DEPENDENCIES
#Import the datetime class from the datetime module
#import datetime as dt   
#Use the now() attribute on the datetime class to get the current time
#now = dt.datetime.now()
#Print the present time.
#print("The time right now is, ", now)

#  NOW, LET'S LOOK AT HOW TO USE THE CSV MODULE
#import datetime (this is a module)
#print(dir(datetime))

#import csv
#print (dir(csv))

#IMPORTANT DATA TYPES AND STRUCTURES
#INT, FLOAT, BOOL, LIST, TUPLE, DICT, DATETIME

#  IMPORTANT MODULES
#CSV, RANDOM, NUMPY

file_to_load = 'Resources/election_results.csv'
# Open the election results and READ the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

#if I want a more efficient set of code, I can use a "with" statement
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)


