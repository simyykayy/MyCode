class CashRegister:
   def __init__(self):
      self.retail_items = []

   def purchase_item(self, retail_item):
      self.retail_items.append(retail_item)

   def get_total(self):
      totalPrice = 0.0
      for item in self.retail_items:
         totalPrice += item.get_price()
      return totalPrice

   def show_items(self):
      i = 0;
      for i in range(0, len(self.retail_items)):
         self.retail_items[i].printDetail()
         if (i != len(self.retail_items) - 1):
            print()

   def clear(self):
      self.retail_items = []


