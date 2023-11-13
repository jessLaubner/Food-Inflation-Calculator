#Program to display how the inflation rate on food has changed grocery shopping in 2023


#pre-pandemic, I could get away with spending $300 on groceries for a family of 4, and it would
#last for close to two weeks. This is including the extra costs of me using
#InstaCart.

#This program shows exactly why grocery shopping has drastically changed
#in the last 3 years.



#variables

groceryBill = 300

#forloop

#counterVariable = years
#startingValue = 2020
#maxValue = 2024

for num in range (2020,2024):
    increase = groceryBill * 0.11
    groceryBill = groceryBill + (groceryBill * 0.11)
    groceryNow = int(float(groceryBill + (groceryBill * 0.11)))
    print('In',num,'groceries went up by $',increase)
    print('and total cost is $',groceryNow)
   
#end for
   
#The End :)
