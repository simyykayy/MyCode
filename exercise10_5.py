from retailitem import *

def main():
   item1 = RetailItem('Jacket', 12, 59.95);
   item2 = RetailItem('Designer Jeans', 40, 34.95)
   item3 = RetailItem('Shirt', 20, 24.95)
   itemList = [item1, item2, item3]
   for i in range(0, len(itemList)):
      print("Retail Item " + repr(i + 1))
      itemList[i].printDetail()
      if (i != len(itemList) - 1):
         print()

if __name__ == "__main__":
   main()
