from tabulate import tabulate


class Item:

    # payRate = 0.8  # -Value after 20% discount!
    all = []

    def __init__(self, name: str, price: float, quantity, discount: float):

        # - Validation of received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        #! if price <= 0 AssertionError is triggered
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"
        assert discount < 1, f"Discount {discount*100} cannot be greater than 100%"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

        Item.all.append(self)

    def calcTotPrice(self):
        return self.price * self.quantity

    def applyDiscount(self):
        self.price = self.price * self.discount
        return self.price

    def showDisc(self):
        discStr = str(round((1 - self.discount) * 100))
        return discStr + "%"

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


def dispInfo(table):
    print(
        "\n"
        + tabulate(
            table, headers="firstrow", tablefmt="fancy_grid", showindex=range(1, 6)
        )
        + "\n"
    )


itPhone = Item("Phone", 15000, 9, 0.76)
itLaptop = Item("Laptop", 65000, 5, 0.73)
itSpeakers = Item("Speakers", 20000, 7, 0.89)
itWashMach = Item("Washing Machine", 15000, 3, 0.85)
itFridge = Item("Refrigerator", 40000, 4, 0.86)

table = [
    [
        "Item",
        "Price",
        "Quantity",
        "Total Price",
        "Applied Discount",
        "Discounted Price",
    ],
    [
        itPhone.name,
        itPhone.price,
        itPhone.quantity,
        itPhone.calcTotPrice(),
        itPhone.showDisc(),
        itPhone.applyDiscount(),
    ],
    [
        itLaptop.name,
        itLaptop.price,
        itLaptop.quantity,
        itLaptop.calcTotPrice(),
        itLaptop.showDisc(),
        itLaptop.applyDiscount(),
    ],
    [
        itSpeakers.name,
        itSpeakers.price,
        itSpeakers.quantity,
        itSpeakers.calcTotPrice(),
        itSpeakers.showDisc(),
        itSpeakers.applyDiscount(),
    ],
    [
        itWashMach.name,
        itWashMach.price,
        itWashMach.quantity,
        itWashMach.calcTotPrice(),
        itWashMach.showDisc(),
        itWashMach.applyDiscount(),
    ],
    [
        itFridge.name,
        itFridge.price,
        itFridge.quantity,
        itFridge.calcTotPrice(),
        itFridge.showDisc(),
        itFridge.applyDiscount(),
    ],
]

dispInfo(table)

# print(Item.all)

# print(itPhone.__dict__) #$ All the attributes for instance level.
# print("\n")
# print(Item.__dict__) #$ ALl the attributes for Class level.
