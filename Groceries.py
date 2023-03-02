class Groceries:
    groceries_list = ["Peaches", "Apples", "Oranges", "Pineapple", "Apple Pie"]
    sales_tax = (5.3 / 100)

    def print_groceries(self):
        for item in self.groceries_list:
            print(item)

    def num_of_groceries(self):
        return len(self.groceries_list)

    def calculate_sales_tax(self, price):
        return price * self.sales_tax

    def get_total(self):
        try:
            price = 0.0
            for item in self.groceries_list:
                print(f"Price of {item} is: {self.price_of_food(item)}")
                price += self.price_of_food(item)
            print(f"Sales tax of groceries is: {self.calculate_sales_tax(price)}")
            print(f"Total price of groceries is: {price + self.calculate_sales_tax(price)}")
        except Exception as e:
            print("Error with code:", e)

    def price_of_food(self, item):
        try:
            if item == "Peaches":
                return 3.00
            elif item == "Apples":
                return 3.00
            elif item == "Oranges":
                return 3.00
            elif item == "Pineapple":
                return 5.00
            elif item == "Apple Pie":
                return 6.00
            else:
                return 0.00
        except Exception as e:
            print("Error with code:",e)
