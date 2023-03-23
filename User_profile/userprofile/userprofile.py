class UserProfile:
    def __init__(self):
        self.name = ''
        self.shipping_address = {}

    def view_profile(self):
        return {'name': self.name, 'shipping_address': self.shipping_address}

    def update_name(self, first_name, last_name):
        self.name = f'{first_name} {last_name}'

    def update_shipping_address(self, shipping_address):
        self.shipping_address = shipping_address
