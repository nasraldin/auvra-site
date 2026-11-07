#!/usr/bin/env python3
"""Builds index.html (English) and ar/index.html (Arabic) from one template.

Run: python3 -I build.py
"""

from html import escape
from pathlib import Path

SITE = "https://nasraldin.github.io/auvra-site/"
PRIVACY = {
    "en": "https://auvra-proxy.app-services-671.workers.dev/legal/privacy",
    "ar": "https://auvra-proxy.app-services-671.workers.dev/legal/privacy/ar",
}
SUPPORT = {
    "en": "https://auvra-proxy.app-services-671.workers.dev/support",
    "ar": "https://auvra-proxy.app-services-671.workers.dev/support/ar",
}
EMAIL = "info@nasraldin.com"

# Karat, parts of gold per 1,000 (the app's purity table, D1).
KARATS = [("24", 999), ("22", 916), ("21", 875), ("18", 750)]

SCREENS = ["home", "markets", "details", "compare", "currencies", "calculator"]

COPY = {
    "en": {
        "title": "Auvra: gold prices, with the math shown",
        "description": (
            "Auvra follows the international gold spot price and works out what it "
            "means per gram in the UAE, Egypt and Saudi Arabia. Free for iPhone, in "
            "English and Arabic."
        ),
        "skip": "Skip to content",
        "other_lang": "العربية",
        "other_href": "ar/",
        "privacy": "Privacy",
        "to_dark": "Switch to dark appearance",
        "to_light": "Switch to light appearance",
        "h1": "Gold prices, with the math shown.",
        "lede": (
            "Auvra follows the international spot price and works out what it means "
            "per gram in the UAE, Egypt and Saudi Arabia. Every price is labelled with "
            "its type and the time it was updated."
        ),
        "soon": "Coming soon to the App Store",
        "soon_note": "Free for iPhone. No account, no ads.",
        "hero_alt_front": "Auvra Home screen showing the spot price and followed markets",
        "hero_alt_back": "Auvra Markets screen listing karats in three markets",
        "assay_h2": "One spot price, every karat.",
        "assay_p": (
            "Local prices start from the international spot price, convert it with the "
            "exchange rate, then apply the purity of the karat. Auvra tags them "
            "Spot-equivalent, because a shop adds its own premium and making charges."
        ),
        "formula": ["Spot price", "Exchange rate", "Purity"],
        "karat": "{k}K",
        "per_thousand": "parts gold in 1,000",
        "bars_label": "Purity of each karat",
        "screens_h2": "Inside the app",
        "screens_p": (
            "Four tabs: Home, Markets, Currencies and Settings. Compare and the "
            "calculator are one tap from Home."
        ),
        "prev": "Previous screens",
        "next": "Next screens",
        "screens": {
            "home": ("Home", "The spot price and the markets you follow, on one page."),
            "markets": ("Markets", "Common karats in three markets, per gram, ounce, tola or kilogram."),
            "details": ("Market details", "Price history from one day to the full record."),
            "compare": ("Compare", "Up to four markets on the same purity, unit and currency."),
            "currencies": ("Currencies", "Gold per gram in dozens of currencies."),
            "calculator": ("Calculator", "Weight, karat, premium, making charges and VAT, with every step shown."),
        },
        "screen_alt": "Auvra {name} screen",
        "promises_h2": "What you can count on",
        "promises": [
            ("Every price says what it is", "Spot or Spot-equivalent. A calculated price is never shown as a shop price."),
            ("Every price says when", "The update time is always on screen. A closed market, old data or no connection is shown plainly."),
            ("Nothing to sign up for", "No account, no ads, no tracking. Your favorites and settings stay on your iPhone."),
            ("Widgets that show their time", "Home Screen and Lock Screen widgets always show when they were last updated."),
            ("Your units, your currency", "Gram, troy ounce, tola or kilogram, in the currency you choose."),
            ("Made for Arabic and English", "Full right-to-left layout, Light and Dark appearance, Dynamic Type and VoiceOver."),
        ],
        "closing_h2": "Auvra is on its way to the App Store.",
        "closing_p": "Free, with no in-app purchases. Questions? Write to {email}.",
        "support": "Support",
        "privacy_policy": "Privacy policy",
        "fine": (
            "Prices are for information only and are not investment advice. "
            "Spot-equivalent prices are calculations, not shop prices. Spot price data "
            "from gold-api.com. Rates by Exchangerate.dev."
        ),
        "copyright": "© 2026 Nasr Aldin",
        "og_locale": "en_US",
    },
    "ar": {
        "title": "Auvra: أسعار الذهب والحساب أمامك",
        "description": (
            "يتابع Auvra سعر الذهب الفوري العالمي ويحسب ما يعادله للغرام في الإمارات "
            "ومصر والسعودية. مجاني على iPhone، بالعربية والإنجليزية."
        ),
        "skip": "انتقل إلى المحتوى",
        "other_lang": "English",
        "other_href": "../",
        "privacy": "الخصوصية",
        "to_dark": "التبديل إلى المظهر الداكن",
        "to_light": "التبديل إلى المظهر الفاتح",
        "h1": "أسعار الذهب، والحساب أمامك.",
        "lede": (
            "يتابع Auvra سعر الذهب الفوري العالمي، ويحسب ما يعادله للغرام في الإمارات "
            "ومصر والسعودية. ويظهر مع كل سعر نوعه ووقت آخر تحديث له."
        ),
        "soon": "قريبا على App Store",
        "soon_note": "مجاني على iPhone، بلا حساب ولا إعلانات.",
        "hero_alt_front": "شاشة الرئيسية في Auvra مع السعر الفوري والأسواق المتابعة",
        "hero_alt_back": "شاشة الأسواق في Auvra مع العيارات في ثلاثة أسواق",
        "assay_h2": "سعر فوري واحد لكل العيارات.",
        "assay_p": (
            "تبدأ الأسعار المحلية من السعر الفوري العالمي، ثم تحول بسعر الصرف، ثم "
            "يطبق عليها نقاء العيار. ويسميها Auvra «مكافئ محسوب»، لأن المحل يضيف "
            "علاوته وأجور الصياغة."
        ),
        "formula": ["السعر الفوري", "سعر الصرف", "النقاء"],
        "karat": "عيار {k}",
        "per_thousand": "جزء ذهب من كل 1000",
        "bars_label": "نقاء كل عيار",
        "screens_h2": "داخل التطبيق",
        "screens_p": (
            "أربعة تبويبات: الرئيسية والأسواق والعملات والإعدادات. والمقارنة والحاسبة "
            "على بعد لمسة من الرئيسية."
        ),
        "prev": "الشاشات السابقة",
        "next": "الشاشات التالية",
        "screens": {
            "home": ("الرئيسية", "السعر الفوري والأسواق التي تتابعها في صفحة واحدة."),
            "markets": ("الأسواق", "العيارات الشائعة في ثلاثة أسواق، بالغرام أو الأونصة أو التولة أو الكيلوغرام."),
            "details": ("تفاصيل السوق", "سجل الأسعار من يوم واحد حتى أقدم بيانات متاحة."),
            "compare": ("المقارنة", "حتى أربعة أسواق على العيار والوحدة والعملة نفسها."),
            "currencies": ("العملات", "سعر غرام الذهب بعشرات العملات."),
            "calculator": ("الحاسبة", "الوزن والعيار والعلاوة وأجور الصياغة والضريبة، مع كل خطوة في الحساب."),
        },
        "screen_alt": "شاشة {name} في Auvra",
        "promises_h2": "ما يمكنك الاعتماد عليه",
        "promises": [
            ("كل سعر يوضح نوعه", "فوري أو مكافئ محسوب. ولا يعرض السعر المحسوب على أنه سعر محل."),
            ("كل سعر يوضح وقته", "وقت التحديث ظاهر دائما. ويظهر بوضوح إغلاق السوق وقدم البيانات وانقطاع الاتصال."),
            ("لا شيء للتسجيل", "لا حساب ولا إعلانات ولا تتبع. تبقى المفضلة والإعدادات على جهاز iPhone."),
            ("أدوات تظهر وقتها", "أدوات الشاشة الرئيسية وشاشة القفل تعرض دائما وقت آخر تحديث."),
            ("بوحداتك وعملتك", "الغرام أو الأونصة أو التولة أو الكيلوغرام، بالعملة التي تختارها."),
            ("للعربية والإنجليزية", "اتجاه كامل من اليمين إلى اليسار، ومظهر فاتح وداكن، ودعم VoiceOver وأحجام الخط الكبيرة."),
        ],
        "closing_h2": "Auvra في طريقه إلى App Store.",
        "closing_p": "مجاني، بلا مشتريات داخل التطبيق. للاستفسار: {email}",
        "support": "الدعم",
        "privacy_policy": "سياسة الخصوصية",
        "fine": (
            "الأسعار للاطلاع فقط وليست نصيحة استثمارية. والأسعار المكافئة المحسوبة "
            "ليست أسعار محلات. بيانات السعر الفوري من gold-api.com، وأسعار الصرف من "
            "Exchangerate.dev."
        ),
        "copyright": "© 2026 Nasr Aldin",
        "og_locale": "ar_AR",
    },
}


def e(text: str) -> str:
    return escape(text, quote=True)


def page(lang: str) -> str:
    c = COPY[lang]
    root = "" if lang == "en" else "../"
    url = SITE if lang == "en" else SITE + "ar/"
    direction = "ltr" if lang == "en" else "rtl"
    shots = f"{root}assets/screens/{lang}/"
    dark_shots = f"{root}assets/screens/{lang}-dark/"
    email_link = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    prev_arrow, next_arrow = ("←", "→") if lang == "en" else ("→", "←")

    bars = "\n".join(
        f"""          <li class="bar">
            <span class="karat">{e(c["karat"].format(k=k))}</span>
            <span class="track" aria-hidden="true"><span class="fill" style="--fine: {fine / 10:.1f}%"></span></span>
            <span class="value">{fine}</span>
            <span class="unit">{e(c["per_thousand"])}</span>
          </li>"""
        for k, fine in KARATS
    )

    gallery = "\n".join(
        f"""        <li>
          <div class="phone"><img src="{shots}{name}.webp" data-dark="{dark_shots}{name}.webp" width="1320" height="2868" loading="lazy" decoding="async" alt="{e(c["screen_alt"].format(name=c["screens"][name][0]))}"></div>
          <h3>{e(c["screens"][name][0])}</h3>
          <p>{e(c["screens"][name][1])}</p>
        </li>"""
        for name in SCREENS
    )

    promises = "\n".join(
        f"""        <li>
          <h3>{e(title)}</h3>
          <p>{e(body)}</p>
        </li>"""
        for title, body in c["promises"]
    )

    formula = ' <i aria-hidden="true">×</i> '.join(f"<span>{e(part)}</span>" for part in c["formula"])

    return f"""<!doctype html>
<html lang="{lang}" dir="{direction}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(c["title"])}</title>
  <meta name="description" content="{e(c["description"])}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="en" href="{SITE}">
  <link rel="alternate" hreflang="ar" href="{SITE}ar/">
  <link rel="alternate" hreflang="x-default" href="{SITE}">
  <meta name="theme-color" content="#faf9f6" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0e0e0f" media="(prefers-color-scheme: dark)">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(c["title"])}">
  <meta property="og:description" content="{e(c["description"])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}assets/og-{lang}.png">
  <meta property="og:locale" content="{c["og_locale"]}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{root}favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300..700&display=swap">
  <link rel="stylesheet" href="{root}assets/site.css">
  <script>
    try {{
      var saved = localStorage.getItem("auvra-theme");
      if (saved === "light" || saved === "dark") document.documentElement.dataset.theme = saved;
    }} catch (error) {{}}
  </script>
</head>
<body>
  <a class="skip" href="#main">{e(c["skip"])}</a>
  <header class="wrap top">
    <a class="brand" href="{root or './'}" aria-label="Auvra">
      <img class="mark" src="{root}assets/mark.svg" width="34" height="34" alt="">
      <img class="word word-light" src="{root}assets/auvra-wordmark-{lang}-ink.svg" alt="" height="20">
      <img class="word word-dark" src="{root}assets/auvra-wordmark-{lang}-paper.svg" alt="" height="20">
    </a>
    <nav>
      <a class="privacy" href="{PRIVACY[lang]}">{e(c["privacy"])}</a>
      <button class="theme" type="button" data-to-dark="{e(c["to_dark"])}" data-to-light="{e(c["to_light"])}" aria-label="{e(c["to_dark"])}">
        <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 0 1 9.8 3.5a8.5 8.5 0 1 0 10.7 10.7Z"/></svg>
        <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg>
      </button>
      <a class="lang" href="{c["other_href"]}" hreflang="{'ar' if lang == 'en' else 'en'}" lang="{'ar' if lang == 'en' else 'en'}">{e(c["other_lang"])}</a>
    </nav>
  </header>

  <main id="main">
    <section class="wrap hero">
      <div>
        <h1>{e(c["h1"])}</h1>
        <p class="lede">{e(c["lede"])}</p>
        <div class="availability">
          <span class="soon"><img src="{root}assets/app-icon.png" width="32" height="32" alt="">{e(c["soon"])}</span>
          <small>{e(c["soon_note"])}</small>
        </div>
      </div>
      <div class="stage">
        <div class="phone back"><img src="{shots}markets.webp" data-dark="{dark_shots}markets.webp" width="1320" height="2868" alt="{e(c["hero_alt_back"])}"></div>
        <div class="phone front"><img src="{shots}home.webp" data-dark="{dark_shots}home.webp" width="1320" height="2868" alt="{e(c["hero_alt_front"])}" fetchpriority="high"></div>
      </div>
    </section>

    <section class="wrap assay" aria-labelledby="assay-title">
      <div class="copy">
        <h2 id="assay-title">{e(c["assay_h2"])}</h2>
        <p>{e(c["assay_p"])}</p>
        <p class="formula">{formula}</p>
      </div>
      <ul class="bars" aria-label="{e(c["bars_label"])}">
{bars}
      </ul>
    </section>

    <section class="screens" aria-labelledby="screens-title">
      <div class="wrap head">
        <div>
          <h2 id="screens-title">{e(c["screens_h2"])}</h2>
          <p>{e(c["screens_p"])}</p>
        </div>
        <div class="scroller-buttons">
          <button type="button" data-step="-1" aria-label="{e(c["prev"])}">{prev_arrow}</button>
          <button type="button" data-step="1" aria-label="{e(c["next"])}">{next_arrow}</button>
        </div>
      </div>
      <ul class="gallery" tabindex="0" aria-label="{e(c["screens_h2"])}">
{gallery}
      </ul>
    </section>

    <section class="wrap promises" aria-labelledby="promises-title">
      <h2 id="promises-title">{e(c["promises_h2"])}</h2>
      <ul>
{promises}
      </ul>
    </section>

    <section class="closing" aria-labelledby="closing-title">
      <div class="wrap">
        <img src="{root}assets/app-icon.png" width="168" height="168" alt="">
        <div>
          <h2 id="closing-title">{e(c["closing_h2"])}</h2>
          <p>{e(c["closing_p"]).format(email=email_link)}</p>
        </div>
      </div>
    </section>
  </main>

  <footer class="wrap">
    <div class="row">
      <nav>
        <a href="{SUPPORT[lang]}">{e(c["support"])}</a>
        <a href="{PRIVACY[lang]}">{e(c["privacy_policy"])}</a>
        <a href="{c["other_href"]}" lang="{'ar' if lang == 'en' else 'en'}">{e(c["other_lang"])}</a>
      </nav>
      <span dir="ltr">{e(c["copyright"])}</span>
    </div>
    <p class="fine">{e(c["fine"])}</p>
  </footer>

  <script>
    (function () {{
      var root = document.documentElement;
      var button = document.querySelector(".theme");
      var system = window.matchMedia("(prefers-color-scheme: dark)");
      function current() {{
        return root.dataset.theme || (system.matches ? "dark" : "light");
      }}
      function apply() {{
        var dark = current() === "dark";
        document.querySelectorAll("img[data-dark]").forEach(function (img) {{
          if (!img.dataset.light) img.dataset.light = img.getAttribute("src");
          var next = dark ? img.dataset.dark : img.dataset.light;
          if (img.getAttribute("src") !== next) img.setAttribute("src", next);
        }});
        document.querySelectorAll('meta[name="theme-color"]').forEach(function (meta) {{
          meta.content = dark ? "#0e0e0f" : "#faf9f6";
        }});
        button.setAttribute("aria-label", dark ? button.dataset.toLight : button.dataset.toDark);
      }}
      button.addEventListener("click", function () {{
        var next = current() === "dark" ? "light" : "dark";
        root.dataset.theme = next;
        try {{ localStorage.setItem("auvra-theme", next); }} catch (error) {{}}
        apply();
      }});
      system.addEventListener("change", apply);
      apply();
    }})();

    (function () {{
      var gallery = document.querySelector(".gallery");
      var buttons = document.querySelectorAll(".scroller-buttons button");
      if (!gallery || !buttons.length) return;
      var rtl = document.documentElement.dir === "rtl";
      function update() {{
        var max = gallery.scrollWidth - gallery.clientWidth;
        var pos = Math.abs(gallery.scrollLeft);
        buttons[0].disabled = pos <= 2;
        buttons[1].disabled = pos >= max - 2;
      }}
      buttons.forEach(function (button) {{
        button.addEventListener("click", function () {{
          var step = Number(button.dataset.step) * gallery.clientWidth * 0.8;
          gallery.scrollBy({{ left: rtl ? -step : step, behavior: "smooth" }});
        }});
      }});
      gallery.addEventListener("scroll", update, {{ passive: true }});
      window.addEventListener("resize", update);
      update();
    }})();
  </script>
</body>
</html>
"""


def main() -> None:
    here = Path(__file__).resolve().parent
    (here / "index.html").write_text(page("en"), encoding="utf-8")
    (here / "ar").mkdir(exist_ok=True)
    (here / "ar" / "index.html").write_text(page("ar"), encoding="utf-8")
    print("built index.html and ar/index.html")


if __name__ == "__main__":
    main()
