from datetime import datetime

class CreditCard:
    def __init__(self, card_number: str, card_holder:str, balance: float, limit:float):
        self.card_holder = card_holder
        self.__card_number = card_number
        self.__balance = balance
        self.__limit = limit
        self.payment_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__payment_history = []       
        
    
    def validate_card_number(self, card_number):
        return self.__card_number == card_number
    
    
    
    def show_balance(self, card_number):
        if self.validate_card_number(card_number):
            return f'Sayın {self.card_holder} bakiyeniz: {self.__balance} TL...'
          
        else:
            return "Lütfen geçerli bir kart numarası giriniz..."
   
     
     
    def make_payment(self,card_number, amount):
        if self.validate_card_number(card_number):
           
            if amount <= self.__balance:
               
               if amount >= 1000:
                    discount = amount* 0.10
                    amount -= discount
                    self.__balance -= amount
                    self.__payment_history.append(f"Tarih: {self.payment_date} -  Harcama: {amount} TL...")
                    return f"Bu alışverişinizden {discount} TL indirim kazandınız. Güncel bakiyeniz: {self.__balance} TL... "
              
               else:
                    self.__balance -= amount
                    self.__payment_history.append(f"Tarih: {self.payment_date} -  Harcama: {amount} TL...")
                    return f"Sayın {self.card_holder} {self.payment_date} tarihinde {self.__card_number[:4]}*** numaralı kartınızdan {amount} TL tutarında harcama yapılmıştır. Güncel bakiyeniz: {self.__balance} TL..."
            
            else:
                return "Kart bakiyeniz harcama için yetersiz..."  
               
        else:
            return "Lütfen geçerli bir kart numarası giriniz..."
        
      
        
    def  show_payment_history(self,card_number):
        if self.validate_card_number(card_number):
            return self.__payment_history
        
        else:
            return "Lütfen geçerli bir kart numarası giriniz..."
            
      
            
    def credit_limit_increment(self, card_number, amount):
        if self.validate_card_number(card_number):
            self.__limit += amount
            return f"Kredi limitiniz {amount} TL arttırıldı. Yeni limit: {self.__limit} TL"
        
        else:
            return "Lütfen geçerli bir kart numarası giriniz..."
             
       
            
credit_card = CreditCard("1234-5678-9876-5432", "Sevgi Erdem", 50000, 20000)     
print(credit_card.show_balance("1234-5678-9876-5432"))
print(credit_card.make_payment("1234-5678-9876-5432", 100))
print(credit_card.show_payment_history("1234-5678-9876-5432"))
print(credit_card.credit_limit_increment("1234-5678-9876-5432", 15000))

        