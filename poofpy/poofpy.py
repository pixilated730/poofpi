import requests
import json
import poofpy.Responses as Responses
from poofpy.Enums import *
class Poof:

    def __init__(self, api_key) -> None:
        self.__access_token = api_key
        self.__session = requests.session()
        self.__session.headers = {
            "Authorization": f"{self.__access_token}",
            "Content-Type": "application/json",
        }
        self.__base_url = "https://www.poof.io/"

    def __request(self, method, path, data=None):
        print(f"Request: {method} {self.__base_url}/{path}, Data: {data}")

        try:
            response = self.__session.request(method, f"{self.__base_url}/{path}", json=data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            #print(f"Response: {response.text}")
            return response.json()
        except requests.exceptions.RequestException as e:
            #print(f"Error in request: {e}")
            return None

        
        #fetch transaction 
    def fetch_transaction(self, payment_id) -> Responses.FetchTransactions:
        try:
            response = self.__request("POST", "api/v1/transaction", data={"transaction": str(payment_id)})

            return Responses.FetchTransactions(**response)
        except Exception:
            pass

    def create_crypto_invoice(self,amount,crypto:CryptoCurrencies,currency:Currency,redirect = "https://www.poof.io") -> Responses.CryptoInvoice:
        """
        Create a cryptocurrency invoice in the respective cryptocurrency you provide Poof. Redirect customers to the page link at checkout or host the invoice an iFrame on your website."""
        response = self.__request("POST","api/v1/create_invoice",data={"amount": str(amount), "crypto": crypto.value, "currency": currency.value, "redirect": redirect })
        return Responses.CryptoInvoice(**response)
    
    def create_crypto_charge(self,amount,crypto:CryptoCurrencies,currency:Currency) -> Responses.CryptoCharge:
        """Notify Poof to track specific payments and amounts to the wallet you link to Poof. An new address will be generated for each payment. Poof will send you a webhook notification to your server upon payment receipt. This endpoint can be used to create your own payment service."""
        response = self.__request("POST","api/v1/create_charge",data={"amount": str(amount), "crypto": crypto.value, "currency": currency.value})
        return Responses.CryptoCharge(**response)
    
    def create_payout(self,amount,crypto:CryptoCurrencies,address):
        """Create a payout in the respective cryptocurrency you provide Poof."""
        response = self.__request("POST","api/v1/payouts",data={"amount": str(amount), "crypto": crypto.value, "address ": address})
        return Responses.CreatePayout(**response)
    
    def FetchWalletBalance(self,crypto:CryptoCurrencies) -> Responses.FetchWalletBalance:
        """"This endpoint fetches your current cryptocurrency balance for Poof Wallets, available for payouts.
        POST /api/v1/balance
        """
        response = self.__request("POST","api/v1/balance",data={"crypto": crypto.value})
        return Responses.FetchWalletBalance(**response)
    
    def create_fiat_invoice(self,amount, payment:PaymentMethod, currency:Currency, redirect_url, success_url)-> Responses.FiatInvoice:
        """Create a direct link for processing the respective payment system.
        POST /api/v1/create_fiat_invoice
        json : amount, payment, currency, redirect_url, success_url"""
        response = self.__request("POST","api/v1/create_fiat_invoice",data={"amount": str(amount), "payment": payment.value, "currency": currency.value, "redirect_url": redirect_url, "success_url": success_url})
        return Responses.FiatInvoice(**response)
    
    def create_fiat_charge(self,amount, payment:PaymentMethod, currency:Currency, redirect_url, success_url) -> Responses.FiatCharge:
        """Create your own payment processor or payment flows with Poof processing payments in the backend..
        POST /api/v1/create_fiat_charge
        json : amount, payment, currency, redirect_url, success_url"""
        response = self.__request("POST","api/v1/create_fiat_charge",data={"amount": str(amount), "payment": payment.value, "currency": currency.value, "redirect_url": redirect_url, "success_url": success_url})
        return Responses.FiatCharge(**response)
    

    

    
        