# CSC500 - Critical Thinking - Part 1 - Matthew Bayne
#====================================================

#Setup Header
print('Average Rainfall Calculator')
print('---------------------------')

#Setup Month Dictionary, initialize variable
month_data = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
total_rainfall = 0

#Take input, calculate months from years.
total_years = int(input('Please input the number of years: '))
total_months = total_years * 12

for year in range(0, (total_years), 1): #Iterate over the number of years
    for month in range(1, 13): #Iterate over 12 months
        current_rainfall = float(input('How many inches of rainfall for {}: '.format(month_data[month]))) #Float to account for small rainfall amounts
        total_rainfall += current_rainfall #Add to total rainfall

average_rainfall = total_rainfall / total_months

print('\nTotal months: {} months'.format(total_months))
print('Total inches of rainfall: {:.2f} inches'.format(total_rainfall))
print('Average rainfall per month: {:.2f} inches'.format(average_rainfall))