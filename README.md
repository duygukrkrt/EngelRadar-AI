♿ EngelRadar AI

> **Şehri gör, engeli bildir, değişime ortak ol.**  
> Yapay zeka destekli, vatandaş odaklı akıllı şehir ve B2G (Business-to-Government) operasyon yönetim platformu.

---

## 🚀 Proje Hakkında

**EngelRadar AI**, şehir içerisindeki kamusal engellerin (bozuk kaldırımlar, tıkalı yağmur giderleri, engelli rampası engelleri vb.) vatandaşlar tarafından zahmetsizce bildirilmesini ve belediye yönetimleri tarafından anlık olarak önceliklendirilip çözüme kavuşturulmasını sağlayan hibrit bir SaaS platformudur.

Geleneksel belediye şikayet süreçlerindeki kağıt kürek bürokrasisini ve karmaşayı ortadan kaldırarak; **vatandaş için tek tuşla resmi dilekçe**, **belediye için ise yapay zeka destekli karar destek ve risk haritası** sunar.

---

## 🌟 Temel Özellikler

### 🧑 1. Vatandaş Portalı (Mobil & Web Dostu)
* **Hızlı İhbar:** Sorunlu alanın fotoğrafını yüklemek ve konum girmek yeterlidir.
* **Yapay Zeka Analizi:** Gemini AI entegrasyonu sayesinde yüklenen görsel taranır, sorun otomatik olarak kategorize edilir ve 1-5 arasında **Risk Skoru** üretir.
* **Otomatik Dilekçe Üretimi:** Sistem, resmi yasal formatta kurumsal bir dilekçe metnini kullanıcı adına saniyeler içinde hazırlar ve belediyeye iletir.
* **Takım Takip Numarası:** Her bildirime özel üretilen `ENG-XXXXXX` kodu ile süreç şeffaf şekilde takip edilir.

### 🏛️ 2. Belediye Yönetim & Operasyon Paneli
* **Akıllı Risk Yoğunluk Haritası:** Şehir genelindeki şikayetlerin yoğunluğuna ve risk derecesine göre dinamik harita görselleştirmesi.
* **Canlı Gelen Dilekçe Akışı:** Tüm ihbarların anlık olarak listelendiği operasyonel tablo.
* **İnteraktif Dilekçe İnceleme:** Tablodan seçilen herhangi bir bildirimin yasal dilekçe metnini detaylı inceleme imkanı.
* **Hızlı Aksiyon Butonları:** 
  * 🚀 *Saha Ekibi Yönlendir*
  * ✅ *Çözüldü Olarak İşaretle*
* **Dahili Simülasyon Fallback Modu:** API anahtarı girilmediği veya bağlantı kopması yaşandığı durumlarda bile hackathon sunumlarının kesintisiz sürmesini sağlayan güvenli yedek mekanizma.

---

## 🛠️ Mimari ve Teknolojiler

Proje, hız, kararlılık ve modern arayüz tasarımı göz önünde bulundurularak şu teknoloji yığınıyla geliştirilmiştir:

* **Arayüz & Çatım:** [Streamlit](https://streamlit.io/) (Python tabanlı interaktif web uygulaması)
* **Yapay Zeka:** Google Gemini API (`gemini-1.5-flash`) - *Görsel ve metin analizi*
* **Veri İşleme & Görselleştirme:** Pandas, Pillow (PIL), Streamlit Native Components
* **Stil:** Özel Modern CSS Tasarımı (Inter font ailesi, özel KPI kartları, dinamik rozetler ve duyarlı düzen)

---

## ⚙️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. **Repoyu Klonlayın:**
   ```bash
   git clone [https://github.com/duygukrkrt/EngelRadar-AI.git](https://github.com/duygukrkrt/EngelRadar-AI.git)
   cd EngelRadar-AI
Gerekli Kütüphaneleri Yükleyin:

Bash
pip install streamlit pandas pillow google-generativeai
Uygulamayı Başlatın:

Bash
streamlit run app04.py
