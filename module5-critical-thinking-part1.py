# CSC500 - Critical Thinking - Part 1 - Matthew Bayne
#====================================================

'''
Input number of years
Var rainfall data

For year in years
    For month in 12 months
        Input monthly rainfall

Output total months
Output total rainfall
Output average rainfall
'''

print('Average Rainfall Calculator')
print('---------------------------')

month_data = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
rainfall_data = {}
total_rainfall = 0

total_years = int(input('Please input the number of years: '))
total_months = total_years * 12

for year in range(0, (total_years), 1):
    for month in range(1, 13, 1):
        current_rainfall = int(input('How many inches of rainfall for {}: '.format(month_data[month])))
        rainfall_data.update({((year * 12) + month):current_rainfall})
        total_rainfall += current_rainfall

average_rainfall = total_rainfall / total_months

print('Total months: {} months'.format(total_months))
print('Total inches of rainfall: {:.2f} inches'.format(total_rainfall))
print('Average rainfall per month: {:.2f} inches'.format(average_rainfall))