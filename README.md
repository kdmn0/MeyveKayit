# MeyveKayıt

MeyveKayıt, bir meyve halinden yapılan alışverişlerde müşteri bazlı toplam kilogram takibi yapmak için geliştirilmiş basit bir **Python masaüstü uygulamasıdır**.  
Uygulama, girilen verileri dosyada saklar ve program her açıldığında kayıtları otomatik olarak yükler.

## Özellikler

- Müşteri adı ve alınan kilogram bilgisi ekleme
- Aynı müşteri için kilogramları otomatik toplama
- Verileri `kayitlar.txt` dosyasında saklama
- Program kapatılsa bile verilerin korunması
- Basit ve kullanıcı dostu Tkinter arayüzü

## Kullanılan Teknolojiler

- Python 3
- Tkinter (GUI)
- Dosya işlemleri (TXT)

## Kullanım

- Müşteri Adı alanına müşteri ismini gir.
- Kg alanına alınan miktarı gir.
- Ekle butonuna bas.
- Aynı müşteri tekrar girildiğinde kilogram otomatik olarak eklenir.
- Tüm kayıtlar kayitlar.txt dosyasına kaydedilir.

[Geliştirici] : Yiğit Arda Kıdıman / kdmn0

**************************************************************************************************************************************************************************************************

# MeyveKayıt

MeyveKayıt is a simple **Python desktop application** designed to track total fruit purchases (in kilograms) per customer in a fruit market.  
The application stores all records in a file and automatically reloads them when restarted.

## Features

- Add customer name and purchased weight (kg)
- Automatically accumulates kilograms for existing customers
- Saves data to a local file (`kayitlar.txt`)
- Preserves records even after closing the application
- Simple and user-friendly Tkinter interface

## Technologies Used

- Python 3
- Tkinter (GUI)
- File handling (TXT)

## Usage

- Enter the customer name in the Customer Name field.
- Enter the purchased weight in kilograms (Kg field).
- Click the Add button.
- If the customer already exists, the entered weight is added to the previous total.
- All records are saved in kayitlar.txt.

[Developer] : Yiğit Arda Kıdıman / kdmn0
