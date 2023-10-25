# CSC500 - Critical Thinking - Matthew Bayne
#====================================================

# Create a dictionary containing course numbers and their respective room numbers.
room_number_dict = {'CSC101': 3004, 'CSC102': 4501, 'CSC103': 6755, 'NET110': 1244, 'COM241': 1411}

# Create a dictionary containing course numbers and their respective instructor names.
instructors_dict = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}

# Create a dictionary containing course numbers and their respective meeting times.
meeting_time_dict = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.', 'COM241': '1:00 p.m.'}

# Merge the dictionaries for easier access
merged_dict = room_number_dict
for key in merged_dict.keys():
    merged_dict[key] = room_number_dict[key], instructors_dict[key], meeting_time_dict[key]

def getCourse():
    course = input('--> Enter a Course Number: ').upper()
    for key in merged_dict.keys():
        if course == key:
            print('\nCourse Number Found!')
            print('**********************')
            print('Course Number: {}'.format(key))
            print('Room Number: {}'.format(merged_dict[key][0]))
            print('Instructor Name: {}'.format(merged_dict[key][1]))
            print('Meeting Time: {}'.format(merged_dict[key][2]))
            return
    print('\nThere\'s no course with that number, \'{}\'.'.format(course))

def getRoom():
    room_number = input('--> Enter a Room Number: ')
    try:
        room_number = int(room_number)
        for key in merged_dict.keys():
            if room_number == merged_dict[key][0]:
                print('\nRoom Number Found!')
                print('**********************')
                print('Course Number: {}'.format(key))
                print('Room Number: {}'.format(merged_dict[key][0]))
                print('Instructor Name: {}'.format(merged_dict[key][1]))
                print('Meeting Time: {}'.format(merged_dict[key][2]))
                return
        print('\nThere\'s no room with that number, \'{}\'.'.format(room_number))
    except (ValueError):
        print('Wrong value, enter only a number next time!')

def getInstructor():
    name = input('--> Enter an Instructor\'s Last Name: ').capitalize()
    for key in merged_dict.keys():
        if name == merged_dict[key][1]:
            print('\nInstructor Found!')
            print('**********************')
            print('Course Number: {}'.format(key))
            print('Room Number: {}'.format(merged_dict[key][0]))
            print('Instructor Name: {}'.format(merged_dict[key][1]))
            print('Meeting Time: {}'.format(merged_dict[key][2]))
            return
    print('\nThere\'s no instructor with the last name, \'{}\'.'.format(name))

def getMeetingTime():
    meeting_time = input('--> Enter a Course Meeting Time: ').lower()
    for key in merged_dict.keys():
        if meeting_time == merged_dict[key][2]:
            print('\nMeeting Time Found!')
            print('**********************')
            print('Course Number: {}'.format(key))
            print('Room Number: {}'.format(merged_dict[key][0]))
            print('Instructor Name: {}'.format(merged_dict[key][1]))
            print('Meeting Time: {}'.format(merged_dict[key][2]))
            return
    print('\nThere\'s no course with that meeting time, \'{}\'.'.format(meeting_time))

quit_ui = False
while quit_ui != True:
    print('\n*=================================*')
    print('*||       Welcome to the        ||*')
    print('*||     Course Compendium!      ||*')
    print('*||-----------------------------||*')
    print('*|| Enter any of the following: ||*')
    print('*|| -Course Number (n)          ||*')
    print('*|| -Course Room (r)            ||*')
    print('*|| -Instructor\'s Last Name (i) ||*')
    print('*|| -Course Meeting Time (t)    ||*')
    print('*|| -Quit (q)                   ||*')
    print('*=================================*\n')
    user_in = input('--> ').lower()
    if user_in[0] == 'q':
        print('--> Quitting now...')
        quit_ui = True
    elif user_in[0] == 'n':
        getCourse()
    elif user_in[0] == 'r':
        getRoom()
    elif user_in[0] == 'i':
        getInstructor()
    elif user_in[0] == 't':
        getMeetingTime()
    else:
        print('Please enter valid input!')
