

class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


class House:
    def __init__(self, wall_area):
        self.area = wall_area

    def paint_needed(self):
        return self.area * 2.5


class DiscountedPaint(Paint):
   def discounted_price(self,discount_percentage):
       price_after_discount = self.total_price() - (self.total_price() * (0.01*discount_percentage))
       return price_after_discount



first_house = House(50)
area = first_house.paint_needed()
print(area)
new_price = DiscountedPaint(5, "yellow")
print(new_price)
price_after_discount = new_price.discounted_price(20)  # 20% de desconto = 0.20
print(price_after_discount)


