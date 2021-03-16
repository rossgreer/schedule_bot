### Sort Events

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


our_list_of_events = ["Study for test", "Do laundry", "Finish homework"]
our_list_of_times = ["18:30","17:00","16:00"]
new_list = sort_events(our_list_of_events, our_list_of_times)
print(new_list)
