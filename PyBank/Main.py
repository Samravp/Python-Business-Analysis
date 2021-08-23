import csv
import os

#path to collect data from the Resources folder
csvpath= os.path.join('Resources','budget_data.csv')

#open the csv and read through
with open(csvpath) as csvfile:
    
    #split the data on commas
     budget_dataset = csv.reader(csvfile, delimiter=',')
     
     #skip column headers
     header = next(budget_dataset)
     
     #Create a list that holds the data
     month_data= list(budget_dataset)

#calculate the total number of months included in the dataset    
num_months = len(month_data)

#loop to create a list of Profit/Lossess
profit_loss = [0]* num_months

for i in range(num_months):
    profit_loss[i] = float(month_data[i][1])
    
#find the net total amount of "Profit/Losses" over the entire period
total_pl = sum(profit_loss)
    
#loop to create a list of montly profit/loss changes

pl_change = [0]*(num_months-1)

for i in range(num_months-1):
    
    pl_change[i] = profit_loss[i+1]-profit_loss[i]

#calculate the average of the changes in "Profit/Losses" over the entire period      
avg_change=round(sum(pl_change)/(num_months-1),2)

#loop to calculate the greatest increase and decrease in profits date over the entire period
#greatest increase and decrease amounts are found through Min and Max functions 
for i in range(num_months-1):
    
    if pl_change[i] == max(pl_change):
        greatest_increase_month =(month_data[i+1][0])
        
    elif pl_change[i] == min(pl_change):
         greatest_decrease_month=(month_data[i+1][0])

#assign a variable to hold the information to print 
Financial_Analysis =(f"Financial Analysis\n\
---------------------------------\n\
Total Months: {num_months}\n\
Total : $ {round(total_pl)}\n\
Average Changes: {avg_change}\n\
Greatest Increase in Profits: {greatest_increase_month} (${round(max(pl_change))})\n\
Greatest Decrease in Profits: {greatest_increase_month} (${round(min(pl_change))})")

#print the analysis
print(Financial_Analysis)

#create a final text file and display analysis
f = open("Analysis/PyBank.txt", "w")
f.write(Financial_Analysis)
f.close()
