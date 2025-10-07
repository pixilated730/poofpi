#poofpy/emums.py
from enum import Enum
class CryptoCurrencies(Enum):
    Bitcoin = "btc"
    Ethereum = "ethereum"
    Litecoin = "ltc"
    Dogecoin = "doge"
    Coinbase = "coinbase"
    Solana   = "solana"
    Moonbeam = "moonbeam"
    
class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    BTC = "BTC"
    CNY = "CNY"
class PaymentMethod(Enum):
    Paypal = "paypal"
    Venmo = "venmo"
    CashApp = "cashapp"
    Skrill = "skrill"
    credit_card = "credit card"