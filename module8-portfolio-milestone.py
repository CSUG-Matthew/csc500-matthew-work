# CSC500 - Portfolio Milestone - Matthew Bayne
#=============================================

#Build the ItemToPurchase class
class ItemToPurchase():
    def __init__(self, item_num = 0, item_name = 'none', item_price = 0.0, item_quantity = 0, item_description = 'none'):
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
        self.item_num = 0

    # Step 8: Implement Add item
    def add_item(self):
        item_instance = ItemToPurchase()
        self.item_num += 1
        print('\nADD ITEM TO CART')
        item_instance.item_num = self.item_num
        item_instance.item_name = input('Enter the item name:\n')
        item_instance.item_description = input('Enter the item description:\n')
        item_instance.item_price = float(input('Enter the item price:\n'))
        item_instance.item_quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(item_instance)

    # Step 9: Implement remove
    def remove_item(self):
        item_to_remove = input('Enter item to remove: ')
        for item in self.cart_items:
            if item_to_remove.lower() == item.item_name.lower():
                ### print('I want to delete {}'.format(item.item_name))
                self.cart_items.remove(item)
                return
        print('Item not found in cart.\nNothing removed.')

    def modify_item(self):
        item_instance = input('Enter item to modify: ')
        for item in self.cart_items:
            if item_instance in item.item_name:
                print(item_instance, 'is in', item.item_num)
                item.request_input()
                return
        print('Item not found in cart.\nNothing modified.')

    # Step 10: Implement Change item quantity
    def change_item_quantity(self):
        print('CHANGE ITEM QUANTITY\n')
        input_name = input('Enter the item name:\n')
        quantity_update = float(input('Enter the new quantity:\n'))
        for item in self.cart_items:
            if input_name.lower() in item.item_name.lower():
                item.item_quantity = quantity_update
                return
        print('Item not found in cart.\nNothing modified.')
        
    '''
    Step 10:
    Implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem() method.

    Example:
    CHANGE ITEM QUANTITY
    Enter the item name:
    Nike Romaleos
    Enter the new quantity:
    3
    '''

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_cost
        return '{:.2f}'.format(total_cost)

    def print_total(self):
        print('\nOUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('Number of Items: {}'.format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.print_item_cost()
            print('Total: ${}'.format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('Item Descriptions')
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
            shopping_cart.add_item()
        elif user_in.lower() == 'r':
            print('You chose \'r\'.')
            shopping_cart.remove_item()
        elif user_in.lower() == 'c':
            print('You chose \'c\'.')
            shopping_cart.change_item_quantity()
        elif user_in.lower() == 'm':
            print('You chose \'m\'.')
            shopping_cart.modify_item()
        elif user_in.lower() == 'i':
            print('You chose \'i\'.')
            shopping_cart.print_descriptions()
        elif user_in.lower() == 'o':
            print('You chose \'o\'.')
            shopping_cart.print_total()
        elif user_in.lower() != 'q':
            print('You need to chose an option!')
    print('You chose \'q\', Quitting now.')

if __name__ == '__main__':
    # Step 7: Prompt user for name and date, output it, create ShoppingCart object.
    my_shopping_cart = ShoppingCart()
    my_shopping_cart.customer_name = input('Enter customer\'s name:\n')
    my_shopping_cart.current_date = input('Enter today\'s date:\n')
    print('Customer name: {}'.format(my_shopping_cart.customer_name))
    print('Today\'s date: {}'.format(my_shopping_cart.current_date))

    #my_shopping_cart = ShoppingCart('Matthew', 'October 22, 2023')
    '''
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
    ))'''

    print_menu(my_shopping_cart)
