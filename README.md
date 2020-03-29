# Election_Analysis
The purpose of this module is to used Python Programming Language to: read and write text files, determine unique election candidates, total election votes as a whole, election votes-per-candidate, percentage of votes for each candidate, and determine the election winner based on the data in the given csv (our text file).

## Challenge
### Background
We know that not everyone has voted in this election, and the election commission wants Seth’s team to confirm the voter turnout for each county. In this challenge, you will help Seth and Tom determine the number of votes that were cast from each county and the percentage of votes each county contributed to the election.

To help Seth and Tom, you need to use for loops and conditional statements to calculate the voter turnout for each county as well as the percentage of votes each county contributed to the election. Then, determine which county had the largest turnout. Save the results to  election_results.txt with your previous election analysis results. To test your code, make sure you also print your results to the output terminal.

### Objectives
The goals of this challenge are for you to:

Extend your use of for loops and conditionals with membership and logical operators.
Scope and refactor code to provide additional information.
Write data to an output file and print the file.

### Instructions
1) Make a copy of the PyPoll.py file that you used throughout this module and rename it PyPoll_Challenge.py.
2) Create a list for the counties.
3) Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
4) Create an empty string that will hold the county name that had the largest turnout.
5) Declare a variable that represents the number of votes that a county received. Hint: Inside a for loop, add an if statement        to check if the county name has already been recorded. If not, add it to the list of county names.
6) Inside the with open() function where you are outputting the file, do the following:
   -Create three if statements to print out the voter turnout results similar to the results shown above.
   -Add the results to the output file.
   -Print the results to the command line.
