# CSC500 - Critical Thinking - Part 2 - Matthew Bayne
#====================================================

#Input current time in 24hr format
time_current = int(input('Enter the current time in the 24 hour format (HH): '))
time_wait = int(input('Enter how many hours to wait till your alarm goes off: '))

#Calculate time
time_total = time_current + time_wait
time_wait_days = time_total // 24 #Floor division by 24 to get an integer for # of days.
time_wait_hours = time_total % 24 #Modulo by 24 to get the left over hours

#Check for am/pm
if time_wait_hours > 11: #Since 12pm is noon and assuming only ints.
    am_pm = 'pm'
else:
    am_pm = 'am'

#Check for days or not and output alarm time
if time_wait_days > 0:
    print('Your alarm will go off at {0}{1} in {2} days.'.format(time_wait_hours, am_pm, time_wait_days))
else:
    print('Your alarm will go off at {0}{1} later today.'.format(time_wait_hours, am_pm))