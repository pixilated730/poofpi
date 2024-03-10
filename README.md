  
  
  
# Poof Python API Wrapper 
## Installing
```
pip install poofpy
```
### get your api key
1. login to [poof](https://www.poof.io/login)
2. create your api key from [here](https://www.poof.io/developers)
### Examples
#### Set your api key
```python
from poofpy import Poof
client = Poof("your api key here")

``` 
#### Creating crypto invoice 
```python
invoice = client.create_crypto_invoice(10,CryptoCurrencies.Bitcoin,Currency.USD)
print(invoice.payment_link)
```
#### Creating crypto charge
```python
charge = client.create_crypto_charge(10,CryptoCurrencies.Bitcoin,Currency.USD)
print(charge.address)
```
#### Creating fiat invoice
```python
invoice = client.create_fiat_invoice(100,PaymentMethod.Paypal, Currency.USD, "https://www.poof.io", "https://www.poof.io")
print(invoice.payment_link)
```
#### Creating fiat charge 
``` python
charge = client.create_fiat_charge(100,PaymentMethod.Paypal, Currency.USD, "https://www.poof.io", "https://www.poof.io")
print(charge.payment_link)
```
#### Getting Balance
```python 
obj = client.FetchWalletBalance(CryptoCurrencies.Litecoin)
print(obj.balance)
```
#### Payout
```python
client.create_payout(10,CryptoCurrencies.Litecoin,"Lc9oPPPLkUsjDTAH13wAcPRKJyNj9gydwC")
```

  
  
  
  
