# CSC500 - Portfolio Milestone - Matthew Bayne
#=============================================

#Build the ItemToPurchase class
class ItemToPurchase():
    def __init__(self, item_num = 0, item_cost = 0, item_name = 'none', item_price = 0.0, item_quantity = 0):
        self.item_num = item_num
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_cost = item_cost

    def request_input(self):
        print( 'Item', self.item_num)
        self.item_name = input('Enter the item name:\n')
        self.item_price = float(input('Enter the item price:\n'))
        self.item_quantity = int(input('Enter the item quantity:\n'))
        self.item_cost = self.item_price * self.item_quantity

    def print_item_cost(self):
        print('{name} {quantity:.0f} @ ${price:.2f} = ${cost:.2f}'.format(name = self.item_name, quantity = self.item_quantity, price = self.item_price, cost = self.item_cost))
'''
#Prompt the user for two items and create two objects of the ItemToPurchase class.
item1 = ItemToPurchase(item_num = 1)
item2 = ItemToPurchase(item_num = 2)
print()
item1.request_input()
item2.request_input()

#Add the costs of the two items together and output the total cost.
print('TOTAL COST')
item1.print_item_cost()
item2.print_item_cost()
print('Total: ${0:.2f}'.format(item1.item_cost + item2.item_cost))
'''

# Module 6
#=============================================

#Build the ShoppingCart class
class ShoppingCart():
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items += ItemToPurchase

    def remove_item(self, ItemToRemove):
        if ItemToRemove in self.cart_items:
            self.cart_items.remove(ItemToRemove)
        else:
            print('Item not found in cart.\nNothing removed.')

    def modify_item(self, ItemToPurchase):
        if ItemToPurchase in self.cart_items:
            pass
            #if ItemToPurchase.item_description ==
            #check if parameter has default values for description, price, and quantity. If not, modify item in cart.
                #cart_items.remove(ItemToRemove)
        else:
            print('Item not found in cart.\nNothing modified.')

    def get_num_items_in_cart(self):
        return(len(self.cart_items))

    def get_cost_of_cart(self):
        for item in self.cart_items:
            pass
            #Determine Total Cost of Items in cart

    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('Number if Items: {}'.format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                print('{} {} @ ${} = ${}'.format())
                total += 1
            print('Total: ${}'.format(self.get_cost_of_cart()))

    def print_descriptions(self):
        pass

def print_menu(shopping_cart):
    user_in = ''
    while user_in.lower() != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        user_in = input('Choose an option: ')

def main():
    print_menu(shopping_cart)

shopping_cart = ShoppingCart()
shopping_cart.add_item('Pickle')
shopping_cart.add_item('Carrot')
shopping_cart.add_item('Tomato')

main()