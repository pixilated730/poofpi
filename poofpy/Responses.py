#poofpy/responses.py
from __future__ import annotations
from pydantic import BaseModel
from typing import Optional

class CryptoInvoice(BaseModel):
    amount: int
    crypto: str
    currency: str
    payment_link: str
    redirect: str

class CryptoCharge(BaseModel):
    address: str
    amount: str
    crypto: str
    currency: str
    due: str
    payment_link: str
    rate: str

class CreatePayout(BaseModel):
    address: str
    amount: str
    remaining_balance: str
    transaction_id: str
    redirect: str

class FetchWalletBalance(BaseModel):
    balance: str
    crypto: str

class FiatInvoice(BaseModel):
    amount: str
    payment: str
    currency: str
    payment_link : str

class FiatCharge(FiatInvoice):
    qr_code :str
    tracking_id:str

class FetchTransactions(BaseModel):
    amount: str
    currency: str
    payment_id: int
    payment_method: str
    paid: Optional[str]
