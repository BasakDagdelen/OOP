## OOP Nedir?

Nesne Yönelimli Programlama (OOP), yazılım geliştirmede gerçek dünya nesnelerini modelleyerek kodun daha düzenli, modüler ve yeniden kullanılabilir olmasını sağlayan bir yaklaşımdır.

### Temel OOP Kavramları

* **Sınıf (Class):** Nesnelerin şablonudur. Özelliklerini (attributes) ve davranışlarını (methods) tanımlar.
* **Nesne (Object):** Sınıfın bir örneğidir. Sınıfın tanımladığı özelliklere ve davranışlara sahiptir.
* **Kapsülleme (Encapsulation):** Verileri ve metotları bir arada tutarak veri güvenliğini sağlar.
* **Kalıtım (Inheritance):** Bir sınıfın özelliklerini başka bir sınıfa aktararak kod tekrarını önler.
* **Çok Biçimlilik (Polymorphism):** Aynı metodun farklı nesnelerde farklı şekillerde çalışabilmesidir.
* **Soyutlama (Abstraction):** Karmaşık detayları gizleyerek sadece gerekli bilgileri göstermektir.
  <br><br>

## Proje Yapısı

`Class.py`, `Books` ve `Library` olmak üzere iki ana sınıftan oluşmaktadır.

### `Books` Sınıfı

Kitap nesnelerini temsil eder. Her kitap, başlık, yazar, yayın yılı ve tür gibi özelliklere sahiptir.

* `title`: Kitabın başlığı (string).
* `author`: Kitabın yazarı (string).
* `publication_year`: Kitabın yayın yılı (string).
* `type`: Kitabın türü (string).
* `show_info()` metodu, kitabın detaylarını ekrana yazdırır.

### `Library` Sınıfı

Kitapların bir listesini tutar. Kütüphaneye kitap eklenmesini ve tüm kitapların listelenmesini sağlar.

* `add_book(book)`: Kütüphaneye yeni bir kitap ekler. Kitabın kütüphanede olup olmadığını kontrol eder.
* `list_books()`: Kütüphanedeki tüm kitapları listeler.

## Örnek Kullanım

```python
# Kitap nesneleri oluştur
book1 = Books("Simyacı", "Paulo Coelho", 1988, "Roman")
book2 = Books("Suç ve Ceza", "Fyodor Dostoyevski", 1866, "Roman")
book3 = Books("Suç ve Ceza", "Fyodor Dostoyevski", 1866, "Roman")

# Kütüphane nesnesi oluştur
library = Library()

# Kitapları kütüphaneye ekle
library.add_book(book1)
library.add_book(book2)

# Kütüphanedeki tüm kitapları listele
library.list_books()

# Aynı kitabı tekrar eklemeyi dene
library.add_book(book3)

# Tüm kitapları tekrar listele
library.list_books()
```
## Çıktısı
```
'Simyacı' kütüphaneye eklendi.
'Suç ve Ceza' kütüphaneye eklendi.

Title: Simyacı
Author: Paulo Coelho
Publication year: 1988
Type: Novel

Title: Suç ve Ceza
Author: Fyodor Dostoyevski
Publication year: 1866
Type: Novel

'Suç ve Ceza kütüphanede mevcut...'

Title: Simyacı
Author: Paulo Coelho
Publication year: 1988
Type: Novel

Title: Suç ve Ceza
Author: Fyodor Dostoyevski
Publication year: 1866
Type: Novel
```
<br>

## Inheritance.py

*  Ödeme sistemi sınıflarını (kredi kartı, Bitcoin, Papara) ve örnek kullanım kodlarını içerir.

## Sınıflar

* `Payment`: Temel ödeme sınıfı. Diğer ödeme yöntemleri bu sınıftan türetilmiştir.
    * `__init__(self, amount: float)`: Ödeme tutarını alır.
    * `process_payment(self)`: Ödeme işlemini simüle eder.
 
 <br>
 
* `CreditCardPayment`: Kredi kartı ile ödeme sınıfı.
    * `__init__(self, amount: float, card_number: str, card_holder: str, expiry_date: str, cvv: str)`: Kredi kartı bilgilerini ve ödeme tutarını alır.
    * `process_payment(self)`: Kredi kartı ile ödeme işlemini simüle eder.
 <br>  
 
* `BitcoinPayment`: Bitcoin ile ödeme sınıfı.
    * `__init__(self, amount: float, wallet_address: str)`: Bitcoin cüzdan adresini ve ödeme tutarını alır.
    * `process_payment(self)`: Bitcoin ile ödeme işlemini simüle eder.
 <br>
    
* `PaparaPayment`: Papara ile ödeme sınıfı.
    * `__init__(self, amount: float, papara_id: str, recipient_name: str)`: Papara ID, alıcı adı ve ödeme tutarını alır.
    * `process_payment(self)`: Papara ile ödeme işlemini simüle eder.

## Örnek Kullanım

```python
credit_card_payment = CreditCardPayment(5412.95, "TRY", "123456789253", "Saygın Yılmaz", "12/01", "054")
credit_card_payment.process_payment()

bitcoin_payment = BitcoinPayment(10255, "TRY", "ec1788f3-817c-4c8b-8d81-98667d582510")
bitcoin_payment.process_payment()

papara_payment = PaparaPayment(12500, "TRY", "9c58173a-e00d-41a8-8fd9-620868baab55", "Burçak Demir")
papara_payment.process_payment()
```
## Çıktısı
```
Sayın Saygın Yılmaz, adınıza kayıtlı sonu 9253 ile biten kartınızdan 5412.95 tutarında ödeme gerçekleştirdiniz...
ec1788*** bitcoin cüzdan ile 10255 TL ödeme yapıldı. 
Sayın 9c5817*** no'lu kullanıcımız 2025-03-07 10:43 tarihinde hesabınızdan Burçak Demir adına 12500 TL para gönderilmiştir...

```
<br>

## Encapsulation.py

`CreditCard` sınıfı, kredi kartı bilgilerini ve işlemlerini yönetmek için kullanılır.

### Özellikler

-   `card_holder`: Kart sahibinin adı.
-   `__card_number`: Kart numarası (gizli).
-   `__balance`: Kart bakiyesi (gizli).
-   `__limit`: Kart limiti (gizli).
-   `payment_date`: Ödeme tarihi ve saati.
-   `__payment_history`: Ödeme geçmişi (gizli).

### Metotlar

-   `__init__(self, card_number: str, card_holder: str, balance: float, limit: float)`: Sınıfın yapıcı metodu. Kart bilgilerini başlatır.
-   `validate_card_number(self, card_number)`: Verilen kart numarasının geçerli olup olmadığını kontrol eder.
-   `show_balance(self, card_number)`: Kart bakiyesini gösterir.
-   `make_payment(self, card_number, amount)`: Karttan ödeme yapar. 1000 TL üzeri harcamalarda %10 indirim uygular.
-   `show_payment_history(self, card_number)`: Ödeme geçmişini gösterir.
-   `credit_limit_increment(self, card_number, amount)`: Kredi limitini artırır.

### Kullanım Örneği

```python
credit_card = CreditCard("1234-5678-9876-5432", "Sevgi Erdem", 50000, 20000)
print(credit_card.show_balance("1234-5678-9876-5432"))
print(credit_card.make_payment("1234-5678-9876-5432", 100))
print(credit_card.show_payment_history("1234-5678-9876-5432"))
print(credit_card.credit_limit_increment("1234-5678-9876-5432", 15000))
```
## Çıktısı
```
Sayın Sevgi Erdem bakiyeniz: 50000 TL...
Sayın Sevgi Erdem 2024-07-06 17:28 tarihinde 1234*** numaralı kartınızdan 100 TL tutarında harcama yapılmıştır. Güncel bakiyeniz: 49900 TL...
['Tarih: 2024-07-06 17:28 -  Harcama: 100 TL...']
Kredi limitiniz 15000 TL arttırıldı. Yeni limit: 35000 TL
```
<br>

## Encapsulation.py
`Encapsulation.py`, temel matematiksel işlemleri gerçekleştiren sınıflar ve bu sınıfları kullanarak işlemleri dinamik olarak çağıran bir fonksiyon içerir.

## Sınıflar

-   `Add_Process`: Toplama işlemini gerçekleştirir.
-   `Subtraction_Process`: Çıkarma işlemini gerçekleştirir.
-   `Multiplication_Process`: Çarpma işlemini gerçekleştirir.
-   `Division_Process`: Bölme işlemini gerçekleştirir.
-   `Mod_Process`: Mod (kalan) işlemini gerçekleştirir.

Her sınıf, `calculate` adında bir metoda sahiptir. Bu metot, iki tamsayı parametre alır ve ilgili matematiksel işlemi gerçekleştirir.

## Fonksiyon

-   `mathematical_process(process, a: int, b: int)`: Verilen işlem nesnesini ve iki tamsayıyı kullanarak matematiksel işlemi gerçekleştirir.

## Kullanım Örneği

```python

add = Add_Process()
subtraction = Subtraction_Process()
multiplication = Multiplication_Process()
divison = Division_Process()
mod = Mod_Process()

print(f'Add: {mathematical_process(add, 15, 10)}')
print(f'Subtraction: {mathematical_process(subtraction, 12, 4)}')
print(f'Multiplication: {mathematical_process(multiplication, 3 , 7)}')
print(f'Divison: {mathematical_process(divison, 44, 6)}' )
print(f'Mod: {mathematical_process(mod, 79, 13)}')
```

