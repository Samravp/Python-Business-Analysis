import csv
import os

#path to collect data from the Resources folder
csvpath= os.path.join('Resources','election_data.csv')

#read in the CSV file
with open(csvpath) as csvfile:
     #split the data on commas
     election_dataset = csv.reader(csvfile, delimiter=',')
     
     #skip column headers
     header = next(election_dataset)
     
     #Create a list that holds the data
     election_data= list(election_dataset)

#calculate the total number of months included in the dataset    
num_votes = len(election_data)

#initialisation of value
candidate_list=['']*num_votes

#loop to create a list of candidates in the data set
for i in range(num_votes):
    candidate_list[i] = (election_data[i][2])

#find out unique values in the candidate list using set function
unique_candidates = list(set(candidate_list))
num_candidates=len(unique_candidates)

#initialise candidate votes to start at zero
votes = [0]*num_candidates

#loop through election data to calculate votes of each candidate
for i in range(num_votes):
    
      for j in range(num_candidates):
          
           if candidate_list[i] == unique_candidates[j]:
    
               votes[j] += 1
               
#calculate percentage of votes
#define a  python function to multiply all values in the list using traversal
 
def percentList(mylist):
    
    result = [0]*len(mylist)
    for i in range(len(mylist)):
         result[i] = round((mylist[i]/sum(mylist))*100)
    return result

#define a variable that holds percent of votes for each candidate
percent_votes = percentList(votes)

#zip lists together  to sort them in descending order
candidate_percent = list(zip(unique_candidates, percent_votes, votes))

#define a function to sort lists in descending order
def sorter(item):
    # Since highest votes first, least error = most votes
    vote_pt = 100-item[1]
    return vote_pt

#use the defined function to sort the list
sorted_list = sorted(candidate_percent, key=sorter)

#define a variable named text that holds information 
text = (f"Election Results\n\
-------------------------\n\
Total Votes : {num_votes}\n\
-------------------------\n")

#loop through final sorted list to print the candidate info

for i in range(4):
    text += (f"{sorted_list[i][0]}: {(sorted_list[i][1])}.000% ({sorted_list[i][2]})\n")
    
#define a variable that displays winner's name                     
winner_text = (f"-------------------------\n\
Winner: {sorted_list[0][0]}\n\
-------------------------")
#print variables
print(text + winner_text)

#create a text file and print the texts
f = open("Analysis/PyPoll.txt", "w", newline="")
f.write(text + winner_text)
f.close()


    


