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

    def __init__(self, item_name, price, in_stock=True):
        self.total_items = []
        self.total_price = +-1
        self.discount = 0 if price else "20%"
        self.item_name = item_name
        self.price = price
        self.in_stock = in_stock
        self.total_items.append({"item_name": self.item_name, "price": self.price, "in_stock": self.stock})



    def add_items(self, new_item, new_price, in_stock):
        self.total_items.append({"item_name": new_item, "price": new_price, "in_stock": in_stock})




item_1 = CashRegister("Earrings", 165, True)
print(item_1.append)










#     def add_item(self, new_item, new_price):
#         self.total_items.append({"item": new_item, "price": new_price, "stock": stock"})
#     #     print(f"Your item {self.item_name} has been added to your basket.")
#     #
#     # def remove_item(self):
#     #     print(f"Your item {self.item_name} has been removed from your basket")
#     #
#     # def apply_discount(self):
#     #     print(f"A discount of {self.discount} has been applied to your basket.")
#     #
#     # def get_total(self, price):
#     #     self.total_price += price
#     #     return self.total_price
#     #
#     # def show_items(self, total_items):
#     #
#     #
#     # def reset_register(self):
#
#
#
# item_1 = CashRegister("earrings", "£165")
# print(item_1.total_item)
# # my_shop.remove_item()
# # my_shop.get_total(165)
# # for total in sum(range(50):
# # my_shop.apply_discount()
#
#
#


