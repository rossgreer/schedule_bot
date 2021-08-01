import datetime  
import keyboard
import pyttsx3
import time
import sys

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
                # if 18:30 <= 17:00 this would give an error, we dont know how to compare 2 strings
                if time1_less_than_eq_time2(candidate_1_time, candidate_2_time): 
                
                    # move our red boxes forward to the next pair
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