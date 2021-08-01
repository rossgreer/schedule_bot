# Evie's Schedulebot program
### Sort Events
import datetime  
import keyboard
import pyttsx3
import time
import sys


def time_to_float(time1):
    # Takes a military time string, and converts to a decimal
    '''
    Example: 
    16:30
    30/60 = 0.5
    16 + 0.5 = 16.5
    16:40
    40/60 = 0.666666666
    16.666666
    '''
    # find out where the colon part is
    colon_position = time1.find(":") 
    hour = time1[:colon_position] # everything from beginning up to colon
    minutes = time1[colon_position+1:] # everything past colon to the end

    hour_int = int(hour)
    minutes_int = int(minutes)

    # turn the 30 into 30/60 = .5
    minutes_decimal = minutes_int/60

    # add it to the 16
    final_time = hour_int + minutes_decimal

    return final_time

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

    # TODO: figure out the current time
    current_time = str(datetime.datetime.now())
    
    # Extract features from current_time: year, month, date, hour, minutes
    current_year = current_time[0:4]
    current_month = current_time[5:7]
    current_date = current_time[8:10]
    current_hour = current_time[11:13]
    current_minute = current_time[14:16]

    # How do we check if the event is in the past?
    ## MM/DD/YY
    event_year = event_complete_date[6:8]
    event_month = event_complete_date[0:2]
    event_date = event_complete_date[3:5]

    if event_year < current_year:
        return True
    elif event_month < current_month and event_year == current_year:
        return True
    elif event_date < current_date and event_month == current_month:
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
    
    #Fix problem here for homework
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


def reminder_date_at_least_month_before_event(event_date, reminder_date):
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
    #check the month and day
    #if True, return True, if False, return False


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
    
    error_flag = False
    if len(event.name) > 300:
        print("This event is invalid; more than 300 characters. ")
        error_flag = True
    elif not validDate(event.date):
        print("Event date is not in valid date format; cannot be added.")
        error_flag = True
    elif not validDate(event.reminder_date):
        print("Reminder date is not in valid date format; cannot be added.")
        error_flag = True
    elif not validMilitaryTime(event.time):
        print("Event is not in valid military time format; cannot be added.")
        error_flag = True
    elif not validMilitaryTime(event.reminder_time):
        print("Reminder is not in valid military time format; cannot be added.")
        error_flag = True



    error_flag2 = False
    if not error_flag:
        if eventIsInThePast(event.date, event.time):
            print("Event is in the past; cannot be added.")
            error_flag2 = True
        elif not two_years_future(event.date):
            print("Event is more than two years in the future; cannot be added.")
            error_flag2 = True
        elif not reminder_date_at_least_month_before_event(event.date, event.reminder_date):
            print("Event is not at least one month before the event.")
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


#homework: write this function:

def convert_date_string_format(date_with_dashes):
    dwd_month = date_with_dashes[5:7]
    dwd_day = date_with_dashes[8:10]
    dwd_year = date_with_dashes[2:4]
    dwd_combined = dwd_month + "/" + dwd_day + "/" + dwd_year
    '''
    Example:
        input is a string, formatted as YYYY-MM-DD
        output should be a string, formatted as MM/DD/YYYY
        So, 2021-05-16 should become 05/16/2021
    '''
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
            if time_to_float(current_time_one) >= time_to_float(reminder_time) and current_date_myd == reminder_date:
                reminder_str = "{} is coming up at {} on {} ".format(event.name, event.time, event.date)
                print(reminder_str)
                engine = pyttsx3.init()
                newVoiceRate = 145
                engine.setProperty('rate',newVoiceRate)
                engine.say(reminder_str)
                engine.runAndWait()
                event.reminded = True
    #check if they are equal
    #remind for 2 minutes
    # if they are, give reminder


if __name__ == '__main__':
    # We need to put events in!
    # We need to store event time, event date, when to be reminded

    ## AREA FOR TESTING FUNCTIONS 
    #test_functions()
    ## END TESTING

    event_limit = 100
    events_list = []
    #temp_events_list = [Event("Walk the dog","9:45","05/23/2021","05/23/2021", "9:25")]
    infinity_counter = 0

    while True: #and infinity_counter < 1000000:

        ### TODO: Check if reminder should be issued 
        #print("Checking for reminders...")
        checkForReminders(events_list)
        #infinity_counter += 1
        if keyboard.is_pressed('n'):  # if key 'q' is pressed 
            print('You Pressed the n key to make a new event!')
            time.sleep(1)
            sys.stdout.flush()
            valid_event = False
            while not valid_event:
                event_name = input("Enter event name. ")
                event_date = input("Enter month, date, and year as MM/DD/YY. ")
                event_time = input("Enter event time. ")
                event_reminder_date = input("What date would you like to be reminded? ")
                event_reminder_time = input("What time would you like to be reminded? ")

                ourFirstEvent = Event(event_name, event_time, event_date, event_reminder_date, event_reminder_time)
                valid_event = checkValidEvent(ourFirstEvent)

                print("This is our first event: " + str(ourFirstEvent))
                print("Does this event pass all the tests? "+str(valid_event))

                if valid_event:
                    events_list += [ourFirstEvent]
                    print("Event added! ScheduleBot is ready to send reminders.")
                else:
                    pass

        ## TODO: Check if user is pressing 'n' for 'new' to add a new event. 
        # Everything seems fine but whenever I put an event in, it says it's in the past, even though it's not.