class RetailItem:
   def __init__(self, desc, inv, price):
      self.desc = desc
      self.inv = inv
      self.price = price;
      
   def printDetail(self):
      print("Description: " + self.desc)
      print("Units in inventory: " + repr(self.inv))
      print("Price: $" + repr(self.price))

   def set_inv(self, UI):
      self.inv = UI

   def set_price(self, price):
      self.price = price

   def get_desc(self):
      return self.desc

   def get_inv(self):
      return self.inv

   def get_price(self):
      return self.price



