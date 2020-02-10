Time Complexity Analysis

For all the following tasks, the Python library 'csv' was imported in the
first place. Two sheets were read and get accessed. Those steps produced constant 
run time complexity.

Task 0
O(2)/O(c)

This problem accessed the 2 lists and 'print' twice, not
involving any iteration or recursion. So, each time its 
'print' cause 'O(1)'. The exact final answer would be O(2).


Task 1
O(n)

###	new_texts = [t[0] for t in texts] + [t[1] for t in texts]
Two 'for' loop here to access two rows causing O(2n)

###	new_calls = [t[0] for t in calls] + [t[1] for t in calls]
Another two 'for' loop here causing O(2n).

###	numbers = new_texts + new_calls
###	set1 = set(numbers)
###	n = len(set1)
###	print("There are", n, "different telephone numbers in the records.")
For the 'set' function, it needs to go through every single data in the list.
With some comparison in the iteration, it can finally output the sorted data.
So, the 'set' function can produce a run time O(n). Other three steps produces 
constant run time O(3). 

Add individual parts together, the complexity would be O(3n+3), 
While when the n is large enough, the constant and coefficient
could be insignificant. So, the final complexity would be O(n).

Task 2
O(n^2)

There are two functions with nested loop in this task, which produce complexity 
O(2n^2).Two iterations, 'for' loop in this task, producing complexity O(2n).
Forget about constants and coefficients, the final time complexity would be O(n^2).

Task 3 
O(nlog(n))

There are four parallel 'for' loops in this task. Each of them has complexity of O(n).
The sorting function in this problem also has a run time O(nlog(n)).
So, the worst case's complexity becomes O(nlog(n)).


Task 4
O(n^2)

For task 4, within the big 'for' loop, there're 3 'for' loops inside the 'if'
condition. So, the worst case complexity calculation for the big 'for' loop 
would be n*(3n+1), which is (3n^2+n).s
Other than the loop, the sorting function produces run time 'n'.
Forget about other constants and coefficients, the answer would be  O(n^2).
