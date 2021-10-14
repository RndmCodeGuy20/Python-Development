from tabulate import tabulate


class Item:
    def __init__(self, name: str, price: float, quantity):

        # -Validation of received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        #! if price <= 0 AssertionError is triggered
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calcTotPrice(self):
        return self.price * self.quantity


def dispInfo(table):
    print(
        "\n"
        + tabulate(
            table, headers="firstrow", tablefmt="fancy_grid", showindex=range(1, 6)
        )
        + "\n"
    )


itPhone = Item("Phone", 15000, 9)
itLaptop = Item("Laptop", 65000, 5)
itSpeakers = Item("Speakers", 20000, 7)
itWashMach = Item("Washing Machine", 15000, 3)
itRefridge = Item("Refrigerator", 40000, 4)

table = [
    ["Item", "Price", "Quantity", "Total Price"],
    [
        itPhone.name,
        itPhone.price,
        itPhone.quantity,
        itPhone.calcTotPrice(),
    ],
    [
        itLaptop.name,
        itLaptop.price,
        itLaptop.quantity,
        itLaptop.calcTotPrice(),
    ],
    [
        itSpeakers.name,
        itSpeakers.price,
        itSpeakers.quantity,
        itSpeakers.calcTotPrice(),
    ],
    [
        itWashMach.name,
        itWashMach.price,
        itWashMach.quantity,
        itWashMach.calcTotPrice(),
    ],
    [
        itRefridge.name,
        itRefridge.price,
        itRefridge.quantity,
        itRefridge.calcTotPrice(),
    ],
]

dispInfo(table)
