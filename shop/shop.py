class Product(object):
    def get_price_choices(self):
        prices = [
            ('0-500', '0-500'),
            ('500-1000','500-1000'),
            ('>1000', '>1000'),
        ]
        return prices