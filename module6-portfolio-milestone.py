# CSC500 - Portfolio Milestone - Matthew Bayne
#=============================================

#Build the ItemToPurchase class
class ItemToPurchase():
    def __init__(self, item_num, item_name = 'none', item_price = 0.0, item_quantity = 0, item_description = 'none'):
        self.item_num = item_num
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_cost = 0.0
        self.item_description = item_description

    def request_input(self):
        print('Item', self.item_num)
        item_name_in = input('Enter the item name:\n')
        if item_name_in != '':
            self.item_name = item_name_in
        item_price_in = input('Enter the item price:\n')
        if item_price_in != '':
            self.item_price = float(item_price_in)
        item_quantity_in = input('Enter the item quantity:\n')
        if item_quantity_in != '':
            self.item_quantity = int(item_quantity_in)
        item_description_in = input('Enter the item description:\n')
        if item_description_in != '':
            self.item_description = item_description_in

    def print_item_cost(self):
        self.item_cost = self.item_price * self.item_quantity
        print('{name} {quantity:.0f} @ ${price:.2f} = ${cost:.2f}'.format(
            name = self.item_name,
            quantity = self.item_quantity,
            price = self.item_price,
            cost = self.item_cost
        ))

#Build the ShoppingCart class
class ShoppingCart():
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_to_remove):
        for item in self.cart_items:
            if item_to_remove == item.item_name:
                del self.cart_items[item.item_num]
                return
        print('Item not found in cart.\nNothing removed.')

    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if ItemToPurchase in item.item_name:
                print(ItemToPurchase, 'is in', item.item_num)
                item.request_input()
                return
        print('Item not found in cart.\nNothing modified.')

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_cost
        return '{:.2f}'.format(total_cost)

    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('Number of Items: {}'.format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.print_item_cost()
            print('Total: ${}'.format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                print('{}: {}'.format(item.item_name, item.item_description))

def print_menu(shopping_cart):
    user_in = ''
    while user_in.lower() != 'q':
        print('\nMENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('m - Modify item info')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        user_in = input('Choose an option: ')
        if user_in.lower() == 'a':
            print('You chose \'a\'.')
        elif user_in.lower() == 'r':
            print('You chose \'r\'.')
            shopping_cart.remove_item(input('Enter item to remove: '))
        elif user_in.lower() == 'c':
            print('You chose \'c\'.')
        elif user_in.lower() == 'm':
            print('You chose \'m\'.')
            shopping_cart.modify_item(input('Enter item to modify: '))
        elif user_in.lower() == 'i':
            print('You chose \'i\'.')
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            shopping_cart.print_descriptions()
        elif user_in.lower() == 'o':
            print('You chose \'o\'.')
            print('\nOUTPUT SHOPPING CART')
            shopping_cart.print_total()
        elif user_in.lower() != 'q':
            print('You need to chose an option!')
    print('You chose \'q\', Quitting now.')

def main():
    print_menu(my_shopping_cart)

my_shopping_cart = ShoppingCart('Matthew', 'October 22, 2023')
my_shopping_cart.add_item(ItemToPurchase(
    item_num = 0,
    item_name = 'Pickle',
    item_price = 0.32,
    item_quantity = 3,
    item_description = 'It\'s a pickle.'
))
my_shopping_cart.add_item(ItemToPurchase(
    item_num = 1,
    item_name = 'Mango',
    item_price = 2.07,
    item_quantity = 7,
    item_description = 'A nice sweet mango.'
))
my_shopping_cart.add_item(ItemToPurchase(
    item_num = 2,
    item_name = 'Water',
    item_price = 1.58,
    item_quantity = 2,
    item_description = 'Refreshing water.'
))
my_shopping_cart.add_item(ItemToPurchase(
    item_num = 3,
    item_name = 'T-Shirt',
    item_price = 21.63,
    item_quantity = 1,
    item_description = 'A cool t-shirt with a dog wearing sunglasses on it.'
))

main()