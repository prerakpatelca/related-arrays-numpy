"""This assignment uses Python lists and sets along with related arrays in numpy. This program gets the input from the user for 5 player names and then stores it in a Python sets from which it randomly selects the users name asks that player to enter 10 times quickly, where program stores the time difference between the first enter & the second enter and stores it in and Python arrays. At the end program prints out some useful information dervied from the dataset.

Prerak Patel, Student, Mohawk College, 2020"""

import numpy as np,time

print("Enter 5 player names:")
""" names variable has type of Python set that is where all the players names are going to be stored. """
names = set()
""" Looping to get 5 unique player names while checking for the empty space and duplicate entries. """
while len(names) != 5:
    players = input().title().strip()
    if players in names:
        print("Name already entered")
    elif players == "":
        print("Name can't be empty")
    else:
        names.add(players)

""" Converting Python Set into numpy array using array function to use numpy functions. """
names = np.array(list(names))
""" count variable is used to keep track of the index of the player whose input we are taking so that we can use that index to store the input into an array"""
count = 0
""" allTurns variable is used to hold the player's individual  array. """
allTurns = []
""" Looping through each player to take their input of 10 quick enters to get the time difference """
for player in names:
    eachTurn = []
    print(player+"'s turn. Press enter 10 times quickly.")
    input()
    time1 = time.time()
    for n in range(9):
        input()
        time2 = time.time()
        eachTurn.append(time2-time1)
        time1 = time2
    allTurns.insert(count,eachTurn)
    count +=1

allTurns = np.array(allTurns)
""" calculating mean of the allTurns array by player's row. """
meanScore = allTurns.mean(axis=1)

""" getting the index array after sorting the names array alphabatically. """
sortSequence = names.argsort()

print("Names " + str(names[sortSequence]) + "\n" +
      "Mean times: " + str(meanScore[sortSequence]) + "\n" +
      "Fastest Average Time: "+ str(np.around(meanScore.min(),decimals=3)) + " by " + names[int(np.where(meanScore == meanScore.min())[0])] + "\n" +
      "Slowest Average Time: " + str(np.around(meanScore.max(),decimals=3)) + " by " + names[int(np.where(meanScore == meanScore.max())[0])] + "\n" +
      "Fastest Single Time: " + str(allTurns.min()) + " by " + names[int(np.where(allTurns == allTurns.min())[0])] + "\n" +
      "Slowest Single Time: " + str(allTurns.max()) + " by " + names[int(np.where(allTurns == allTurns.max())[0])] + "\n\n" +
      str(names[sortSequence]) + "\n" + str(np.around(allTurns, decimals=3)[sortSequence]))










