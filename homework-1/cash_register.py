# """
#
# TASK 1
# #
# # Write a class to represent a Cash Register.
# # Your class should keep the state of price total and purchased items
# #
# # Below is a starter code:
# # ------------------------
# # 1. you can add new variables and function if you want to
# # 2. you will NEED to add accepted method parameters where required.
# # For example, method add_item probably accepts some kind of an item?..
# # 3. You will need to write some examples of how your code works.
# #
# # """

class CashRegister:

    def __init__(self):

        self.total_items = dict()
        self.total_price = 0
        self.discount = 0

    def add_item(self, new_item, new_price):
        self.total_items.update({new_item: new_price})
        print(f"The {new_item} has been added to your cash register. ")

    def remove_item(self, old_item):
        self.total_items.pop(old_item)
        print(f"The {old_item} has been removed from your cash register. ")

    def apply_discount(self, discount_percentage, min_spend):
        if self.total_price >= min_spend:
            self.discount = self.total_price * discount_percentage / 100
            self.total_price = self.total_price - self.discount
        else:
            self.discount = 0
        print(f"Price after discount: {self.total_price}.")

    def get_total(self):
        total = 0
        for price in self.total_items.values():
            total = total + price
        self.total_price = total
        return total

    def show_items(self):
        print(f"The items in the cash register are:")
        for item in self.total_items:
            print(item)

    def reset_register(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        print(f"Your cash register has been reset")

# EXAMPLE code run:

my_cash_register = CashRegister()
my_cash_register.add_item("Necklace", 200)
my_cash_register.add_item("Bracelet", 350)
my_cash_register.add_item("Earrings", 300)
print(my_cash_register.get_total())
my_cash_register.remove_item("Bracelet")
my_cash_register.show_items()
print(my_cash_register.get_total())
my_cash_register.apply_discount(20, 400)
my_cash_register.reset_register()
