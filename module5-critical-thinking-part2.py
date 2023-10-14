# CSC500 - Critical Thinking - Part 2 - Matthew Bayne
#====================================================

'''
Input number of books this month
Var points equals 0

If book number is >= 8
    points = 60
Else If book numer is >= 6 And book number is <= 7
    points = 30
Else If book numer is >= 4 And book number is <= 5
    points = 15
Else If book numer is >= 2 And book number is <= 3
    points = 5
Else
    ponts = 0

Output points
'''

print('Welcome to the CSU Global Bookstore Book Club Points Calculator, CGBBCPC!')
books_number = int(input('Please enter the number of books purchased this month: \n'))

reward_points = 0
additional_message = 'You should buy more books!'

if books_number >= 8:
    reward_points = 60
    additional_message = 'Great job!'
elif (books_number >= 6) and (books_number <= 7):
    reward_points = 30
    additional_message = 'Doin\' pretty good!'
elif (books_number >= 4) and (books_number <= 5):
    reward_points = 16
    additional_message = 'Adequate.'
elif (books_number >= 2) and (books_number <= 3):
    reward_points = 5
    additional_message = 'I guess that\'s better than nothing.'

print('You have been awarded {} CGBBCPC points this month! {}'.format(reward_points, additional_message))