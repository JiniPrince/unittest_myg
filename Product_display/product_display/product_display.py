#product_display.py
class ProductDisplay:
    def display_products(self):
        products = [
            {

                'name': 'realme',
                'description': 'latest android version',
                'price': 9099,
                'image': 'realme.jpg',

                'reviews': [
                    {'username': 'user1', 'rating': 4, 'comment': 'Great product'},
                    {'username': 'user2', 'rating': 3, 'comment': 'Okay product'}
                     ],
                'features': [
                    {'name': 'Feature 1', 'value': 'Value 1'},
                    {'name': 'Feature 2', 'value': 'Value 2'}
                ]
            },
            {
                'name': 'lg refrigerator',
                'description': '500l  capacity',
                'price': 90999,
                'image': 'lg.jpg',
                'reviews': [
                    {'username': 'user3', 'rating': 5, 'comment': 'Amazing product'},
                    {'username': 'user4', 'rating': 2, 'comment': 'Disappointing product'}
                ],
                'features': [
                    {'name': 'Feature 1', 'value': 'Value 1'},
                    {'name': 'Feature 3', 'value': 'Value 3'}
                ]
            }
        ]
        return products
