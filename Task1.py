"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
new_texts = [t[0] for t in texts] + [t[1] for t in texts]
new_calls = [t[0] for t in calls] + [t[1] for t in calls]
numbers = new_texts + new_calls
set1 = set(numbers)
n = len(set1)
print("There are", n, "different telephone numbers in the records.")
