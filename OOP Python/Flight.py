class Flight:
    
    def __init__(self, capacity):
        self.capacity = capacity 
        self.passengers = []

    def addPassenger(self, names):
        if not self.openSeats():
            return False
        self.passengers.append(names)
        return True

    def openSeats(self):
        return self.capacity - len(self.passengers)

flight = Flight(capacity=4)

people = ["Mike", "Dwight", "Jim", "Pam"]
for person in people: 
    if flight.addPassenger(person):
        print(f"{person} added successfully to the flight!")
    else:
        print(f"Sorry, {person} could not be added!")
    