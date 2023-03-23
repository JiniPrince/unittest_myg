# dropdown.py

class DropdownList:
    def __init__(self):
        self.dropdown_items = {
            'E-MI Claims': ['Item 1', 'Item 2', 'Item 3'],
            'New Arrivals': ['Item 4', 'Item 5', 'Item 6'],
            'Home Appliances': ['Item 7', 'Item 8', 'Item 9'],
            'Mobiles': ['Item 10', 'Item 11', 'Item 12'],
            'Laptops' : ['Item 13', 'Item 14', 'Item 15']
        }

    def get_dropdown_items(self, dropdown_name):
        if dropdown_name in self.dropdown_items:
            return self.dropdown_items[dropdown_name]
        else:
            return None

    def add_dropdown_item(self, item, dropdown_name):
        if dropdown_name in self.dropdown_items:
            self.dropdown_items[dropdown_name].append(item)
        else:
            self.dropdown_items[dropdown_name] = [item]

    def remove_dropdown_item(self, item, dropdown_name):
        if dropdown_name in self.dropdown_items and item in self.dropdown_items[dropdown_name]:
            self.dropdown_items[dropdown_name].remove(item)
        else:
            raise ValueError('Item or dropdown not found')
