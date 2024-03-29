# Evie's Schedulebot program
import datetime  
import keyboard
import pyttsx3
import time
import sys


def time1_less_than_eq_time2(time1, time2, date1, date2):
    # Given two times, return True if time1 is earlier than or equal to time2.
    # Return False otherwise
    # time1 and time2 are each strings, in military time.
    # date should be MM/DD/YYYY

    date1_year, date1_month, date1_day = int(date1[6:10]), int(date1[0:2]), int(date1[3:5])
    date2_year, date2_month, date2_day = int(date2[6:10]), int(date2[0:2]), int(date2[3:5])
    time1_hour, time1_minute = int(time1[0:2]), int(time1[3:5])
    time2_hour, time2_minute = int(time2[0:2]), int(time2[3:5])

    if date1_year < date2_year:
        return True 
    elif date1_year > date2_year:
        return False
    elif date1_month < date2_month:
        return True
    elif date1_month > date2_month:
        return False
    elif date1_day < date2_day:
        return True
    elif date1_day > date2_day:
        return False
    elif time1_hour < time2_hour:
        return True
    elif time1_hour > time2_hour:
        return False
    elif time1_minute < time2_minute:
        return True
    elif time1_minute > time2_minute:
        return False
    else:
        return True
    
def sort_events(list_of_events):
    #this function sorts a list of events in chronological order.
    start_of_list_iteration = 0
    while start_of_list_iteration < len(list_of_events): 

        for index, num in enumerate(list_of_events):
            candidate_1_position = index
            candidate_1_time = list_of_events[index].time
            candidate_1_event = list_of_events[index]
            candidate_1_date = list_of_events[index].date

            candidate_2_position = index+1
            if candidate_2_position < len(list_of_events):
                candidate_2_time = list_of_events[index+1].time
                candidate_2_event = list_of_events[index+1]
                candidate_2_date = list_of_events[index+1].date

                if not time1_less_than_eq_time2(candidate_1_time, candidate_2_time, candidate_1_date, candidate_2_date):
                    # switch the numbers order
                    # take the first candidate, put it where the second candidate was.
                    list_of_events[candidate_2_position] = candidate_1_event

                    # take second candidate, put it where first candidate was.
                    list_of_events[candidate_1_position] = candidate_2_event

        start_of_list_iteration += 1

    return list_of_events


class Event():

    def __init__(self, event_name, event_time, event_date, event_reminder_date, event_reminder_time):
        self.name = event_name
        self.time = event_time
        self.date = event_date
        self.reminder_date = event_reminder_date
        self.reminder_time = event_reminder_time
        self.reminded = False

    def __str__(self):
        return self.name

def eventIsInThePast(event_complete_date, event_time):
    ## Returns 'True' if the event is in the past
    ## Returns 'False' otherwise

    current_time = str(datetime.datetime.now())
    
    # Extract features from current_time: year, month, date, hour, minutes
    current_year = current_time[0:4]
    current_month = current_time[5:7]
    current_date = current_time[8:10]
    current_hour = current_time[11:13]
    current_minute = current_time[14:16]

    event_year = event_complete_date[6:8]
    event_month = event_complete_date[0:2]
    event_date = event_complete_date[3:5]

    if event_year < current_year:
        return True
    elif event_month < current_month and event_year == current_year:
        return True
    elif event_date < current_date and event_month == current_month:
        return True
    elif event_date == current_date and event_time < current_time:
        return True
    else:
        return False

def two_years_future(event_date):
    ## Returns 'True' if the event is within the next two years
    ## Returns 'False' otherwise
    current_time = str(datetime.datetime.now())
    event_year = event_date[6:8]
    current_year = current_time[2:4]
    event_month = event_date[0:2]
    current_month = current_time[5:7]
    
    if int(event_year)-2 < int(current_year):
        return True
    elif int(event_year)-2 == int(current_year) and int(event_month) <= int(current_month):
        return True
    else:
        return False

def validMilitaryTime(event_time):
    ## Returns 'True' if time is valid military time
    ## Returns 'False' otherwise
    try:
        int(event_time[0:2])
    except ValueError:
        return False

    try:
        int(event_time[3:5])
    except ValueError:
        return False

    event_hour = int(event_time[0:2])
    event_minute = int(event_time[3:5])
    if event_hour < 24 and event_minute < 60:
        return True
    else:
        return False

def validDate(event_date):
    ## if it is, return True, if not, return False    
    ## Returns 'True' if the date is a valid date
    ## Returns 'False' otherwise
    ## Valid dates should be in the format MM/DD/YYYY
    if event_date[2] != '/':
        return False
    if not event_date[5] == '/':
        return False
    try:
        int(event_date[0:2])
    except ValueError:
        return False
    try:
        int(event_date[3:5])
    except ValueError:
        return False
    try:
        int(event_date[6:10])
    except ValueError:
        return False
        
    return True


def reminder_date_within_a_month_of_event(event_date, reminder_date):
    #MM/DD/YY (event date)
    #MM/DD/YY (reminder)

    reminder_year = reminder_date[6:8]
    reminder_month = reminder_date[0:2]
    reminder_day = reminder_date[3:5]

    event_year = event_date[6:8]
    event_month = event_date[0:2]
    event_day = event_date[3:5]

    if int(reminder_year) == int(event_year):
        return True
    elif int(event_month) >= int(event_month)-1 and int(event_day) < int(event_day): 
        return True
    else:
        return False


def checkValidEvent(event):
    ## Returns 'True' if this is a valid event
    ## Returns 'False' otherwise, and prints what is invalid
    ## Criteria:
    ##    name is less than or equal to 300 characters
    ##    event is in the future
    ##    event is less than two years in the future
    ##    time is valid military time
    ##    reminder date is not more than a month before the event
    ##    reminder time is a valid military time
    
    error_flag, error_flag2 = False, False
    if len(event.name) > 300:
        print("This event is invalid; more than 300 characters. ")
        error_flag = True
    elif not validDate(event.date) or not validDate(event.reminder_date):
        print("Event or reminder date is not in valid date format; cannot be added.")
        error_flag = True
    elif not validMilitaryTime(event.time) or not validMilitaryTime(event.reminder_time):
        print("Event or reminder is not in valid military time format; cannot be added.")
        error_flag = True

    if not error_flag:
        if eventIsInThePast(event.date, event.time) or eventIsInThePast(event.reminder_date, event.reminder_time):
            print("Event or reminder is in the past; cannot be added.")
            error_flag2 = True
        elif not two_years_future(event.date):
            print("Event is more than two years in the future; cannot be added.")
            error_flag2 = True
        elif not reminder_date_within_a_month_of_event(event.date, event.reminder_date):
            print("Reminder is not within one month of the event.")
            error_flag2 = True

    return not error_flag and not error_flag2

def test_functions():
    print("FUNCTION TESTS")
    print("Testing Event In The Past")
    print("First date: 4/22/2021, should be False")
    current_time_check = eventIsInThePast("04/22/21","10:00")
    print("Result: "+str(current_time_check))
    print("Second date: 3/3/2021, should be True")
    current_time_check = eventIsInThePast("03/03/21","10:00")
    print("Result: "+str(current_time_check))
    print("Testing Two Years Future")
    print("First date: 5/4/2022, should be True")
    current_time_check = two_years_future("05/04/22")
    print("Result: "+str(current_time_check))
    print("Second date: 1/4/2072, should be False")
    current_time_check = two_years_future("01/04/72")
    print("Result: "+str(current_time_check))
    print("Testing Valid Military Time")
    print("Time: meow, should be False")
    current_time_check = validMilitaryTime("meow")
    print("Result: "+str(current_time_check))
    print("Time: 1:0, should be False")
    current_time_check = validMilitaryTime("1:0")
    print("Result: "+str(current_time_check))
    print("Time: me:ow, should be False")
    current_time_check = validMilitaryTime("me:ow")
    print("Result: "+str(current_time_check))
    print("Time: 24:59, should be False")
    current_time_check = validMilitaryTime("24:59")
    print("Result: "+str(current_time_check))
    print("Time: 07:60, should be False")
    current_time_check = validMilitaryTime("07:60")
    print("Result: "+str(current_time_check))
    print("Time: 107:60, should be False")
    current_time_check = validMilitaryTime("107:60")
    print("Result: "+str(current_time_check))
    print("Time: 10:50, should be True")
    current_time_check = validMilitaryTime("10:50")
    print("Result: "+str(current_time_check))
    print("Time: 01:06, should be True")
    current_time_check = validMilitaryTime("01:06")
    print("Result: "+str(current_time_check))
    print("Testing Valid Date")
    print("Date: meow, should be False")
    current_time_check = validDate("meow")
    print("Result: "+str(current_time_check))
    print("Date: 21452839, should be False")
    current_time_check = validDate("21452839")
    print("Result: "+str(current_time_check))
    print("Date: 05/02/2021, should be True")
    current_time_check = validDate("05/02/2021")
    print("Result: "+str(current_time_check))
    print("Date: me/owwwww, should be False")
    current_time_check = validDate("me/owwwww")
    print("Result: "+str(current_time_check))


def convert_date_string_format(date_with_dashes):
    '''
    Example:
        input is a string, formatted as YYYY-MM-DD
        output should be a string, formatted as MM/DD/YYYY
        So, 2021-05-16 should become 05/16/2021
    '''
    dwd_month = date_with_dashes[5:7]
    dwd_day = date_with_dashes[8:10]
    dwd_year = date_with_dashes[2:4]
    dwd_combined = dwd_month + "/" + dwd_day + "/" + dwd_year
    return dwd_combined

def checkForReminders(events_list):
    current_time = str(datetime.datetime.now())
    current_date_myd = convert_date_string_format(current_time[0:10])
    current_date = current_time[8:10]
    current_hour = current_time[11:13]
    current_minute = current_time[14:16]
    current_time_one = current_time[11:16]
    for event in events_list:
        reminder_time = event.reminder_time
        reminder_date = event.reminder_date
        if event.reminded == False:
            if time1_less_than_eq_time2(reminder_time, current_time_one, reminder_date, current_date_myd):
                reminder_str = "{} is coming up at {} on {} ".format(event.name, event.time, event.date)
                print(reminder_str)
                sys.stdout.flush()

                engine = pyttsx3.init()
                newVoiceRate = 145
                engine.setProperty('rate',newVoiceRate)
                engine.say(reminder_str)
                engine.runAndWait()
                event.reminded = True

if __name__ == '__main__':
    event_limit, events_list = 100, []
    while True:
        checkForReminders(events_list)
        if keyboard.is_pressed('p'):
            print("You pressed the p key to print your events!\n")
            sys.stdout.flush()
            sorted_event_list = sort_events(events_list)
            for event in sorted_event_list:
                print(event.name + ", on " + event.date + ", at " + event.time)
            sys.stdout.flush()
            time.sleep(1)
        if keyboard.is_pressed('n'):  # if key 'n' is pressed 
            print('You Pressed the n key to make a new event!')
            time.sleep(1)
            sys.stdin.flush()
            sys.stdout.flush()
            valid_event = False
            while not valid_event:
                event_name = input("Enter event name. ")
                event_date = input("Enter month, date, and year as MM/DD/YY. ")
                event_time = input("Enter event time. ")
                event_reminder_date = input("What date would you like to be reminded? ")
                event_reminder_time = input("What time would you like to be reminded? ")
                sys.stdout.flush()
                ourFirstEvent = Event(event_name, event_time, event_date, event_reminder_date, event_reminder_time)
                valid_event = checkValidEvent(ourFirstEvent)
                print("Does this event pass all the tests? "+str(valid_event)+"\n")
                sys.stdout.flush()
                if valid_event:
                    events_list += [ourFirstEvent]
                    print("Event added! ScheduleBot is ready to send reminders.\n")
                    sys.stdout.flush()