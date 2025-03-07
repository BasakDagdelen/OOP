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
