from parent_class import Product


class bakery(Product):
    def __init__(self, name, price, length_p, width_p, height_p, expiration_date):
        Product.__init__(self, name, price, length_p, width_p, height_p)
        self.__expiration_date = expiration_date

    @property
    def get_expiration_date(self):
        return self.__expiration_date


    @get_expiration_date.setter
    def set_expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    def info(self):
        Product.info(self)
        print(f"The expiration date is {self.__expiration_date}")


bagel = bakery(name="bagel", price=2, expiration_date="14.03.2024", length_p=2, width_p=2, height_p=2)
bagel.info()

