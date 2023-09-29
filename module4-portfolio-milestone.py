#WIP
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
    def __init__(self, item_num, item_cost = 0, item_name = 'none', item_price = 0.0, item_quantity = 0):
        self.item_num = item_num
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_cost = item_cost

    def request_input(self):
        print(r'//========\\')
        print( '|| Item', self.item_num, '||')
        print(r'\\========//')
        self.item_name = input('Enter the item name:\n')
        self.item_price = float(input('Enter the item price:\n'))
        self.item_quantity = int(input('Enter the item quantity:\n'))
        self.item_cost = self.item_price * self.item_quantity

    def print_item_cost(self):
        print('{name} {quantity:.0f} @ ${price:.2f} = ${cost:.2f}'.format(name = self.item_name, quantity = self.item_quantity, price = self.item_price, cost = self.item_cost))

#Prompt the user for two items and create two objects of the ItemToPurchase class.

item1 = ItemToPurchase(item_num = 1)
item2 = ItemToPurchase(item_num = 2)

#Add the costs of the two items together and output the total cost.

print()
print(' TOTAL COST')
item1.request_input()
item1.print_item_cost()
item2.request_input()
item2.print_item_cost()

print('Total: ${0:.2f}'.format(item1.item_cost + item2.item_cost))