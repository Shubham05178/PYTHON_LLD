class AmountProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def pay(self, amount):
        self.payment_method.pay(amount)
