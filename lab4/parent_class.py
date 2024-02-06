class Product:
    def __init__(self, name, price, length_p, width_p, height_p):
        self.__name = name
        self.__price = int(price)
        self.length_p = length_p
        self.width_p = width_p
        self.height_p = height_p

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def set_name(self, price):
        self.__price = price

    def info(self):
        print(f"The product name is {self.__name}, it`s cost {self.__price}")

    def sale(self, sale):
        last_price = round(self.__price * ((100 - sale) / 100), 2)
        if last_price > 0.01:
            print(f"The price, after sale is {last_price}")
        else:
            print(f'err')

    def count(self, length_box, width_box, height_box):
        count = 0
        # size = [self.length_p, self.width_p, self.height_p]
        var = ([self.length_p, self.width_p, self.height_p], [self.length_p, self.height_p, self.width_p],
               [self.width_p, self.length_p, self.height_p], [self.width_p, self.height_p, self.length_p],
               [self.height_p, self.length_p, self.width_p], [self.height_p, self.width_p, self.length_p])

        for i, j, k in var:
            c = (length_box // i) * (width_box // j) * (height_box // k)
            if c > count:
                count = c
        print(f'{count} of products can fit in this box')

    def __add__(self, other):
        return self.__price + other.__price

# Product_1 = Product(input(), input())
# Product_2 = Product(input(), input())
# Product_3 = Product(input(), input())
#
#
# Product_1.info()
# Product_2.info()
# Product_3.info()


Product1 = Product(name='guitar', price=5000, length_p=10, width_p=20, height_p=30)
Product2 = Product(name='book', price=500, length_p=2, width_p=3, height_p=4)

Product1.info()
Product1.sale(10)
Product2.count(length_box=4, width_box=5, height_box=10)