from paymentmethod import CreditCardPayment,BitcoinPayment
from amountprocessor import AmountProcessor
c1=CreditCardPayment()
AmountProcessor(c1).pay(100)

AmountProcessor(BitcoinPayment()).pay(200)