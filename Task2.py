"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
call_time = {}
answer_time = {}

def call(arg):
    for num_call, num_answer, date, duration in calls:
        if num_call not in arg.keys():
            arg[num_call] = []
        arg[num_call].append(int(duration))

def answer(arg):
    for num_call, num_answer, date, duration in calls:
        if num_answer not in arg.keys():
            arg[num_answer] = []
        arg[num_answer].append(int(duration))

answer(answer_time)
call(call_time)

for key, value in answer_time.items():
    if key in call_time.keys():
        call_time[key] += value
    else:
        call_time[key] = value

for key, value in call_time.items():
    call_time[key] = sum(value)

longest = max(call_time, key = call_time.get)

print(longest, "spent the longest time", call_time[longest], "seconds, on the phone suting September 2016.")