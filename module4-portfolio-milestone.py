#Build the ItemToPurchase class.

class ItemToPurchase():
    #Attributes
    #item_name (string)
    #item_price (float)
    #item_quantity (int)
    #Default constructor
    #Initializes item's name = "none", item's price = 0, item's quantity = 0
    #Method
    #print_item_cost()
    def __init__(self, item_num, item_name = 'none', item_price = 0.0, item_quantity = 0):
        self.item_num = item_num
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def request_input(self):
        print(r'//========\\')
        print( '|| Item', self.item_num, '||')
        print(r'\\========//')
        self.item_name = input('Enter the item name:\n')
        self.item_price = input('Enter the item price:\n')
        self.item_quantity = input('Enter the item quantity:\n')

    def print_item_cost(self):
        print(self.item_name, ' ', self.item_quantity, ' @ $', self.item_price, ' = $', self.item_cost, sep='')

#Prompt the user for two items and create two objects of the ItemToPurchase class.

item1 = ItemToPurchase(item_num = 1)
item2 = ItemToPurchase(item_num = 2)

#Add the costs of the two items together and output the total cost.

print()
print('TOTAL COST')

item1.print_item_cost()
item2.print_item_cost()

print('Total: $', (item1.item_cost + item2.item_cost), sep='')