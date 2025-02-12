
class GroceryStore:
    def __init__(self, store_name, apples_sold, apple_price, oranges_sold, orange_price):
        self.store_name = store_name
        self.apples_sold = apples_sold
        self.apple_price = apple_price
        self.oranges_sold = oranges_sold
        self.orange_price = orange_price

    def calculate_annual_revenue(self):
        apple_revenue = self.apples_sold * self.apple_price
        orange_revenue = self.oranges_sold * self.orange_price
        total_revenue = apple_revenue + orange_revenue
        return total_revenue

bambaruush = GroceryStore("Bambaruush", 534, 5000, 487, 10000)
jimshen = GroceryStore("Jimshen", 764, 4800, 423, 9300)
fruits = GroceryStore("Fruits", 136, 5000, 228, 10000)

bambaruush_revenue = bambaruush.calculate_annual_revenue()
jimshen_revenue = jimshen.calculate_annual_revenue()
fruits_revenue = fruits.calculate_annual_revenue()

total_revenue = bambaruush_revenue + jimshen_revenue + fruits_revenue

print(f"Бамбарууш дэлгүүрийн орлого: {bambaruush_revenue}")
print(f"Жимсхэн дэлгүүрийн орлого: {jimshen_revenue}")
print(f"Fruits дэлгүүрийн орлого: {fruits_revenue}")
print(f"Бүх дэлгүүрийн нийт жилийн орлого: {total_revenue}")
