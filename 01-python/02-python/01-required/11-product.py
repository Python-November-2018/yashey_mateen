class Product:
    def __init__(self, price, item_Name, weight, brand, status):
        self.price = price
        self.item_Name = item_Name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        print(self.price += (self.price*tax))
        return self.price
    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like_new":
            self.status = "for sale"
        if reason_for_return == "opened":
            self.status = "used"
            self.price -= (self.price*.20)
        return self
    def display_info(self):
        print(f"Item: {self.item_Name} \n Price: {self.price} \n Weight: {self.weight} \n Brand: {self.brand} \n Status: {self.status}")
        return self

