import streamlit as st
import pandas as pd
from PIL import Image
import google.generativeai as genai
import random
from datetime import datetime

# --- GEMINI API AYARI ---
API_KEY = "BURAYA_API_KEY_YAZIN"
if API_KEY != "BURAYA_API_KEY_YAZIN":
    genai.configure(api_key=API_KEY)

st.set_page_config(page_title="EngelRadar AI", page_icon="♿", layout="wide")

# ---------------------------------------------------------------- TASARIM (CSS)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0B1F3A;
    --navy-2: #12305A;
    --teal: #14B8A6;
    --orange: #F97316;
    --red: #EF4444;
    --yellow: #F59E0B;
    --green: #22C55E;
    --bg: #F4F7FB;
    --card: #FFFFFF;
    --text: #0F172A;
    --muted: #64748B;
}

html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }
.stApp { background: var(--bg); }
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.block-container { max-width: 1150px; padding-top: 1.5rem; padding-bottom: 4rem; }
p, label, li, span, div { font-size: 1.02rem; }

[data-testid="stSidebar"] { background: var(--navy); }
[data-testid="stSidebar"] * { color: #E2E8F0 !important; }
[data-testid="stSidebar"] .brand { font-size: 1.5rem; font-weight: 800; color: #fff !important; }
[data-testid="stSidebar"] .brand span { color: var(--teal) !important; }
[data-testid="stSidebar"] .tag { font-size: .85rem; color: #94A3B8 !important; margin-bottom: 1.5rem; }

.hero {
    background: linear-gradient(135deg, var(--navy) 0%, var(--navy-2) 60%, #0E7490 100%);
    border-radius: 24px; padding: 2.6rem 2.6rem; color: #fff; margin-bottom: 1.6rem;
    position: relative; overflow: hidden;
    box-shadow: 0 20px 40px -20px rgba(11,31,58,.6);
}
.hero::after {
    content: "♿"; position: absolute; right: 2rem; top: -1rem; font-size: 11rem;
    opacity: .08; line-height: 1;
}
.hero .pill {
    display: inline-block; background: rgba(20,184,166,.18); color: #5EEAD4;
    border: 1px solid rgba(94,234,212,.4); padding: .3rem .9rem; border-radius: 999px;
    font-size: .8rem; font-weight: 600; letter-spacing: .04em; margin-bottom: 1rem;
}
.hero h1 { color: #fff; font-size: 2.6rem; font-weight: 800; margin: 0 0 .5rem 0; line-height: 1.15; }
.hero h1 em { font-style: normal; color: var(--teal); }
.hero p { color: #CBD5E1; font-size: 1.15rem; margin: 0; max-width: 640px; }

.card {
    background: var(--card); border-radius: 18px; padding: 1.5rem 1.6rem;
    box-shadow: 0 1px 2px rgba(15,23,42,.05), 0 8px 24px -12px rgba(15,23,42,.12);
    border: 1px solid #E8EEF5; margin-bottom: 1rem;
}
.card h3 { margin: 0 0 .8rem 0; font-size: 1.25rem; font-weight: 700; color: var(--text); }

.kpi { border-left: 6px solid var(--teal); padding: 1.2rem 1.4rem; }
.kpi .label { font-size: .8rem; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); font-weight: 600; }
.kpi .value { font-size: 2.6rem; font-weight: 800; color: var(--text); line-height: 1.1; margin: .25rem 0; }
.kpi .delta { font-size: .85rem; font-weight: 600; color: #0F766E; }
.kpi.red    { border-left-color: var(--red); }    .kpi.red .delta { color: var(--red); }
.kpi.green  { border-left-color: var(--green); }  .kpi.green .delta { color: #15803D; }

.step { display: flex; gap: .9rem; align-items: flex-start; margin-bottom: 1rem; }
.step .num {
    min-width: 36px; height: 36px; border-radius: 50%; background: var(--teal);
    color: #fff; font-weight: 700; display: flex; align-items: center; justify-content: center;
}
.step b { display: block; color: var(--text); }
.step small { color: var(--muted); font-size: .9rem; }

.badge { padding: .25rem .75rem; border-radius: 999px; font-size: .82rem; font-weight: 600; white-space: nowrap; }
.b-red { background: #FEE2E2; color: #B91C1C; }
.b-yel { background: #FEF3C7; color: #B45309; }
.b-grn { background: #DCFCE7; color: #15803D; }
.b-blu { background: #DBEAFE; color: #1D4ED8; }

table.tbl { width: 100%; border-collapse: collapse; }
table.tbl th { text-align: left; font-size: .78rem; text-transform: uppercase; letter-spacing: .06em;
               color: var(--muted); padding: .7rem .8rem; border-bottom: 2px solid #E8EEF5; }
table.tbl td { padding: .95rem .8rem; border-bottom: 1px solid #EEF2F7; font-size: 1rem; }
table.tbl tr:hover td { background: #F8FAFC; }
.mono { font-family: ui-monospace, Menlo, monospace; font-weight: 600; color: var(--navy-2); }

.stTextInput input { border-radius: 12px; padding: .8rem 1rem; font-size: 1rem; }
[data-testid="stFileUploaderDropzone"] {
    border: 2px dashed var(--teal); background: #F0FDFA; border-radius: 16px; padding: 1.6rem;
}
[data-testid="stFileUploaderDropzoneInstructions"] > div > span { display: none; }
[data-testid="stFileUploaderDropzoneInstructions"] > div::before {
    content: "Fotoğrafı buraya sürükleyin"; font-weight: 600; display: block; color: #0F766E;
}
[data-testid="stFileUploaderDropzoneInstructions"] > div::after {
    content: "JPG veya PNG · en fazla 200 MB"; font-size: .85rem; color: var(--muted);
}
[data-testid="stFileUploaderDropzone"] button { font-size: 0; }
[data-testid="stFileUploaderDropzone"] button::after { content: "Dosya Seç"; font-size: 1rem; }

.stButton > button, .stDownloadButton > button {
    background: linear-gradient(135deg, var(--orange), #FB923C); color: #fff; border: none;
    border-radius: 12px; padding: .75rem 1.6rem; font-weight: 700; font-size: 1.05rem;
    box-shadow: 0 10px 20px -10px rgba(249,115,22,.7); width: 100%;
}
.stButton > button:hover { filter: brightness(1.06); color: #fff; }

.stTabs [data-baseweb="tab-list"] { gap: .5rem; border-bottom: none; }
.stTabs [data-baseweb="tab"] {
    background: #fff; border-radius: 12px; padding: .7rem 1.3rem; font-weight: 600;
    border: 1px solid #E8EEF5;
}
.stTabs [aria-selected="true"] { background: var(--navy); color: #fff; }
.stTabs [aria-selected="true"] p { color: #fff; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }
</style>
""", unsafe_allow_html=True)

# Session State (Canlı Liste ve Dilekçe Metinleri İçin)
if 'kayitlar' not in st.session_state:
    st.session_state['kayitlar'] = [
        {
            "no": "ENG-482910", "tarih": "24.10.2026", "kat": "Tıkalı Yağmur Gideri", "konum": "Merkez Mah. No:12", "puan": 5, "durum": "Saha ekibi yönlendirildi",
            "dilekce": "T.C. BELEDİYE BAŞKANLIĞI\nFen İşleri Müdürlüğü'ne,\n\nKonu: Altyapı / Tıkalı Yağmur Gideri Bildirimi\nTarih: 24.10.2026\n\nMerkez Mahallesi No:12 önünde bulunan yağmur giderinin tıkanması sonucu su birikintileri oluşmuş olup, yaya ve engelli geçişini engellemektedir. Gereğinin yapılmasını arz ederim."
        },
        {
            "no": "ENG-829102", "tarih": "23.10.2026", "kat": "Bozuk Kaldırım", "konum": "İnönü Cad. No:4", "puan": 3, "durum": "İncelemede",
            "dilekce": "T.C. BELEDİYE BAŞKANLIĞI\nFen İşleri Müdürlüğü'ne,\n\nKonu: Bozuk Kaldırım Bildirimi\nTarih: 23.10.2026\n\nİnönü Caddesi No:4 adresindeki kaldırım taşlarında çökme ve bozulmalar meydana gelmiştir. Yayaların güvenliği için onarılmasını arz ederim."
        },
        {
            "no": "ENG-391029", "tarih": "22.10.2026", "kat": "Çevre Kirliliği", "konum": "Cumhuriyet Meydanı", "puan": 2, "durum": "Çözüldü",
            "dilekce": "T.C. BELEDİYE BAŞKANLIĞI\nZabıta Müdürlüğü'ne,\n\nKonu: Çevre Kirliliği Bildirimi\nTarih: 22.10.2026\n\nCumhuriyet Meydanı çevresinde atık birikintileri oluşmuştur. Temizlik ekiplerince müdahale edilmesini arz ederim."
        }
    ]

def risk_rozet(p):
    if p >= 4: return f'<span class="badge b-red">● {p}/5 Kritik</span>'
    if p == 3: return f'<span class="badge b-yel">● {p}/5 Orta</span>'
    return f'<span class="badge b-grn">● {p}/5 Düşük</span>'

def durum_rozet(d):
    cls = {"Çözüldü": "b-grn", "İncelemede": "b-yel"}.get(d, "b-blu")
    return f'<span class="badge {cls}">{d}</span>'

# ---------------------------------------------------------------- SOL MENÜ
with st.sidebar:
    st.markdown('<div class="brand">♿ Engel<span>Radar</span> AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="tag">Akıllı Şehir Yönetim Sistemi</div>', unsafe_allow_html=True)
    sayfa = st.radio("Giriş türü", ["🧑 Vatandaş Portalı", "🏛️ Belediye Paneli"], label_visibility="collapsed")
    st.markdown("---")
    st.caption("EngelRadar AI v2.5 - Canlı Sistem")

# ================================================================ VATANDAŞ PORTALI
if sayfa.startswith("🧑"):
    st.markdown("""
    <div class="hero">
        <div class="pill">YAPAY ZEKA DESTEKLİ</div>
        <h1>Şehri gör, engeli bildir,<br><em>değişime ortak ol.</em></h1>
        <p>Fotoğrafı yükleyin; yapay zeka anında analiz etsin, risk puanını çıkarsın ve resmi dilekçenizi oluştursun.</p>
    </div>
    """, unsafe_allow_html=True)

    sol, sag = st.columns([1.6, 1], gap="large")

    with sol:
        st.markdown('<div class="card"><h3>📝 Sorun Bildirim Formu</h3>', unsafe_allow_html=True)
        foto = st.file_uploader("Sorunun fotoğrafı", type=["jpg", "jpeg", "png"])
        konum = st.text_input("📍 Konum / Adres", placeholder="Örn: Merkez Mah. Atatürk Cad. No:12")
        eposta = st.text_input("✉️ E-posta (takip için)", placeholder="ornek@email.com")
        gonder = st.button("🚀 Analiz Et ve Bildir")
        st.markdown('</div>', unsafe_allow_html=True)

        if foto is not None:
            image = Image.open(foto)
            st.image(image, caption="Yüklenen Görsel", use_container_width=True)

        if gonder:
            if not foto or not konum:
                st.warning("Lütfen bir fotoğraf yükleyin ve konum adresini girin!")
            else:
                with st.spinner("Yapay zeka görseli ve konumu analiz ediyor..."):
                    try:
                        model = genai.GenerativeModel('gemini-1.5-flash')
                        prompt = "Bu kamusal alan sorununu analiz et. SORUN: [Kısa sorun adı] RİSK: [1-5 arası rakam]"
                        response = model.generate_content([prompt, image])
                        ai_text = response.text
                        
                        sorun_turu = "Altyapı / Kamusal Engel"
                        risk_puani = 4
                        for line in ai_text.split('\n'):
                            if "SORUN:" in line: sorun_turu = line.split("SORUN:")[1].strip()
                            if "RİSK:" in line:
                                try: risk_puani = int(''.join(filter(str.isdigit, line.split("RİSK:")[1])))
                                except: risk_puani = 4
                    except Exception:
                        sorun_turu = "Bozuk Kaldırım ve Geçit Engeli"
                        risk_puani = 4

                    takip_no = f"ENG-{random.randint(100000, 999999)}"
                    bugun = datetime.now().strftime('%d.%m.%Y')
                    
                    yeni_dilekce_metni = f"""T.C. 
BELEDİYE BAŞKANLIĞI
Fen İşleri ve Zabıta Müdürlüğü'ne,

Konu: Kamusal Alan / Altyapı Arıza ve Risk Bildirimi hk.
Tarih: {bugun}

Şehir genelinde yürüttüğünüz kamusal iyileştirme ve vatandaş odaklı hizmet anlayışınıza istinaden; aşağıda konumu belirtilen bölgede yaya güvenliğini tehdit eden aksaklık tespit edilmiştir.

📍 BÖLGE / KONUM: {konum}
🤖 TESPİT EDİLEN SORUN: {sorun_turu} (Risk Skoru: {risk_puani}/5)

İlgili lokasyonda gerekli teknik incelemenin aciliyetle yapılarak saha ekiplerinizce çalışmaların başlatılmasını arz ederim.

Saygılarımla,
Bildirim Takip Numarası: {takip_no}"""

                    st.session_state['kayitlar'].insert(0, {
                        "no": takip_no, "tarih": bugun, "kat": sorun_turu, "konum": konum, "puan": risk_puani, "durum": "Yeni İhbar 🆕", "dilekce": yeni_dilekce_metni
                    })

                    st.success(f"Bildiriminiz başarıyla belediyeye iletildi! Takip Numaranız: **{takip_no}**")

    with sag:
        st.markdown("""
        <div class="card">
            <h3>💡 Nasıl Çalışır?</h3>
            <div class="step"><div class="num">1</div><div><b>Fotoğraf yükleyin</b><small>Sorunu net gösteren bir kare yeterli.</small></div></div>
            <div class="step"><div class="num">2</div><div><b>Yapay zeka analiz eder</b><small>Görsel taranır ve risk puanlanır.</small></div></div>
            <div class="step"><div class="num">3</div><div><b>Tek tuşla dilekçe</b><small>Resmi dilekçe otomatik oluşturulup sisteme düşer.</small></div></div>
            <div class="step"><div class="num">4</div><div><b>Süreci takip edin</b><small>Takip numarasıyla belediye durumu izlenir.</small></div></div>
        </div>
        """, unsafe_allow_html=True)

# ================================================================ BELEDİYE PANELİ
else:
    st.markdown("""
    <div class="hero">
        <div class="pill">🔒 BELEDİYE PERSONEL GİRİŞİ</div>
        <h1>Belediye Yönetim &amp; <em>Operasyon Paneli</em></h1>
        <p>Yapay zeka destekli karar destek ve saha yönetim sistemi.</p>
    </div>
    """, unsafe_allow_html=True)

    toplam_bildirim = len(st.session_state['kayitlar'])
    kritik_sayisi = sum(1 for k in st.session_state['kayitlar'] if k['puan'] >= 4)
    cozulen_sayisi = sum(1 for k in st.session_state['kayitlar'] if k['durum'] == "Çözüldü")

    k1, k2, k3 = st.columns(3)
    kpiler = [
        (k1, "", "Toplam Bildirim", str(toplam_bildirim), "↑ Canlı akış"),
        (k2, "red", "Kritik Acil İhbar", str(kritik_sayisi), "↑ Öncelikli"),
        (k3, "green", "Çözülen İhbar", str(cozulen_sayisi), "↑ Başarılı"),
    ]
    for kol, renk, ad, deger, delta in kpiler:
        kol.markdown(f"""
        <div class="card kpi {renk}">
            <div class="label">{ad}</div>
            <div class="value">{deger}</div>
            <div class="delta">{delta}</div>
        </div>""", unsafe_allow_html=True)

    st.write("")
    sekme1, sekme2 = st.tabs(["🗺️ Akıllı Öncelik Haritası", "📋 İş Emirleri & Dilekçe İnceleme"])

    with sekme1:
        harita = pd.DataFrame({
            "lat":  [41.3887, 41.3921, 41.3850, 41.3902, 41.3870],
            "lon":  [33.7827, 33.7790, 33.7880, 33.7861, 33.7765],
            "renk": ["#EF4444", "#F59E0B", "#22C55E", "#EF4444", "#22C55E"],
            "boyut": [140, 110, 80, 140, 80],
        })
        st.markdown('<div class="card"><h3>Risk Yoğunluk Haritası</h3>', unsafe_allow_html=True)
        st.map(harita, latitude="lat", longitude="lon", color="renk", size="boyut", height=420)
        st.markdown("""
        <span class="badge b-red">● Kritik</span>&nbsp;
        <span class="badge b-yel">● Orta</span>&nbsp;
        <span class="badge b-grn">● Düşük</span></div>""", unsafe_allow_html=True)

    with sekme2:
        st.markdown('<div class="card"><h3>📋 Canlı Gelen Dilekçe Akışı ve İnceleme</h3>', unsafe_allow_html=True)
        st.caption("Aşağıdaki listeden detayını görmek istediğiniz dilekçenin Takip Numarasını seçin:")
        
        # Tablo Görünümü
        satirlar = ""
        for k in st.session_state['kayitlar']:
            satirlar += (f"<tr><td class='mono'>{k['no']}</td><td>{k['tarih']}</td><td><b>{k['kat']}</b></td>"
                         f"<td>{k['konum']}</td><td>{risk_rozet(k['puan'])}</td><td>{durum_rozet(k['durum'])}</td></tr>")
        st.markdown(f"""
        <table class="tbl">
            <tr><th>Takip No</th><th>Tarih</th><th>Kategori</th><th>Konum</th><th>Risk</th><th>Durum</th></tr>
            {satirlar}
        </table>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # İnteraktif Dilekçe Seçim Kutusu
        secilen_no = st.selectbox(
            "🔍 İncelemek İçin Takip Numarası Seçin:", 
            [k['no'] for k in st.session_state['kayitlar']]
        )
        
        # Seçilen dilekçenin detayını bul ve göster
        secilen_kayit = next(k for k in st.session_state['kayitlar'] if k['no'] == secilen_no)
        
        st.markdown(f"#### 📄 Resmi Dilekçe Detayı: `{secilen_no}`")
        st.text_area("Kurumsal Dilekçe Metni", secilen_kayit['dilekce'], height=200)
        
        col_islem1, col_islem2 = st.columns(2)
        with col_islem1:
            if st.button("🚀 Saha Ekibi Yönlendir"):
                secilen_kayit['durum'] = "Saha Ekibi Yönlendirildi"
                st.success(f"{secilen_no} nolu bildirim için saha ekipleri yönlendirildi!")
                st.rerun()
        with col_islem2:
            if st.button("✅ Çözüldü Olarak İşaretle"):
                secilen_kayit['durum'] = "Çözüldü"
                st.success(f"{secilen_no} nolu bildirim çözüldü olarak güncellendi!")
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)