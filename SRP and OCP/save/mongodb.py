from save.save import SavetoDB


class MongoDB(SavetoDB):
    def saveToDB(self, shopping_cart):
        print("Saving to MongoDB")
        for item in shopping_cart.getProducts():
            print(item._name, "\t", item._price)