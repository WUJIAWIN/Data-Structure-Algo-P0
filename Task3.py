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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
   

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# part A

# get receiving number that called from (080) area
    # get codes from three parts:
    # fixed line enclosed in "()"
    # "first 4 digits" (7/8/9) for mobiles that have a space in between
    # telemarkets number "140"

called_from_B = []
codes = []
sorted_codes = []
for num in calls:
    if "(080)" in num[0]:
        called_from_B.append(num[1])
for num in called_from_B:
    if num[0] == "(" :
        j = num.index(")")
        codes.append(num[0:(j+1)])
    elif " " in num:
        codes.append(num[0:4])
    elif num[0:3] == "140":
        codes.append("140")

sorted_codes = list(set(codes))
sorted_codes.sort()
print("The numbers called by people in Bangalore have codes:")
for code in sorted_codes:
    print(code)
# Part B

# of all the calls made
# from a number starting with "(080)", what percentage of these calls
# were made to a number also starting with "(080)"?
call_to_B = 0
for num in calls:
    if "(080)" in num[0] and "(080)" in num[1]:
        call_to_B +=1
percentage = round(call_to_B/(len(called_from_B))*100,2)
print(percentage, "percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.")
