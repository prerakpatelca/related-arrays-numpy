# Related Arrays using numpy
This program uses Python lists and sets along with related arrays in numpy.

# Input
Get a list of 5 player names from the user. It will not let the user enter duplicate or empty names. Used string methods to strip leading and trailing whitespace and to make sure each name is capitalized. At the end of the process, the names are stored in a new random order in a numpy array.

# Related Arrays
Now see how quickly the users can hammer on the Enter key. The input function to get 10 inputs from each user. Used the Python time function in the time module to compute the interval between each input (there will be 9 intervals in total). Intervals are rounded to 3 decimal places.
Below is an example of a piece of code that computes the time (without rounding) for a single interval.
`import time`
`input()`
`time1 = time.time()`
`input()`
`time2 = time.time()`
`print(time2-time1,"seconds")`

Used numpy (no loops) compute and output the mean time for each player, then reported the fastest and slowest mean times (rounded to 3 decimal places) as well as the fastest and slowest single interval times (rounded to 3 decimal places). Includes the name of the players who achieved these times.
Finally, there is an output of both the names and the times array for debugging.
