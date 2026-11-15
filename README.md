# Pesona Wakatobi

Website pariwisata statis untuk Destinasi Wisata **Taman Nasional Wakatobi** — yaitu Empat Pulau Utama:
**Wangi-Wangi**, **Kaledupa**, **Tomia**, dan **Binongko** (Provinsi Sulawesi Tenggara).

Dibuat sebagai panduan informatif bagi wisatawan yang ingin menjelajahi keanekaragaman hayati
 bawah laut, warisan budaya, dan kealamian taman nasional terbesar di Indonesia.

## 🌊 Fitur

- **6 halaman** — Beranda + 4 halaman pulau + Kontak
- **Responsif penuh** — hamburger menu + layout adaptif di semua halaman (mobile & desktop)
- **Self-hosted gambar** — tidak ada hotlink ke situs pihak ketiga (tahan link rot & content rehosting)
- **Aksesibilitas** — skip-link, `aria-*`, fokus terlihat, `alt` pada seluruh gambar, `prefers-reduced-motion`
- **SEO & social** — meta description, Open Graph tags, favicon, `lang="id"`
- **Performa** — `loading="lazy"`, dimensi gambar eksplisit (anti layout shift), CSS/JS ter-cache terpisah
- **Tanpa dependency** — HTML/CSS/JS murni, tanpa build step, tanpa framework

## 📁 Struktur Project

```
Peson_wakatobi/
├── index.html          # Beranda + kartu 4 pulau
├── wangi-wangi.html    # Detail Pulau Wangi-Wangi
├── kaledupa.html       # Detail Pulau Kaledupa
├── tomia.html          # Detail Pulau Tomia
├── binongko.html       # Detail Pulau Binongko
├── kontak.html         # Halaman kontak
├── css/
│   └── style.css       # Satu sumber stylesheet (navbar, footer, komponen, responsive)
├── js/
│   └── main.js         # Hamburger, scroll-reveal, active nav, auto-update tahun
├── img/
│   ├── *.jpg           # Foto destinasi (self-hosted)
│   └── favicon-*.png   # Favicon
├── build_pages.py      # Generator halaman (opsional, untuk regenerasi konsisten)
└── README.md
```

## 🚀 Menjalankan

Repo ini purely static — cukup buka `index.html` di browser, atau jalankan server lokal:

```bash
# Python (tersedia di Kali)
python3 -m http.server 8000

# atau Node.js
npx serve .

# lalu buka http://localhost:8000
```

Deploy: upload seluruh isi folder ke **GitHub Pages**, **Netlify**, **Vercel**, atau hosting statis mana pun.
Tidak ada build step yang perlu dijalankan.

## 🛠️ Regenerasi Halaman

Semua halaman detail dibangun dari `build_pages.py` agar head/navbar/footer selalu konsisten.

```bash
# Butuh Python 3
uv run python build_pages.py
```

Script ini menulis ulang `wangi-wangi.html`, `kaledupa.html`, `tomia.html`, `binongko.html`, dan `kontak.html`.
Halaman `index.html` ditulis manual (kompleks secara visual).

## ♿ Aksesibilitas

- Tombol **"Lewati ke konten utama"** pada awal setiap halaman
- Menu mobile dapat diakses keyboard, ditutup dengan `Esc`, dan mengembalikan fokus
- Semua gambar punya teks alternatif deskriptif
- `prefers-reduced-motion` mematikan animasi untuk pengguna yang sensitif terhadap gerakan
- Konten tetap terbaca bila JavaScript dinonaktifkan (fallback `.no-js`)

## 📸 Credit Foto

Seluruh foto disimpan di folder `img/`. Foto ilustrasi untuk lokasi yang tidak tersedia
di sumber publik digenerasi sebagai representasi visual. Untuk penggunaan komersial,
ganti dengan foto dokumentasi asli.

## 📄 Lisensi

MIT — bebas digunakan dan dimodifikasi.
