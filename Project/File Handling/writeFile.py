import os

baconFile = open("bacon.txt", "w")
baconFile.write("I love Bacon!")

baconFile.close()

baconFile = open("bacon.txt", "a")
baconFile.write("\nBacon is not a vegetable!")
baconFile.close()

baconFile = open("bacon.txt", "r")

print(baconFile.read())

baconFile.close()
