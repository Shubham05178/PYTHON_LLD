class Invoice:
    def printInvoice(self, shopping_cart):
        products = shopping_cart.getProducts()

        if not products:
            print("No products in cart")
            return

        name_width = max(len("Product Name"), max(len(item._name) for item in products))
        border = "*" * (name_width + 18)

        print("\n")
        print(border)
        print("Invoice")
        print(f'{"Product Name":<{name_width}}   Price')

        total = 0
        for item in products:
            total += item._price
            print(f'{item._name:<{name_width}}   {item._price}')

        print(border)
        print(f"Gross Amt: {total}$")
        print(border)