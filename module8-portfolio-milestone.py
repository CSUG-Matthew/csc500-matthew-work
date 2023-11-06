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
        while True: # Require a name for an item to be created.
            input_name = input('Enter the item name:\n')
            if input_name == '':
                print('An item name is required to add an item to cart!')
            else:
                item_instance.item_name = input_name
                break
        try:
            item_instance.item_description = input('Enter the item description:\n')
        except ValueError:
            print('Wrong value entered. Default decription of \'none\' set. Use the modify option to fix.')
        try:
            item_instance.item_price = float(input('Enter the item price:\n'))
        except ValueError:
            print('Wrong value entered. Default price of \'0.0\' set. Use the modify option to fix.')
        try:
            item_instance.item_quantity = int(input('Enter the item quantity:\n'))
        except ValueError:
            print('Wrong value entered. Default quantity of \'0\' set. Use the modify option to fix.')
        self.cart_items.append(item_instance)

    # For Testing/Quickly adding items
    def quick_add(self, item_instance):
        self.item_num += 1
        item_instance.item_num = self.item_num
        self.cart_items.append(item_instance)

    # Step 9: Implement remove
    def remove_item(self):
        print('\nREMOVE ITEM FROM CART')
        self.get_current_cart_list()
        item_to_remove = input('Enter name of item to remove: ')
        for item in self.cart_items:
            if item_to_remove.lower() == item.item_name.lower():
                self.cart_items.remove(item)
                print('\'{}\' item removed from cart!'.format(item.item_name))
                return
        print('Item not found in cart.\nNothing removed.')

    # Step 10: Implement Change item quantity (Done by modifying modify_item method)
    def modify_item(self, choice):
        self.get_current_cart_list()
        item_instance_name = input('Enter the item name:\n')
        for item in self.cart_items:
            if item_instance_name.lower() in item.item_name.lower() and item_instance_name != '':
                if choice == 'c': # Edit quantity
                    try:
                        item.item_quantity = int(input('Enter the new quantity:\n'))
                        print('Item quantity of \'{}\' updated!'.format(item.item_quantity))
                    except ValueError:
                        print('Wrong value entered. Original value of \'{}\' unchanged. Use the modify option to change.'.format(item.item_quantity))
                    return
                elif choice == 'm': # Add missing info
                    info_missing_flag = False
                    # No need to check for missing name here, shouldn't happen.
                    if item.item_description == 'none':
                        item.item_description = input('Enter the missing item description:\n')
                        print('Item description of \'{}\' updated!'.format(item.item_description))
                        info_missing_flag = True
                    if item.item_price == 0.0:
                        try:
                            item.item_price = float(input('Enter the missing item price:\n'))
                            print('Item price of \'{}\' updated!'.format(item.item_price))
                        except ValueError:
                            print('Wrong value entered. Default price of \'0.0\' set. Use the modify option to fix.')
                        info_missing_flag = True
                    if item.item_quantity == 0:
                        try:
                            item.item_quantity = int(input('Enter the missing item quantity:\n'))
                            print('Item quantity of \'{}\' updated!'.format(item.item_quantity))
                        except ValueError:
                            print('Wrong value entered. Default quantity of \'0\' set. Use the modify option to fix.')
                        info_missing_flag = True
                    if info_missing_flag == False:
                        print('No item information was missing!')
                    return
        print('Item not found in cart.\nNothing modified.')

    # Add giving a list of items, for use when name input required (modify_items).
    def get_current_cart_list(self):
        print('Current items in cart:')
        for item in self.cart_items:
            print(' *', item.item_name)
        return

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
        print('m - Modify missing item info')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit\n')
        user_in = input('Choose an option: ')
        if user_in.lower() == 'a':
            print('You chose \'a\'.')
            shopping_cart.add_item()
        elif user_in.lower() == 'r':
            print('You chose \'r\'.')
            shopping_cart.remove_item()
        elif user_in.lower() == 'c':
            print('You chose \'c\'.\n')
            print('CHANGE ITEM QUANTITY')
            shopping_cart.modify_item('c')
        elif user_in.lower() == 'm':
            print('You chose \'m\'.\n')
            print('MODIFY MISSING ITEM INFO')
            shopping_cart.modify_item('m')
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
    print_menu(my_shopping_cart)

    '''
    # Testing Setup
    my_shopping_cart = ShoppingCart('Matthew', 'November 05, 2023')
    my_shopping_cart.quick_add(ItemToPurchase(
        item_num = 0,
        item_name = 'Pickle',
        item_price = 0.32,
        item_quantity = 3,
        item_description = 'It\'s a pickle.'
    ))
    my_shopping_cart.quick_add(ItemToPurchase(
        item_num = 1,
        item_name = 'Mango',
        item_price = 2.07,
        item_quantity = 7,
        item_description = 'A nice sweet mango.'
    ))
    my_shopping_cart.quick_add(ItemToPurchase(
        item_num = 2,
        item_name = 'Water',
        #item_price = 1.58, # Testing for missing value
        item_quantity = 2,
        item_description = 'Refreshing water.'
    ))
    my_shopping_cart.quick_add(ItemToPurchase(
        item_num = 3,
        item_name = 'T-Shirt',
        item_price = 21.63,
        #item_quantity = 1, # Testing for missing value
        item_description = 'A cool t-shirt with a dog wearing sunglasses on it.'
    ))
    print_menu(my_shopping_cart)
    '''
