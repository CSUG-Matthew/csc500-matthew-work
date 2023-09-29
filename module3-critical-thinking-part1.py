# CSC500 - Critical Thinking - Part 1 - Matthew Bayne
#====================================================

#Input food cost
food_cost = float(input('Please enter the cost of your food: $'))

#Calculate Values
sales_tax = food_cost * 0.07 #7% Sales Tax
food_tip = food_cost * 0.18 #18% Food Tip
total_price = food_cost + sales_tax + food_tip

#Output Values to two decimal points
print('Sales Tax (7%): ${0:.2f}'.format(sales_tax))
print('Food Tip (18%): ${0:.2f}'.format(food_tip))
print('Total Price: ${0:.2f}'.format(total_price))