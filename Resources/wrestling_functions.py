import os
import csv

# Path to collect data from the Resources folder
file_to_load = 'wwe-data-2016.csv'

# Define the function and have it accept the 'wrestlerData' as its sole parameter

def print_percentages(row):
    name = row[0]
    wins = int row[1]
    loss = int row[2]
    draw = int row [3]
# Find the total number of matches wrestled
  sum = wins + loss + draw

# Find the percentage of matches won
  print(wins/sum)

# Find the percentage of matches lost
  print(loss/sum)

# Find the percentage of matches drawn
  print(draw/sum)

# Print out the wrestler's name and their percentage stats
def wrestlers_name():
    print(f"{name}, {wins}, {loss}, {draw}")

# Read in the CSV file
#with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    #for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        #if(name_to_check == row[0]):
            #print_percentages(row)
