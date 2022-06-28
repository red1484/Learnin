import time
import datetime
import json
from os.path import exists


def countdown(timer_name, total_seconds):
    print(f"Current timer: {timer_name}")
    while total_seconds > 0:
 
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
 
    



timers_dict = {}        #stores the timer in dictionary
saved_timer = ""        #y or n if user has a saved timer
timer_file = ""         #saved timer file to load must include .txt
total_timers = 0        #total amount of unique timers
total_reps = 0          #total amount to repeat unique timers
new_timer = ""          #y or n if user wants to save a new timer
new_file = ""           #new filename of timer to save .txt automatically added
total_time = 0          #the total time the timer will run

print("""This program is a repeating timer. you can specify how many timers
        to make and then how many times you want to repeat the timers.""")

# asks user to enter a saved file if they have one and create file if not
while True:
    saved_timer = input("Load saved timer(y/n/):")

    #ask user for saved file and validates if its path exists
    if saved_timer == "y":

        while True:
            timer_file = input("Enter saved file(Dont forget .txt extention):")

            if exists(timer_file):
                break
            print("Please enter a valid path:")
            
        #loads saved timer into timers_dict
        with open(timer_file) as f:
            data = f.read()
        timers_dict = json.loads(data)

        break

    #create new timers if one is not loaded
    elif saved_timer == "n":
        total_timers = int(input("How many timers would you like to make:"))
        total_reps = int(input("How many times would you like them to repeat:"))
        timers_dict.update({"reps": int(total_reps)})

        for x in range(total_timers):
            timer_name = input(f"Enter a name for timer {x+1}:")
            h, m, s = input("Enter time(hr/min/sec):").split("/")
            total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
            timers_dict.update({timer_name: total_seconds})

        #asks user if they would like to save new timer
        while True:
            new_timer = input("Would you like to save timer(y/n):")

            #saves new timer to .txt file
            if new_timer == "y":
                new_file = input("Name of file to save(Will automaically add .txt to file name):")
                with open(new_file + ".txt", 'w') as convert_file:
                    convert_file.write(json.dumps(timers_dict))
                break
            elif new_timer == "n":
                break
            print("Please enter y or n")
        break


    print("Please enter y or n")
    
#grabs the reps from dictionary       
total_reps = timers_dict.pop("reps")   
print()

#calculates the total time of the timers
for x in timers_dict.values():
    total_time += x
total_time = total_time * total_reps

#prints out the current timer info
print(f"Total Duration: {datetime.timedelta(seconds = total_time)}")
print()
print(f"This timer will repeat {total_reps} times.")
print("Timers that will be repeated:")

for x, y in timers_dict.items():
    print(x, datetime.timedelta(seconds = y))
print()

#Iterates through the timers_dict running the timers
program_start = input("Press enter to start timer")

for x in range(total_reps):
    print(f"Reps to go: {total_reps-x}")
    for name, timer in timers_dict.items():
        countdown(name, timer)
program_end = input("Press enter to exit")

