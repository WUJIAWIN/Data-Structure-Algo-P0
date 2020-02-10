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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# made outgoing calls
# never send texts
# never receive texts
# never receive calls

telemarketers = []
for num in calls:
    if num[0] not in [x[1] for x in calls] + [x[0] for x in texts] + [x[1] for x in texts]:
        telemarketers.append(num[0])

sorted_number = list(set(telemarketers))
sorted_number.sort()
print("These numbers could be telemarketers: ")
for number in sorted_number:
    print(number)
