from product.product import Product


class ShoppingCart:
    def __init__(self):
        self._shoppinglist = []

    def addProduct(self, product: Product):
        self._shoppinglist.append(product)
        return self

    def getProducts(self):
        return self._shoppinglist

    def getTotalAmount(self):
        return sum(product._price for product in self._shoppinglist)