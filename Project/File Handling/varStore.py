import shelve

shelfFile = shelve.open("mydata\\mydata")

cats = ["Zophie", "Pooka", "Michael"]

shelfFile["cats"] = cats
shelfFile.close()

shelfFile = shelve.open("mydata\\mydata")
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

shelfFile.close()
