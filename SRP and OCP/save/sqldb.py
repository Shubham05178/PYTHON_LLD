from save.save import SavetoDB


class SQLDB(SavetoDB):
    def saveToDB(self, shopping_cart):
        print("Saving to SQLDB")
        for item in shopping_cart.getProducts():
            print(item._name, "\t", item._price)