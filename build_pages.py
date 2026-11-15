#!/usr/bin/env python3
"""
Generator halaman detail Pesona Wakatobi.
Menjamin semua halaman memakai head/navbar/footer yang konsisten,
dan struktur komponen baru (hero content, card media, badge, tags).
"""
import pathlib
import re

BASE = pathlib.Path(__file__).parent

NAV_ITEMS = [
    ("index.html", "Beranda"),
    ("wangi-wangi.html", "Wangi-Wangi"),
    ("kaledupa.html", "Kaledupa"),
    ("tomia.html", "Tomia"),
    ("binongko.html", "Binongko"),
    ("kontak.html", "Kontak"),
]

ICONS = {
    "maps": '<path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>',
    "phone": '<path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>',
    "mail": '<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>',
    "whatsapp": '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.488"/>',
}

CURRENT = "index.html"


def svg(icon):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" '
        'focusable="false">' + ICONS[icon] + "</svg>"
    )


def nav(current):
    items = "\n".join(
        f'      <a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in NAV_ITEMS
    )
    return f"""  <nav class="navbar" aria-label="Navigasi utama">
    <a href="index.html" class="navbar-brand">
      <span class="logo"><img src="img/favicon-32.png" alt="" width="34" height="34" /></span>
      <span class="brand-text">Pesona Wakatobi<small>Four Islands</small></span>
    </a>
    <button class="hamburger" id="hamburger" aria-expanded="false" aria-controls="navLinks" aria-label="Buka menu navigasi">
      <span></span>
      <span></span>
      <span></span>
    </button>
    <div class="nav-links" id="navLinks">
{items}
    </div>
  </nav>"""


def head(title, desc, og_img):
    return f"""<!DOCTYPE html>
<html lang="id" class="no-js">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="author" content="Pesona Wakatobi" />
  <meta name="theme-color" content="#080f1e" />

  <meta property="og:type" content="website" />
  <meta property="og:locale" content="id_ID" />
  <meta property="og:site_name" content="Pesona Wakatobi" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="img/{og_img}" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="icon" href="img/favicon-32.png" sizes="32x32" />
  <link rel="apple-touch-icon" href="img/favicon-180.png" />
  <link rel="stylesheet" href="css/style.css" />

  <script>document.documentElement.classList.remove('no-js');</script>
</head>
<body>
  <a class="skip-link" href="#main">Lewati ke konten utama</a>

{nav(CURRENT)}"""


def footer(note="Website Pariwisata"):
    return f"""  <footer>
    <div class="footer-brand">
      <span class="logo"><img src="img/favicon-32.png" alt="" width="28" height="28" /></span>
      Pesona Wakatobi
    </div>
    <p>&copy; <span data-year>2026</span> {note} &middot; Taman Nasional Wakatobi, Sulawesi Tenggara</p>
  </footer>

  <script src="js/main.js" defer></script>
</body>
</html>
"""


def hero(eyebrow, title_html, subtitle, img, short=True, actions=""):
    cls = "hero hero--short" if short else "hero"
    return f"""    <section class="{cls}" style="background-image: url('img/{img}');">
      <div class="hero__content">
        <span class="eyebrow">{eyebrow}</span>
        <h1>{title_html}</h1>
        <p>{subtitle}</p>
{actions}      </div>
      <span class="scroll-hint" aria-hidden="true">Gulir</span>
    </section>
"""


def dest_card(img, alt, w, h, title, paragraphs, extra=""):
    paras = "\n".join(f"          <p>{p}</p>" for p in paragraphs)
    return f"""      <article class="dest-card">
        <div class="dest-card__media">
          <img src="img/{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async" />
        </div>
        <div class="desc">
          <h3>{title}</h3>
{paras}
{extra}        </div>
      </article>"""


def dest_grid(cards):
    body = "\n".join(cards)
    return f"""    <div class="destinations">
{body}
    </div>"""


# ==========================================================================
# WANGI-WANGI
# ==========================================================================
def build_wangi():
    cards = [
        dest_card(
            "dermaga-sombu.jpg",
            "Dermaga Sombu yang menjorok ke laut di Pulau Wangi-Wangi",
            750, 500,
            "Dermaga Sombu",
            [
                "Dermaga Sombu (Sombu Jetty), yang terletak di Desa Sombu, Wanci, adalah salah satu landmark wisata bahari di Pulau Wangi-Wangi. Dermaga kayu yang panjang dan estetik ini menjorok ke perairan jernih, menjadikannya lokasi yang sangat populer untuk berfoto, terutama saat momen matahari terbenam.",
                "Lebih dari sekadar jembatan biasa, Dermaga Sombu berfungsi sebagai gerbang entry langsung menuju dive site yang terkenal dan mudah diakses, bahkan untuk pemula. Berjalan di atasnya sudah menyajikan pemandangan air laut tosca yang tenang dan mengundang.",
                "Perairan di bawah dan sekitar Dermaga Sombu dikenal sebagai bagian dari keindahan Taman Nasional Wakatobi, menawarkan kekayaan terumbu karang dan biota laut yang memikau untuk kegiatan snorkeling dan diving. Lokasi ini dikenal sebagai Sombu Dive, ditandai dengan adanya patung Ikan Napoleon di dekatnya.",
            ],
        ),
        dest_card(
            "puncak-toliamba.jpg",
            "Pemandangan laut luas dari Puncak Toliamba di Wanci",
            1050, 700,
            "Puncak Toliamba",
            [
                "Panorama Laut dan Pulau: Dari ketinggian Toliamba, pengunjung dapat menikmati hamparan lautan biru yang luas berpadu dengan hijaunya pepohonan. Pada hari yang cerah, Anda dapat melihat pemandangan indah pulau-pulau di sekitar Kepulauan Wakatobi, bahkan konon hingga Pulau Buton.",
                "Spot Matahari Terbenam (Sunset): Tempat ini disebut-sebut sebagai salah satu lokasi terbaik di Wanci untuk menyaksikan momen sunset yang sangat menawan, di mana cahaya keemasan memancar di atas lautan.",
                "Lanskap Asri: Area Puncak Toliamba dikelilingi oleh pepohonan yang rindang dan alam yang masih asri, menciptakan suasana yang sejuk, tenang, dan damai, menjadikannya tempat favorit untuk bersantai atau sekadar nongkrong bagi muda-mudi dan keluarga.",
            ],
        ),
        dest_card(
            "marina-togo.jpg",
            "Area Marina Togo Mowondu di Wanci pada malam hari",
            653, 366,
            "Marina Togo Mowondu (Bypass Marina)",
            [
                "Di Wanci, area yang paling terkenal dengan nama &quot;Marina&quot; dikenal sebagai Marina Togo Mowondu atau sering juga disebut Bypass Marina. Lokasi ini merupakan destinasi wisata tepi laut yang sangat populer, bahkan bisa disebut sebagai pusat keramaian dan tempat berkumpulnya masyarakat lokal maupun wisatawan.",
                "Secara ringkas, Marina Togo Mowondu bukan hanya sekadar pelabuhan kecil (marina), tetapi telah berkembang menjadi taman kota tepi laut yang menjadi jantung kehidupan sosial, kuliner, dan rekreasi di Pulau Wangi-Wangi.",
            ],
        ),
        dest_card(
            "benteng-liya-togo.jpg",
            "Desa Benteng Liya Togo di Pulau Wangi-Wangi",
            700, 466,
            "Benteng Liya Togo",
            [
                "Benteng Liya Togo adalah salah satu situs sejarah dan budaya terpenting di Pulau Wangi-Wangi (Wanci), Wakatobi, yang terletak di Desa Liya Togo. Dibangun sekitar tahun 1200-an Masehi, benteng ini merupakan peninggalan dari masa kekuasaan Kesultanan Buton, berfungsi sebagai pusat pertahanan, pemerintahan, dan syiar Islam di wilayah tersebut.",
                "Struktur benteng ini dikenal memiliki arsitektur pertahanan yang kompleks dengan tiga lapis perlindungan, didirikan di atas ketinggian yang strategis sehingga selain memiliki nilai historis, ia juga menawarkan pemandangan indah ke arah laut dan perkampungan di sekitarnya.",
                "Di dalam area Benteng Liya Togo, terdapat dua peninggalan vital. Yang pertama adalah Masjid Mubarak, yang diperkirakan dibangun pada tahun 1546 dan diyakini sebagai salah satu masjid tertua di Sulawesi Tenggara, menjadi simbol penting penyebaran agama Islam di Wakatobi. Selain itu, terdapat pula Baruga (rumah adat) dan sejumlah Lawa (pintu gerbang atau pos jaga), yang semuanya mencerminkan kekayaan budaya dan sistem sosial masyarakat masa lalu.",
            ],
        ),
        dest_card(
            "goa-kontamale.jpg",
            "Goa Kontamale, pemandian alami di Desa Wanci",
            900, 600,
            "Goa Kontamale",
            [
                "Permandian Kontamale (atau sering disebut Goa Kontamale) adalah salah satu objek wisata yang sangat terkenal di Wanci (Pulau Wangi-Wangi), Wakatobi, Sulawesi Tenggara. Ini adalah pemandian umum alami yang menawarkan pengalaman unik dengan air jernih dari mata air dalam gua.",
                "Goa Kontamale juga menyimpan sebuah mitos yang dipercaya oleh warga setempat, yaitu mata air di goa ini dipercaya dapat mempermudah jodoh bagi mereka yang masih lajang atau yang mengalami kesulitan dalam hubungan percintaan (sulit menikah). Mitos ini konon berasal dari kisah sepasang kekasih di masa lalu yang akhirnya menikah setelah mandi di goa tersebut.",
                "Secara keseluruhan, Permandian Kontamale adalah tempat yang tepat bagi Anda yang mencari ketenangan dan ingin menikmati kesegaran air alami di tengah keindahan alam goa yang eksotis di Wanci.",
            ],
        ),
        dest_card(
            "sombu.jpg",
            "Dermaga kayu Sombu di Wanci pada sore hari",
            1400, 1400,
            "Dermaga Sombu Sunset",
            [
                "Suasana Dermaga Sombu paling dramatis terjadi pada jam-jam menuju matahari terbenam, ketika langit berubah warna menjadi gradasi jingga, ungu, dan biru tua di atas laut tosca yang tenang.",
                "Spot ini menjadi favorit fotografer sekaligus tempat paling nyaman untuk menikmati angin laut sore sambil menunggu matahari sepenuhnya tenggelam di balik cakrawala.",
            ],
        ),
    ]

    return f"""  <main id="main">
{hero("Pulau 01 &mdash; Wanci", "Pulau <span class=\"accent\">Wangi-Wangi</span>", "Pintu gerbang Wakatobi: pusat administrasi kabupaten, Dermaga Matahora, dan marina yang ramai.", "wangi-hero.jpg")}
    <div class="content container">
      <h2>Tentang Wangi-Wangi</h2>
      <p>
        Wangi-Wangi adalah pulau terbesar dan pusat administrasi Kabupaten Wakatobi. Pulau ini menjadi pintu masuk utama bagi wisatawan yang datang melalui Bandara Matahora. Nama &quot;Wangi-Wangi&quot; konon berasal dari harumnya bunga cengkeh dan pala yang tumbuh subur di pulau ini.
      </p>
      <p>
        Selain sebagai pusat pemerintahan, Wangi-Wangi menawarkan keindahan alam yang memikau, mulai dari pantai berpasir putih hingga spot snorkeling yang mudah diakses.
      </p>

      <h2>Destinasi Unggulan</h2>
{dest_grid(cards)}
    </div>
  </main>

"""


# ==========================================================================
# KALEDUPA
# ==========================================================================
def build_kaledupa():
    cards = [
        dest_card(
            "pulau-hoga.jpg",
            "Pulau Hoga dengan pantai pasir putih di dekat Pulau Kaledupa",
            900, 473,
            "Pulau Hoga",
            [
                "Pulau Hoga adalah salah satu permata tersembunyi di gugusan Kepulauan Wakatobi, Sulawesi Tenggara, dan secara administratif terletak berdekatan dengan Pulau Kaledupa.",
            ],
            extra="""          <h5>Daya Tarik Utama</h5>
          <p>Surga Penyelam (Diving &amp; Snorkeling): Hoga sangat terkenal di kalangan penyelam internasional karena dianggap sebagai salah satu lokasi terumbu karang terbaik di dunia. Di perairannya, terdapat keanekaragaman hayati laut yang luar biasa, dengan laporan yang menyebutkan ada sekitar 750 spesies koral dari total 850 spesies yang ada di dunia. Setidaknya ada 29 titik penyelaman yang tersebar di sekitarnya.</p>
          <p>Keheningan dan Keasrian: Pulau ini menawarkan suasana yang sangat tenang, asri, dan jauh dari keramaian, menjadikannya tempat yang sempurna untuk healing dan menikmati alam tropis yang murni.</p>
          <p>Pantai Pasir Putih: Pulau Hoga dikelilingi oleh pantai pasir putih yang bersih dan air laut yang sangat jernih dengan gradasi warna biru hingga tosca.</p>
""",
        ),
        dest_card(
            "benteng-ollo.jpg",
            "Benteng batu kuno dengan masjid tua di Lea Kaledupa",
            900, 600,
            "Benteng Ollo",
            [
                "Benteng Ollo di Desa Ollo Selatan, Pulau Kaledupa, merupakan salah satu peninggalan bersejarah utama di Wakatobi yang erat kaitannya dengan sistem pemerintahan lokal Barata Kaedupa di bawah naungan Kesultanan Buton. Benteng ini didirikan sebagai respons terhadap ancaman nyata dari bajak laut Tobelo (Sanggila) yang sering menyerang dan merampok wilayah Kaledupa.",
                "Dibangun dari batu gunung, pasir, dan kapur, benteng berbentuk persegi panjang ini memiliki fungsi krusial sebagai pusat pertahanan dan keamanan bagi masyarakat setempat, sekaligus menjadi tempat berlindung saat situasi genting.",
                "Selain fungsi militernya, Benteng Ollo juga berperan ganda sebagai pusat pemerintahan Barata Kaedupa dan pusat kegiatan keagamaan. Hal ini dibuktikan dengan keberadaan Masjid Agung Bente di dalam kompleks benteng. Masjid ini tidak hanya menjadi tempat ibadah tetapi juga pusat syiar dan pendidikan agama Islam di Kaledupa pada masa lampau. Dengan demikian, Benteng Ollo merupakan simbol kekuatan pertahanan, tata kelola pemerintahan, dan penyebaran peradaban Islam di Pulau Kaledupa.",
            ],
        ),
    ]

    return f"""  <main id="main">
{hero("Pulau 02 &mdash; Ade", "Pulau <span class=\"accent\">Kaledupa</span>", "Pulau budaya: warisan Kesultanan Buton, tenun ikat Suku Bajo, dan bersebelahan dengan Pulau Hoga.", "pulau-hoga.jpg")}
    <div class="content container">
      <h2>Tentang Kaledupa</h2>
      <p>
        Kaledupa adalah sebuah pulau di Kepulauan Wakatobi, Sulawesi Tenggara, yang terkenal dengan keindahan alam bawah lautnya, seperti spot diving dan keberadaan kuda laut mini (Pygmy Seahorse). Pulau ini juga menawarkan daya tarik budaya, kuliner khas, dan pengalaman menyaksikan langsung kehidupan Suku Bajo. Kaledupa secara administratif merupakan sebuah kecamatan di Kabupaten Wakatobi yang terdiri dari beberapa pulau seperti Kaledupa, Lentea, dan Darawa.
      </p>
      <p>
        Pulau ini juga dikenal sebagai pusat kebudayaan Suku Bajo dan memiliki komunitas yang sangat menjunjung tinggi kearifan lokal.
      </p>

      <h2>Destinasi Unggulan</h2>
{dest_grid(cards)}
    </div>
  </main>

"""


# ==========================================================================
# TOMIA
# ==========================================================================
def build_tomia():
    cards = [
        dest_card(
            "onemobaa.jpg",
            "Pulau Onemobaa (Pulau Tolandona) dengan terumbu karang",
            900, 598,
            "Pulau Onemobaa: Identitas dan Resort Selam Kelas Dunia",
            [
                "Pulau Onemobaa, yang juga dikenal dengan nama lokal Pulau Tolandona, adalah pulau kecil yang terletak di dekat Pulau Tomia, salah satu dari empat pulau utama di Wakatobi. Pulau ini menjadi sangat terkenal di kalangan penyelam internasional karena merupakan lokasi utama dari Wakatobi Dive Resort, sebuah resor mewah yang diakui secara global sebagai destinasi selam dan snorkeling premium. Akses ke pulau ini sering melalui penerbangan charter pribadi langsung dari Bali yang dikelola oleh resor, menjamin kondisi perairan yang sangat terawat dan eksklusif.",
            ],
        ),
        dest_card(
            "puncak-tomia.jpg",
            "Puncak Tomia di Desa Kahianga dengan vista kepulauan",
            640, 480,
            "Puncak Tomia",
            [
                "Puncak Tomia adalah salah satu destinasi wisata darat yang paling terkenal di Pulau Tomia, Wakatobi. Lokasinya berada di dataran tinggi Desa Kahianga, Kecamatan Tomia Timur. Berbeda dengan citra Wakatobi yang didominasi keindahan bawah laut, bukit ini memberikan pengalaman yang berbeda, yaitu menikmati keseluruhan panorama kepulauan dari ketinggian.",
            ],
        ),
        dest_card(
            "tadu-sangia.jpg",
            "Tebing karst Tadu Sangia yang menjulang di tepi laut Pulau Tomia",
            900, 600,
            "Tadu Sangia",
            [
                "Pemandangan Unik: Tadu Sangia terkenal karena memiliki formasi tebing-tebing batu karang (karst) yang menjulang di tepi laut. Kontras antara batu karang yang kokoh, vegetasi hijau, dan birunya air laut menciptakan pemandangan yang dramatis dan menarik.",
                "Spot Panjat Tebing: Kawasan Tadu Sangia, khususnya bagian &quot;Fatu Kolo&quot; atau &quot;Fatu Nomo,&quot; menjadi satu-satunya spot resmi untuk panjat tebing di Pulau Tomia. Hal ini menarik para petualang yang ingin menikmati tantangan fisik sambil disuguhi pemandangan laut Wakatobi dari ketinggian.",
                "Aktivitas Petualangan: Selain panjat tebing, kawasan ini juga cocok untuk berkemah di area sekitar tebing dan pantai, memberikan pengalaman staycation alam yang unik.",
            ],
        ),
        dest_card(
            "pantai-lakota.jpg",
            "Pantai Lakota di Pulau Tomia saat matahari terbenam",
            900, 600,
            "Pantai Lakota",
            [
                "Pantai Lakota adalah destinasi wisata pantai paling populer di Pulau Tomia, Wakatobi, yang terletak di sisi barat pulau, menjadikannya lokasi utama dan terbaik untuk menikmati pemandangan matahari terbenam (sunset) yang memikau. Keindahan alamnya berasal dari kombinasi pesisir pantai dengan tebing karang landai yang menyediakan sudut pandang tinggi untuk menyaksikan cakrawala laut yang luas, menciptakan suasana yang romantis dan tenang di golden hour.",
                "Selain menyuguhkan panorama alam yang spektakuler, pantai ini juga mudah dijangkau dan didukung oleh fasilitas sederhana seperti warung makan dan akomodasi di sekitarnya, menjadikannya tempat ideal bagi wisatawan yang mencari pengalaman bersantai di daratan Tomia, sebagai penyeimbang sempurna dari aktivitas selam dan snorkeling Wakatobi.",
            ],
        ),
        dest_card(
            "goa-kontamale.jpg",
            "Ruang goa dengan air jernih di tepi laut Pulau Tomia",
            900, 600,
            "Gua Te'e Wali",
            [
                "Gua Te'e Wali memiliki bentuk mulut yang cukup luas dengan diameter sekitar 6 meter dan cenderung berbentuk semi-vertikal. Jalan masuknya menuju dasar gua dikelilingi oleh pepohonan yang rimbun, menciptakan suasana yang sejuk dan asri di sekitar mulut gua. Suasananya yang tenang dan airnya yang bening menjadikan tempat ini sebagai lokasi yang sempurna untuk menikmati pagi hari atau bersantai, jauh dari hiruk pikuk.",
                "Secara keseluruhan, Te'e Wali merupakan bukti kekayaan geologi Pulau Tomia dan menjadi salah satu destinasi wisata darat yang memikau, menawarkan misteri alam berupa air tawar di tepi laut, yang sangat berharga bagi masyarakat kepulauan.",
            ],
        ),
        dest_card(
            "ampombero.jpg",
            "Tebing tinggi Ampombero menghadap Samudra Pasifik",
            555, 416,
            "Pantai Ampombero",
            [
                "Ampombero adalah salah satu destinasi ikonik di Pulau Tomia, Wakatobi, yang terletak di wilayah Desa Kulati, Tomia Timur. Lokasi ini dikenal karena keberadaan tebing-tebing tinggi yang menghadap langsung ke lautan luas, menawarkan panorama Samudra Pasifik yang spektakuler, menjadikannya spot favorit untuk fotografi, terutama saat matahari terbit dan terbenam.",
                "Keunikan utama Ampombero terletak pada namanya yang berarti &quot;melambaikan tangan&quot; dalam bahasa lokal. Tebing ini dulunya adalah titik krusial di mana masyarakat lokal berkumpul untuk mengantar dan mengucapkan selamat tinggal kepada sanak keluarga yang berlayar jauh, menjadikannya simbol kesetiaan, kerinduan, dan harapan akan kepulangan yang selamat di tengah kehidupan bahari yang dinamis.",
            ],
        ),
    ]

    return f"""  <main id="main">
{hero("Pulau 03 &mdash; Te'e", "Pulau <span class=\"accent\">Tomia</span>", "Surga penyelam: lebih dari 20 titik dive kelas dunia dengan visibilitas hingga 50 meter.", "onemobaa.jpg")}
    <div class="content container">
      <h2>Tentang Tomia</h2>
      <p>
        Tomia adalah surga bagi para penyelam dan pencinta laut. Pulau ini memiliki lebih dari 20 titik penyelaman kelas dunia yang diakui oleh komunitas diving internasional. Terumbu karang di sini termasuk yang paling utuh dan beragam di dunia.
      </p>
      <p>
        Dengan visibilitas air hingga 50 meter dan arus yang menantang, Tomia menawarkan pengalaman menyelam yang tak terlupakan.
      </p>

      <h2>Spot Diving &amp; Snorkeling</h2>
{dest_grid(cards)}
    </div>
  </main>

"""


# ==========================================================================
# BINONGKO
# ==========================================================================
def build_binongko():
    cards = [
        dest_card(
            "desa-mati.jpg",
            "Reruntuhan batu karang Taman Batu di Desa Mati, Pulau Binongko",
            900, 600,
            "Desa Mati &quot;Taman Batu&quot;",
            [
                "Tempat wisata misterius pertama ini berasal dari sebuah tempat yang terdiri dari karang berwarna hitam terhampar dari bibir pantai hingga ke puncak bukit. Warga setempat menyebut tempat ini sebagai Taman Batu.",
                "Di puncak bukit inilah dahulu terdapat sebuah desa bernama Desa Taduna. Desa ini dikelilingi oleh benteng yang terbuat dari batu karang untuk melindungi desa. Namun, pada suatu hari desa ini medadak ditinggalkan oleh penduduknya dan akhirnya menjadi desa mati.",
            ],
        ),
        dest_card(
            "mercusuar-sangia.jpg",
            "Mercusuar Sangia di Pulau Binongko",
            300, 168,
            "Mercusuar Sangia",
            [
                "Mercusuar Sangia dibangun sekitar tahun 1994. Kini mercusuar ini tidak berfungsi lagi.",
                "Meski relatif baru, bangunan ini terlihat rapuh dan mengalami kerusakan di beberapa titik termasuk tangga yang terputus. Hampir tak ada warga yang terlihat melintas di daerah ini.",
                "Menurut penuturan warga di tempat ini, dilarang menggunakan bahasa Kesultanan Buton dan juga pakaian berwarna merah. Jika pantangan dilanggar maka orang tersebut dipercaya akan mendapat celaka. Konon ketika Pulau Binongko ditaklukan oleh pasukan Kesultanan Buton, sebagian masyarakat Binongko merasa tidak rela dan itulah awalnya munculnya pantangan tersebut.",
            ],
        ),
        dest_card(
            "danau-kemento.jpg",
            "Danau Kemento yang dikelilingi hutan bakau di Pulau Binongko",
            900, 600,
            "Danau Kemento",
            [
                "Tempat wisata misterius selanjutnya tidak jauh dari Taman Batu terdapat Danau Kemento yang ditumbuhi dengan rimbunnya taman bakau. Sekilas danau ini tampak seperti danau lainnya yang ada di Indonesia. Namun, siapa sangka jika danau ini menyimpan sebuah menakutkan bagi warga masyarakat sekitar.",
            ],
        ),
    ]

    return f"""  <main id="main">
{hero("Pulau 04 &mdash; Tukang Besi", "Pulau <span class=\"accent\">Binongko</span>", "Pulau terpencil: warisan pandai besi, desa mati, dan mercusuar tua.", "desa-mati.jpg")}
    <div class="content container">
      <h2>Tentang Binongko</h2>
      <p>
        Nama Wakatobi, yang berasal dari empat pulau utamanya, sering disamakan dengan Tukang Besi&mdash;gugusan kepulauan itu sendiri. Namun, Binongko-lah yang secara historis dikenal sebagai &quot;Pulau Tukang Besi&quot;. Julukan ini berasal dari tradisi turun-temurun masyarakatnya yang memiliki keahlian luar biasa dalam pertukangan besi dan pandai besi. Sejak zaman dahulu, penduduk Binongko adalah produsen alat-alat pertanian, senjata tajam, dan peralatan rumah tangga yang terbuat dari besi, dan hasil karya mereka diperdagangkan hingga ke pulau-pulau lain di Nusantara. Keterampilan ini diwariskan dari generasi ke generasi dan masih dapat disaksikan di beberapa desa, menjadikannya pusat budaya kerajinan logam di Wakatobi.
      </p>

      <h2>Destinasi Unggulan</h2>
{dest_grid(cards)}
    </div>
  </main>

"""


# ==========================================================================
# KONTAK
# ==========================================================================
def build_kontak():
    phone = "+6282256109423"
    phone_display = "+62 822-5610-9423"
    wa = "6282256109423"
    email = "pesonawakatobi001@gmail.com"

    return f"""  <main id="main">
{hero("Hubungi Kami", "Mari <span class=\"accent\">Berkenalan</span>", "Punya pertanyaan tentang paket wisata, dive site, atau akomodasi di Wakatobi? Tim kami siap membantu.", "hero-wakatobi.jpg")}
    <div class="content container">
      <h2>Informasi Kontak</h2>
      <p>
        Jika Anda memiliki pertanyaan tentang destinasi wisata di Wakatobi, atau ingin merencanakan perjalanan, jangan ragu untuk menghubungi kami. Kami siap membantu Anda menjelajahi keindahan surga bawah laut Indonesia.
      </p>

      <div class="contact-info">
        <div class="contact-card contact-card--wide">
          <h3>Lokasi</h3>
          <p>Kantor Pariwisata Wakatobi<br />Jl. Raya Wangi-Wangi, Pulau Wangi-Wangi<br />Kabupaten Wakatobi, Sulawesi Tenggara<br />Indonesia</p>
          <div class="social-icons">
            <a href="https://maps.google.com/?q=Wakatobi" target="_blank" rel="noopener noreferrer" title="Lokasi di Google Maps" aria-label="Lokasi di Google Maps">
              {svg('maps')}
            </a>
          </div>
        </div>

        <div class="contact-card">
          <h3>Telepon</h3>
          <p><a href="tel:{phone}">{phone_display}</a></p>
          <div class="social-icons">
            <a href="tel:{phone}" title="Hubungi via Telepon" aria-label="Hubungi via telepon">
              {svg('phone')}
            </a>
          </div>
        </div>

        <div class="contact-card contact-card--wide">
          <h3>Email</h3>
          <p><a href="mailto:{email}">{email}</a></p>
          <div class="social-icons">
            <a href="mailto:{email}" title="Kirim Email" aria-label="Kirim email">
              {svg('mail')}
            </a>
          </div>
        </div>

        <div class="contact-card">
          <h3>Media Sosial</h3>
          <p>Hubungi kami langsung untuk update terbaru tentang Wakatobi.</p>
          <div class="social-icons">
            <a href="https://wa.me/{wa}" target="_blank" rel="noopener noreferrer" title="WhatsApp" aria-label="WhatsApp">
              {svg('whatsapp')}
            </a>
          </div>
        </div>
      </div>
    </div>
  </main>

"""


# ==========================================================================
# BUILD ALL
# ==========================================================================
PAGES = {
    "wangi-wangi.html": (
        "Wangi-Wangi &mdash; Pintu Gerbang Wakatobi | Pesona Wakatobi",
        "Panduan wisata Pulau Wangi-Wangi di Wakatobi: Dermaga Sombu, Puncak Toliamba, Marina Togo Mowondu, Benteng Liya Togo, dan Goa Kontamale.",
        "wangi-hero.jpg",
        build_wangi,
        "Website Pariwisata",
    ),
    "kaledupa.html": (
        "Kaledupa &mdash; Pulau Budaya Wakatobi | Pesona Wakatobi",
        "Panduan wisata Pulau Kaledupa di Wakatobi: Pulau Hoga dengan dive site kelas dunia, Benteng Ollo, warisan Kesultanan Buton, dan budaya Suku Bajo.",
        "pulau-hoga.jpg",
        build_kaledupa,
        "Website Pariwisata",
    ),
    "tomia.html": (
        "Tomia &mdash; Surga Penyelam Wakatobi | Pesona Wakatobi",
        "Panduan wisata Pulau Tomia di Wakatobi: Pulau Onemobaa, Puncak Tomia, Tadu Sangia, Pantai Lakota, Gua Te'e Wali, dan Pantai Ampombero.",
        "onemobaa.jpg",
        build_tomia,
        "Website Pariwisata",
    ),
    "binongko.html": (
        "Binongko &mdash; Pulau Tukang Besi | Pesona Wakatobi",
        "Panduan wisata Pulau Binongko di Wakatobi: Desa Mati Taman Batu, Mercusuar Sangia, Danau Kemento, dan warisan pandai besi khas Nusantara.",
        "desa-mati.jpg",
        build_binongko,
        "Website Pariwisata Resmi",
    ),
    "kontak.html": (
        "Kontak &mdash; Pesona Wakatobi",
        "Hubungi kantor pariwisata Wakatobi untuk informasi tentang perjalanan, panduan destinasi, dan reservasi.",
        "hero-wakatobi.jpg",
        build_kontak,
        "Website Pariwisata",
    ),
}


def main():
    global CURRENT
    for filename, (title, desc, og, builder, note) in PAGES.items():
        CURRENT = filename
        body = builder()
        html = head(title, desc, og) + "\n" + body + footer(note)
        (BASE / filename).write_text(html, encoding="utf-8")
        print(f"built {filename:22s} {len(html):6d} bytes")


if __name__ == "__main__":
    main()
