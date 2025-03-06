from uuid import uuid4
from datetime import datetime

class Payment: 
    def __init__(self, amount: float):
        self.amount = amount      
        
    def process_payment(self):
        print (f'{self.amount} tutarında ödeme gerçekleştirildi...')
 
   
        
class CreditCardPayment(Payment):   
    def __init__(self, card_number: str, card_holder: str, expiry_date:str, cvv: str, amount):
        super().__init__(amount)
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        self.cvv = cvv
        
        
    def  process_payment(self):
        print (f'Sayın {self.card_holder}, adınıza kayıtlı sonu {self.card_number[-4:]} ile biten kartınızdan {self.amount} tutarında ödeme gerçekleştirdiniz...')
      
       

class BitcoinPayment(Payment):  
    def __init__(self, amount, wallet_address:str):
        super().__init__(amount)
        self.wallet_address = wallet_address
        
    def process_payment(self):
        print(f'{self.wallet_address[:6]}*** bitcoin cüzdan ile {self.amount} TL ödeme yapıldı. ')
     
        
        
class PaparaPayment(Payment):        
    def __init__(self, papara_id:str, recipient_name:str, amount):
        super().__init__(amount)
        self.papara_id = papara_id
        self.recipient_name = recipient_name
        self.payment_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        
    def process_payment(self):  
        print(f"Sayın {self.papara_id[0:6]}*** no'lu kullanıcımız {self.payment_date} tarihinde hesabınızdan {self.recipient_name} adına {self.amount} TL para gönderilmiştir...")
  
  
     
credit_card_payment = CreditCardPayment("123456789253", "Saygın Yılmaz", "12/01", "054", 5412.95)
credit_card_payment.process_payment()

bitcoin_payment =BitcoinPayment(10255, "ec1788f3-817c-4c8b-8d81-98667d582510");
bitcoin_payment.process_payment()

papara_payment= PaparaPayment("9c58173a-e00d-41a8-8fd9-620868baab55", "Burçak Demir", 12500)
papara_payment.process_payment()

#print(uuid4())