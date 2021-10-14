from tabulate import tabulate


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calcTotPrice(self, Pr, Qu):
        return Pr * Qu


def dispInfo(table):
    print("\n")
    print(
        tabulate(
            table, headers="firstrow", tablefmt="fancy_grid", showindex=range(1, 6)
        )
    )
    print("\n")


itPhone = Item("Phone", 15000, 9)
itLaptop = Item("Laptop", 65000, 5)
itSpeakers = Item("Speakers", 20000, 7)
itWashMach = Item("Washing Machine", 15000, 3)
itRefridge = Item("Refridgerator", 40000, 4)

table = [
    ["Item", "Price", "Quantity", "Total Price"],
    [
        itPhone.name,
        itPhone.price,
        itPhone.quantity,
        itPhone.calcTotPrice(itPhone.price, itPhone.quantity),
    ],
    [
        itLaptop.name,
        itLaptop.price,
        itLaptop.quantity,
        itLaptop.calcTotPrice(itLaptop.price, itLaptop.quantity),
    ],
    [
        itSpeakers.name,
        itSpeakers.price,
        itSpeakers.quantity,
        itSpeakers.calcTotPrice(itSpeakers.price, itSpeakers.quantity),
    ],
    [
        itWashMach.name,
        itWashMach.price,
        itWashMach.quantity,
        itWashMach.calcTotPrice(itWashMach.price, itWashMach.quantity),
    ],
    [
        itRefridge.name,
        itRefridge.price,
        itRefridge.quantity,
        itRefridge.calcTotPrice(itRefridge.price, itRefridge.quantity),
    ],
]

dispInfo(table)
