#!/usr/bin/env python3
"""Genera todas las páginas HTML del sitio en español (/) e inglés (/en/).

Edita los textos y las apps en este archivo y ejecuta:

    python3 tools/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EMAIL = "mvergaraguerrero@proton.me"
GITHUB = "https://github.com/KbzonZito"
KOFI = "https://ko-fi.com/kbzonzito"
YEAR = 2026

# --------------------------------------------------------------------------
# Apps. El orden es el de la portada.
# --------------------------------------------------------------------------
APPS = [
    {
        "slug": "printer-hub",
        "name": "Printer Hub",
        "icon": "/assets/apps/printer-hub.png",
        "repo": f"{GITHUB}/printer-hub",
        "download": f"{GITHUB}/printer-hub/releases/latest",
        "license": "MIT",
        "version": "1.1",
        "platforms": {"es": ["Android"], "en": ["Android"]},
        "status": {"es": "Disponible", "en": "Available"},
        "short": {
            "es": "Controla tu impresora 3D con Klipper desde el teléfono.",
            "en": "Control your Klipper 3D printer from your phone.",
        },
        "lead": {
            "es": "Printer Hub habla directamente con Moonraker, la API de Mainsail y Fluidd, a través de tu Wi-Fi. Sin cuentas, sin nube y sin anuncios. Nació para la Creality Hi y funciona con cualquier impresora con Klipper y Moonraker.",
            "en": "Printer Hub talks directly to Moonraker, the API behind Mainsail and Fluidd, over your Wi-Fi. No account, no cloud, no ads. It was built for the Creality Hi and works with any printer running Klipper and Moonraker.",
        },
        "features": {
            "es": [
                ("Estado en vivo", "Progreso, capa, tiempo restante, temperaturas y parada de emergencia siempre a mano."),
                ("Cámara", "WebRTC de Creality, MJPEG o las webcams de Moonraker, a pantalla completa y con capturas."),
                ("Archivos y vista previa", "Sube, organiza e imprime. Vista previa del G-code capa por capa."),
                ("Notificaciones y widget", "Avisos con foto al terminar, pausar o fallar una impresión, incluso con la app cerrada."),
                ("Calibraciones guiadas", "PID, Z offset, input shaper, malla de la cama y editor de printer.cfg."),
                ("Varias impresoras", "Una vista general de todas, historial con estadísticas y coste por impresión."),
            ],
            "en": [
                ("Live status", "Progress, layer, time left, temperatures and an emergency stop always within reach."),
                ("Camera", "Creality WebRTC, MJPEG or your Moonraker webcams, full screen with snapshots."),
                ("Files and preview", "Upload, organise and print. Layer-by-layer G-code preview."),
                ("Notifications and widget", "Alerts with a photo when a print finishes, pauses or fails, even with the app closed."),
                ("Guided calibrations", "PID, Z offset, input shaper, bed mesh and a printer.cfg editor."),
                ("Several printers", "An overview of all of them, history with statistics and cost per print."),
            ],
        },
        "install": {
            "es": "Todavía no está en Google Play. Descarga el APK desde GitHub, o instálala con Obtainium para recibir las actualizaciones automáticamente.",
            "en": "It isn't on Google Play yet. Download the APK from GitHub, or install it with Obtainium to get updates automatically.",
        },
        "privacy": {
            "es": [
                ("Datos que recopila", "Ninguno. Printer Hub no tiene cuentas, analítica, anuncios ni servidor propio. Tus impresoras, ajustes y vistas previas guardadas se quedan en el teléfono, y puedes borrarlos en Ajustes → Almacenamiento."),
                ("Conexiones", "La app solo se conecta a las impresoras que tú agregas, directamente en tu red local o a través de tu propia VPN."),
                ("Permisos", "Internet y estado de la red, para hablar con tus impresoras. Notificaciones y servicio en primer plano, para avisarte del progreso de una impresión con la app cerrada."),
                ("Respaldos", "Si exportas un respaldo, el archivo se guarda donde tú elijas. La app no lo envía a ningún sitio."),
            ],
            "en": [
                ("Data collected", "None. Printer Hub has no account, analytics, ads or server of its own. Your printers, settings and saved previews stay on your phone, and you can delete them in Settings → Storage."),
                ("Connections", "The app only connects to the printers you add, directly on your local network or over your own VPN."),
                ("Permissions", "Internet and network state, to talk to your printers. Notifications and a foreground service, to keep you posted on a print while the app is closed."),
                ("Backups", "If you export a backup, the file is saved wherever you choose. The app never sends it anywhere."),
            ],
        },
    },
    {
        "slug": "bookloft",
        "name": "Bookloft",
        "icon": "/assets/apps/bookloft.png",
        "repo": f"{GITHUB}/Bookloft",
        "download": f"{GITHUB}/Bookloft/releases/latest",
        "license": "GPL-3.0",
        "version": "0.9",
        "platforms": {"es": ["Android"], "en": ["Android"]},
        "status": {"es": "Beta", "en": "Beta"},
        "short": {
            "es": "Tu biblioteca personal: estantes, sagas, notas y tus EPUB y PDF.",
            "en": "Your personal library: shelves, series, notes and your EPUBs and PDFs.",
        },
        "lead": {
            "es": "Organiza lo que lees, lo que quieres leer y lo que ya terminaste. Sin cuentas ni servidores: todo queda en tu dispositivo y tú decides dónde respaldarlo.",
            "en": "Keep track of what you're reading, what's next and what you've finished. No accounts, no servers: everything stays on your device and you decide where to back it up.",
        },
        "features": {
            "es": [
                ("Estantes", "Leyendo, próximos, leídos y sin terminar, con calificación, páginas, fechas, etiquetas y notas."),
                ("Autores y sagas", "Cada autor con sus sagas en orden, cuántos llevas y cuál sigue."),
                ("¿Qué leo ahora?", "Tres propuestas con su razón, a partir de lo que ya has leído."),
                ("Agrega libros a tu manera", "Busca en Open Library, escanea el ISBN, haz una foto a tu estantería o comparte un pantallazo."),
                ("Tu año en libros", "Leídos, páginas, autores y favoritos, listos para compartir como imagen."),
                ("Importa y respalda", "Goodreads, StoryGraph, Obsidian o CSV. Respaldos en CSV o ZIP que se fusionan sin perder nada."),
            ],
            "en": [
                ("Shelves", "Reading, up next, read and unfinished, with ratings, pages, dates, tags and notes."),
                ("Authors and series", "Every author with their series in order, how many you've read and which one is next."),
                ("What should I read next?", "Three picks with a reason, based on what you've already read."),
                ("Add books your way", "Search Open Library, scan the ISBN, snap your bookshelf or share a screenshot."),
                ("Your year in books", "Books read, pages, authors and favourites, ready to share as an image."),
                ("Import and back up", "Goodreads, StoryGraph, Obsidian or CSV. CSV or ZIP backups that merge without losing anything."),
            ],
        },
        "install": {
            "es": "Descarga el APK más reciente desde GitHub y ábrelo en el teléfono. Las versiones nuevas se instalan encima de la anterior y conservan tu biblioteca.",
            "en": "Download the latest APK from GitHub and open it on your phone. New versions install over the previous one and keep your library.",
        },
        "privacy": {
            "es": [
                ("Datos que recopila", "Ninguno. Bookloft no tiene cuentas ni servidor propio. Tu biblioteca, notas y archivos se guardan solo en tu dispositivo."),
                ("Conexiones", "La app solo se conecta a Open Library y Apple Books, para buscar libros y portadas; a Anthropic, solo si conectas tu propia API key; y a donde tú compartas un respaldo (Drive, correo, archivos)."),
                ("Tu API key", "Si usas las funciones de IA, tu API key de Anthropic se guarda cifrada en el Keystore del teléfono y nunca se incluye en los respaldos. Las imágenes que envíes a Claude se rigen por la política de privacidad de Anthropic."),
                ("Cámara y fotos", "Solo se usan cuando escaneas un ISBN o eliges una foto, y la imagen no sale del teléfono salvo que uses la IA con tu API key."),
            ],
            "en": [
                ("Data collected", "None. Bookloft has no accounts and no server of its own. Your library, notes and files are stored only on your device."),
                ("Connections", "The app only connects to Open Library and Apple Books, to search for books and covers; to Anthropic, only if you add your own API key; and wherever you choose to share a backup (Drive, email, files)."),
                ("Your API key", "If you use the AI features, your Anthropic API key is stored encrypted in the phone's Keystore and is never included in backups. Images you send to Claude are covered by Anthropic's privacy policy."),
                ("Camera and photos", "Only used when you scan an ISBN or pick a photo, and the image stays on your phone unless you use the AI with your API key."),
            ],
        },
    },
    {
        "slug": "cartera-cl",
        "name": "Cartera CL",
        "icon": "/assets/apps/cartera-cl.svg",
        "repo": None,  # repositorio privado
        "download": None,
        "license": None,
        "version": None,
        "platforms": {"es": ["Web", "PWA"], "en": ["Web", "PWA"]},
        "status": {"es": "En desarrollo", "en": "In development"},
        "short": {
            "es": "Sigue tu cartera de acciones de la Bolsa de Santiago.",
            "en": "Track your Santiago Stock Exchange portfolio.",
        },
        "lead": {
            "es": "Posiciones, rentabilidad, calendario de dividendos, metas de ingreso y análisis técnico para inversionistas en Chile. No compra ni vende: solo registra y analiza.",
            "en": "Positions, returns, a dividend calendar, income goals and technical analysis for investors in Chile. It doesn't buy or sell: it only records and analyses.",
        },
        "features": {
            "es": [
                ("Posiciones y rentabilidad", "Costo promedio, ganancia realizada y rentabilidad ponderada por tiempo frente al IPSA."),
                ("Dividendos", "Calendario con fecha límite y de pago, distinguiendo anunciados y proyectados."),
                ("Metas de ingreso", "Cuánto te rinde tu cartera al mes y cuánto te falta para tu meta."),
                ("Análisis técnico", "Gráficos de velas con indicadores y señales."),
                ("En pesos y en UF", "Precios diarios, UF, dólar e IPC actualizados automáticamente."),
                ("Instalable", "Úsala desde el navegador o agrégala a la pantalla de inicio del teléfono."),
            ],
            "en": [
                ("Positions and returns", "Average cost, realised gains and time-weighted return against the IPSA."),
                ("Dividends", "A calendar with record and payment dates, telling announced and projected apart."),
                ("Income goals", "How much your portfolio pays you each month and how far you are from your goal."),
                ("Technical analysis", "Candlestick charts with indicators and signals."),
                ("In pesos and UF", "Daily prices, UF, dollar and CPI updated automatically."),
                ("Installable", "Use it in the browser or add it to your phone's home screen."),
            ],
        },
        "install": {
            "es": "Cartera CL todavía está en desarrollo. Escríbeme si quieres probarla cuando abra.",
            "en": "Cartera CL is still in development. Email me if you'd like to try it when it opens.",
        },
        "privacy": None,  # se publicará cuando la app abra
    },
]

# --------------------------------------------------------------------------
# Textos de la interfaz
# --------------------------------------------------------------------------
T = {
    "es": {
        "base": "",
        "home_title": "KbzonZito · Desarrollador de apps",
        "home_desc": "Apps sencillas, sin cuentas ni anuncios, diseñadas y desarrolladas por KbzonZito.",
        "nav_apps": "Apps", "nav_about": "Sobre mí", "nav_contact": "Contacto",
        "contact_page": "contacto.html", "privacy_page": "privacidad.html",
        "theme_label": "Cambiar tema", "other_lang": "English", "other_code": "EN",
        "h1a": "Hago apps", "h1b": "que hacen una cosa, y la hacen bien.",
        "hero_p": "Soy KbzonZito, desarrollador independiente. Diseño, programo y mantengo cada app de principio a fin, sin cuentas, sin anuncios y con el código abierto.",
        "see_apps": "Ver mis apps", "write_me": "Escríbeme",
        "apps_count": lambda n: f"{n} apps",
        "about_p1": "Me gusta construir herramientas pequeñas y rápidas que resuelven un problema concreto: controlar mi impresora 3D, ordenar mis libros, seguir mis inversiones.",
        "about_p2": "Todas funcionan sin cuentas y guardan tus datos en tu dispositivo. Publico el código en GitHub, así que puedes ver cómo funcionan, reportar errores o proponer ideas.",
        "about_tags": ["Android", "Web", "TypeScript", "Código abierto"],
        "github_profile": "Ver mi perfil de GitHub",
        "band_h": "¿Una idea, un error o una sugerencia?",
        "band_p": "Respondo personalmente, normalmente en menos de 48 horas.",
        "contact_title": "Contacto y soporte",
        "contact_lead": "Para dudas, errores o sugerencias sobre cualquiera de mis apps, escríbeme. Respondo personalmente, normalmente en menos de 48 horas.",
        "contact_btn": "Escribir a",
        "contact_h2": "Para ayudarte más rápido",
        "contact_tips": [
            "Indica el nombre de la app y su versión.",
            "Cuéntame el modelo de tu teléfono y la versión de Android.",
            "Si es un error, describe los pasos para reproducirlo. Una captura ayuda mucho.",
        ],
        "contact_issues": "Si prefieres, también puedes abrir un issue en el repositorio de la app en GitHub.",
        "features_h": "Qué puedes hacer", "install_h": "Instalar", "support_h": "Soporte",
        "download": "Descargar APK", "view_code": "Ver código", "privacy": "Política de privacidad",
        "support_p": "¿Algo no funciona o tienes una sugerencia? Escríbeme a",
        "license": "Licencia", "version": "Versión",
        "privacy_title": lambda n: f"Política de privacidad de {n}",
        "privacy_intro": lambda n: f"Esta política explica qué información trata {n}, desarrollada por KbzonZito.",
        "updated": "Última actualización: 4 de noviembre de 2026",
        "privacy_tail": [
            ("Menores", "La app no recopila información de ninguna persona, incluidos los menores de 13 años."),
            ("Cambios", "Cualquier cambio se publicará en esta página con su fecha de actualización."),
        ],
        "privacy_contact": "Contacto",
        "privacy_contact_p": "Si tienes dudas sobre esta política, escribe a",
        "support_kofi": "Apoyar en Ko-fi",
        "nf_title": "Esta página no existe",
        "nf_lead": "Puede que el enlace esté mal escrito o que la página se haya movido.",
        "back_home": "Volver al inicio",
    },
    "en": {
        "base": "/en",
        "home_title": "KbzonZito · App developer",
        "home_desc": "Simple apps with no accounts and no ads, designed and built by KbzonZito.",
        "nav_apps": "Apps", "nav_about": "About", "nav_contact": "Contact",
        "contact_page": "contact.html", "privacy_page": "privacy.html",
        "theme_label": "Change theme", "other_lang": "Español", "other_code": "ES",
        "h1a": "I make apps", "h1b": "that do one thing, and do it well.",
        "hero_p": "I'm KbzonZito, an independent developer. I design, build and maintain every app from start to finish, with no accounts, no ads and open source code.",
        "see_apps": "See my apps", "write_me": "Email me",
        "apps_count": lambda n: f"{n} apps",
        "about_p1": "I like building small, fast tools that solve one specific problem: running my 3D printer, organising my books, tracking my investments.",
        "about_p2": "They all work without an account and keep your data on your device. The code is on GitHub, so you can see how they work, report bugs or suggest ideas.",
        "about_tags": ["Android", "Web", "TypeScript", "Open source"],
        "github_profile": "See my GitHub profile",
        "band_h": "An idea, a bug or a suggestion?",
        "band_p": "I reply personally, usually within 48 hours.",
        "contact_title": "Contact and support",
        "contact_lead": "For questions, bugs or suggestions about any of my apps, email me. I reply personally, usually within 48 hours.",
        "contact_btn": "Email",
        "contact_h2": "To help you faster",
        "contact_tips": [
            "Tell me the app's name and version.",
            "Include your phone model and Android version.",
            "If it's a bug, describe the steps to reproduce it. A screenshot helps a lot.",
        ],
        "contact_issues": "If you prefer, you can also open an issue in the app's GitHub repository.",
        "features_h": "What you can do", "install_h": "Install", "support_h": "Support",
        "download": "Download APK", "view_code": "View code", "privacy": "Privacy policy",
        "support_p": "Something not working, or have a suggestion? Email me at",
        "license": "License", "version": "Version",
        "privacy_title": lambda n: f"{n} privacy policy",
        "privacy_intro": lambda n: f"This policy explains what information {n}, developed by KbzonZito, handles.",
        "updated": "Last updated: 4 November 2026",
        "privacy_tail": [
            ("Children", "The app doesn't collect information from anyone, including children under 13."),
            ("Changes", "Any change will be published on this page with its update date."),
        ],
        "privacy_contact": "Contact",
        "privacy_contact_p": "If you have questions about this policy, email",
        "support_kofi": "Support on Ko-fi",
        "nf_title": "This page doesn't exist",
        "nf_lead": "The link may be mistyped, or the page may have moved.",
        "back_home": "Back to home",
    },
}

# path of each logical page per language
def url(lang, page, slug=None):
    b = T[lang]["base"]
    if page == "home":
        return f"{b}/"
    if page == "contact":
        return f"{b}/{T[lang]['contact_page']}"
    if page == "app":
        return f"{b}/apps/{slug}/"
    if page == "privacy":
        return f"{b}/apps/{slug}/{T[lang]['privacy_page']}"
    raise ValueError(page)

OTHER = {"es": "en", "en": "es"}

SUN = '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>'
GH = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.53-1.33-1.28-1.69-1.28-1.69-1.05-.71.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.19-3.1-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.84 1.19 3.1 0 4.42-2.7 5.4-5.26 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5z"/></svg>'
CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>'


def head(lang, title, desc, here, alt):
    t = T[lang]
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="{lang}" href="https://kbzonzito.github.io{here}">
<link rel="alternate" hreflang="{OTHER[lang]}" href="https://kbzonzito.github.io{alt}">
<link rel="alternate" hreflang="x-default" href="https://kbzonzito.github.io{here if lang == 'es' else alt}">
<meta name="theme-color" content="#ECEEEA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1D2220" media="(prefers-color-scheme: dark)">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&display=swap">
<link rel="stylesheet" href="/assets/style.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{url(lang, 'home')}">KbzonZito</a>
  <nav class="nav" aria-label="{t['nav_apps']}">
    <a href="{url(lang, 'home')}#apps">{t['nav_apps']}</a><a class="nav-about" href="{url(lang, 'home')}#about">{t['nav_about']}</a><a href="{url(lang, 'contact')}">{t['nav_contact']}</a>
  </nav>
  <a class="icon-btn lang" href="{alt}" hreflang="{OTHER[lang]}" lang="{OTHER[lang]}" title="{t['other_lang']}" aria-label="{t['other_lang']}">{t['other_code']}</a>
  <a class="icon-btn" href="{GITHUB}" title="GitHub" aria-label="GitHub">{GH}</a>
  <button class="icon-btn theme-toggle" type="button" aria-label="{t['theme_label']}">{SUN}{MOON}</button>
</div></header>
'''


def footer(lang):
    t = T[lang]
    return f'''
<footer class="site-footer"><div class="wrap">
  <span>© {YEAR} KbzonZito</span>
  <nav class="footer-links">
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <a href="{GITHUB}">GitHub</a>
    <a href="{KOFI}">{t['support_kofi']}</a>
  </nav>
</div></footer>
</body>
</html>
'''


def tags(app, lang):
    out = [f'<span class="tag">{p}</span>' for p in app["platforms"][lang]]
    cls = "tag status" if app["download"] else "tag status pending"
    out.append(f'<span class="{cls}">{app["status"][lang]}</span>')
    return "".join(out)


def home(lang):
    t = T[lang]
    rows = []
    for a in APPS:
        rows.append(f'''      <li>
        <a class="product" href="{url(lang, 'app', a['slug'])}">
          <img src="{a['icon']}" alt="" width="64" height="64" style="view-transition-name:icon-{a['slug']}">
          <div>
            <h3 style="view-transition-name:name-{a['slug']}">{a['name']}</h3>
            <p>{a['short'][lang]}</p>
          </div>
          <div class="product-end">
            <div class="meta">{tags(a, lang)}</div>
            {CHEV}
          </div>
        </a>
      </li>''')
    about_tags = "".join(f'<li class="tag">{x}</li>' for x in t["about_tags"])
    return head(lang, t["home_title"], t["home_desc"], url(lang, "home"), url(OTHER[lang], "home")) + f'''
<main>
  <section class="hero wrap">
    <h1><span>{t['h1a']}</span><span>{t['h1b']}</span></h1>
    <p>{t['hero_p']}</p>
    <div class="actions">
      <a class="btn" href="#apps">{t['see_apps']}</a>
      <a class="btn quiet" href="{url(lang, 'contact')}">{t['write_me']}</a>
    </div>
  </section>

  <section class="section wrap" id="apps">
    <div class="section-head">
      <h2>{t['nav_apps']}</h2>
      <p>{t['apps_count'](len(APPS))}</p>
    </div>
    <ul class="products">
{chr(10).join(rows)}
    </ul>
  </section>

  <section class="section wrap" id="about">
    <div class="about">
      <h2>{t['nav_about']}</h2>
      <div>
        <p>{t['about_p1']}</p>
        <p>{t['about_p2']}</p>
        <ul class="facts">{about_tags}</ul>
        <p class="gh-link"><a class="btn quiet" href="{GITHUB}">{GH}{t['github_profile']}</a></p>
      </div>
    </div>
  </section>

  <section class="wrap">
    <div class="contact-band">
      <div>
        <h2>{t['band_h']}</h2>
        <p>{t['band_p']}</p>
      </div>
      <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </section>
</main>
''' + footer(lang)


def contact(lang):
    t = T[lang]
    tips = "".join(f"<li>{x}</li>" for x in t["contact_tips"])
    return head(lang, f"{t['contact_title']} · KbzonZito", t["contact_lead"], url(lang, "contact"), url(OTHER[lang], "contact")) + f'''
<main class="wrap page">
  <h1>{t['contact_title']}</h1>
  <p class="lead">{t['contact_lead']}</p>
  <p><a class="btn" href="mailto:{EMAIL}">{t['contact_btn']} {EMAIL}</a></p>
  <div class="prose">
    <h2>{t['contact_h2']}</h2>
    <ul>{tips}</ul>
    <p>{t['contact_issues']}</p>
  </div>
</main>
''' + footer(lang)


def app_page(lang, a):
    t = T[lang]
    feats = "".join(f"<li><strong>{h}</strong><span>{d}</span></li>" for h, d in a["features"][lang])
    buttons = []
    if a["download"]:
        buttons.append(f'<a class="btn" href="{a["download"]}">{t["download"]}</a>')
    if a["repo"]:
        buttons.append(f'<a class="btn quiet" href="{a["repo"]}">{GH}{t["view_code"]}</a>')
    if a["privacy"]:
        buttons.append(f'<a class="btn quiet" href="{url(lang, "privacy", a["slug"])}">{t["privacy"]}</a>')
    if not a["download"]:
        buttons.insert(0, f'<a class="btn" href="mailto:{EMAIL}?subject={a["name"]}">{t["write_me"]}</a>')
    facts = []
    if a["version"]:
        facts.append(f'<span>{t["version"]} {a["version"]}</span>')
    if a["license"]:
        facts.append(f'<span>{t["license"]} {a["license"]}</span>')
    facts_html = f'<p class="app-facts">{"".join(facts)}</p>' if facts else ""
    return head(lang, f"{a['name']} · KbzonZito", a["short"][lang], url(lang, "app", a["slug"]), url(OTHER[lang], "app", a["slug"])) + f'''
<main class="wrap page">
  <div class="app-hero">
    <img src="{a['icon']}" alt="" width="96" height="96" style="view-transition-name:icon-{a['slug']}">
    <div>
      <h1 style="view-transition-name:name-{a['slug']}">{a['name']}</h1>
      <div class="meta">{tags(a, lang)}</div>
    </div>
  </div>
  <p class="lead">{a['lead'][lang]}</p>
  <p class="btn-row">{"".join(buttons)}</p>
  {facts_html}

  <section class="section app-section">
    <div class="section-head"><h2>{t['features_h']}</h2></div>
    <ul class="features">{feats}</ul>
  </section>

  <section class="section">
    <div class="section-head"><h2>{t['install_h']}</h2></div>
    <p class="narrow">{a['install'][lang]}</p>
  </section>

  <section class="section">
    <div class="section-head"><h2>{t['support_h']}</h2></div>
    <p class="narrow">{t['support_p']} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </section>
</main>
''' + footer(lang)


def privacy_page(lang, a):
    t = T[lang]
    blocks = list(a["privacy"][lang]) + t["privacy_tail"]
    body = "".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in blocks)
    return head(lang, f"{t['privacy']} · {a['name']}", t["privacy_title"](a["name"]), url(lang, "privacy", a["slug"]), url(OTHER[lang], "privacy", a["slug"])) + f'''
<main class="wrap page">
  <h1>{t['privacy_title'](a['name'])}</h1>
  <p class="updated">{t['updated']}</p>
  <div class="prose">
    <p>{t['privacy_intro'](a['name'])}</p>
    {body}
    <h2>{t['privacy_contact']}</h2>
    <p>{t['privacy_contact_p']} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</main>
''' + footer(lang)


def not_found():
    # 404 único y bilingüe (GitHub Pages solo admite uno)
    es, en = T["es"], T["en"]
    return head("es", f"404 · KbzonZito", es["nf_lead"], "/", "/en/") + f'''
<main class="wrap page">
  <h1>{es['nf_title']}</h1>
  <p class="lead">{es['nf_lead']}</p>
  <p class="lead" lang="en">{en['nf_title']}. {en['nf_lead']}</p>
  <p class="btn-row"><a class="btn" href="/">{es['back_home']}</a><a class="btn quiet" href="/en/" lang="en">{en['back_home']}</a></p>
</main>
''' + footer("es")


def write(path, html):
    p = ROOT / path.lstrip("/")
    if path.endswith("/"):
        p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print("  ", p.relative_to(ROOT))


if __name__ == "__main__":
    for lang in ("es", "en"):
        write(url(lang, "home"), home(lang))
        write(url(lang, "contact"), contact(lang))
        for a in APPS:
            write(url(lang, "app", a["slug"]), app_page(lang, a))
            if a["privacy"]:
                write(url(lang, "privacy", a["slug"]), privacy_page(lang, a))
    write("/404.html", not_found())
