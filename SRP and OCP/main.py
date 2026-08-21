from save.mongodb import MongoDB
from save.sqldb import SQLDB
from product.product import Product
from shoppingcart.shoppingcart import ShoppingCart
from invoice.invoice import Invoice


def main():
    cart = ShoppingCart()
    print("No of items:")
    item_count = int(input())

    for _ in range(item_count):
        product_name = input("Enter Product Name: ")
        product_price = int(input("Enter Product Price: "))
        cart.addProduct(Product(product_name, product_price))

    Invoice().printInvoice(cart)

    save_strategies = [MongoDB(), SQLDB()]
    for strategy in save_strategies:
        strategy.saveToDB(cart)


if __name__ == "__main__":
    main()