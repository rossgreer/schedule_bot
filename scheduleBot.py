# Evie's Schedulebot program
### Sort Events
import datetime  



def time_to_int(time1):
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
    # “find out where the colon part is”
    colon_position = time1.find(":") 
    hour = time1[:colon_position] # everything from beginning up to colon
    minutes = time1[colon_position+1:] # everything past colon to the end

    hour_int = int(hour)
    minutes_int = int(minutes)

    # “turn the 30 into 30/60 = .5”
    minutes_decimal = minutes_int/60

    # “add it to the 16”
    final_time = hour_int + minutes_int

    return final_time

def time1_less_than_eq_time2(time1, time2):
    # Given two times, return ‘True’ if time1 is less than or equal to time2.
    # Return ‘False’ otherwise
    # time1 and time2 are each strings, in military time. 
  
    if time_to_int(time1) <= time_to_int(time2):
        return True
    else:
        return False
    
def sort_events(list_of_events, list_of_times):
    start_of_list_iteration = 0
    while start_of_list_iteration < len(list_of_events): 

        for index, num in enumerate(list_of_events):
            candidate_1_position = index
            candidate_1_time = list_of_times[index]
            candidate_1_event = list_of_events[index]

            candidate_2_position = index+1
            if candidate_2_position < len(list_of_times):
                candidate_2_time = list_of_times[index+1]
                candidate_2_event = list_of_events[index+1]

                # if candidate_1_value <= candidate_2_value:
                # if “18:30” <= “17:00” ←- this would give an error, we don’t know how to compare 2 strings
                if time1_less_than_eq_time2(candidate_1_time, candidate_2_time): 
                
                    # move our ‘red boxes’ forward to the next pair
                    continue
                else: 
                    # switch the numbers order
                    # take the first candidate, put it where the second candidate was.
                    list_of_times[candidate_2_position] = candidate_1_time
                    list_of_events[candidate_2_position] = candidate_1_event

                    # take second candidate, put it where first candidate was. 
                    list_of_times[candidate_1_position] = candidate_2_time
                    list_of_events[candidate_1_position] = candidate_2_event
                
        start_of_list_iteration += 1

    return list_of_times, list_of_events

#our_list_of_events = ["Study for test", "Do laundry", "Finish homework"]
#our_list_of_times = ["18:30","17:00","16:00"]
#new_list = sort_events(our_list_of_events, our_list_of_times)
#print(new_list)

class Event():

    def __init__(self, event_name, event_time, event_date, event_reminder_date, event_reminder_time):
        self.name = event_name
        self.time = event_time
        self.date = event_date
        self.reminder_date = event_reminder_date
        self.reminder_time = event_reminder_time

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

    event_year = event_complete_date[7:9]
    event_month = event_complete_date[0:2]
    event_date = event_complete_date[3:5]

    ## TODO NEXT TIME: Finish this logic!
    if the event year < current_year:

        return True



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

    if len(event.name) > 3:
        print("This event is invalid; more than 300 characters. ")
        return False
    elif eventIsInThePast(event.date, event.time):
        print("Event is in the past; cannot be added.")
        return False


    return True


if __name__ == '__main__':
    # We need to put events in!
    # We need to store event time, event date, when to be reminded

    ## AREA FOR TESTING FUNCTIONS 
    print("Testing Event In The Past")
    print("First date: 4/1/2021, should be False")
    current_time_check = eventIsInThePast("04/01/21","10:00")
    print("Second date: 3/3/2021, should be True")
    current_time_check = eventIsInThePast("03/03/21","10:00")


    ## END TESTING

    event_limit = 100
    events_list = []

    ## TODO: Need to press 'n' for 'new' to add event. 

    ## TODO: no more than 300 characters
    event_name = input("Enter event name.")
    ## TODO: event must be in the future, but not more than 2 years into the future
    event_date = input("Enter month, date, and year as MM/DD/YY.")
    ## TODO: Must be a valid military time
    event_time = input("Enter event time.")
    ## TODO: reminder can't be more than a month before a event
    event_reminder_date = input("What date would you like to be reminded?")
    ## TODO: must be a valid military time
    event_reminder_time = input("What time would you like to be reminded?")

    ourFirstEvent = Event(event_name, event_time, event_date, event_reminder_date, event_reminder_time)

    print(ourFirstEvent)

    print(checkValidEvent(ourFirstEvent))

    if checkValidEvent(ourFirstEvent):
        events_list += [ourFirstEvent]
    else:
        pass
        ## TODO: decide what to do with an invalid event

