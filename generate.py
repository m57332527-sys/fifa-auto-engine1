#!/usr/bin/env python3
"""
Programmatic SEO generator – outputs 1,000+ high-intent static HTML guides
into `public/`. Each page focuses on wired vs wireless streaming physics,
includes JSON‑LD TechArticle schema, Tailwind via CDN, Amazon affiliate links
(tag=timevalue0e2-20) and the required disclaimer.
"""
import os
from datetime import date
from itertools import product

# ---------- DATA MATRICES ----------
devices      = ["Smart TV", "Firestick", "Roku"]
problems     = ["Buffer Drops", "Packet Loss", "Streaming Lag"]
services     = [
    "Netflix", "Prime Video", "Hulu", "Disney+", "HBO Max",
    "YouTube TV", "Apple TV+", "Peacock", "Paramount+", "ESPN+"
]
speeds_mbps  = [100, 200, 500, 1000]
years        = [2024, 2025]          # keep content feeling current
connections  = ["Wi-Fi 5", "Wi-Fi 6", "Ethernet"]

# Affiliate links (hardcoded tag)
AMAZON_CAT8 = "https://www.amazon.com/s?k=Cat8+Ethernet+Cable&tag=timevalue0e2-20"
AMAZON_HDMI = "https://www.amazon.com/s?k=HDMI+2.1+Cable&tag=timevalue0e2-20"

# Dynamic date for schema
TODAY = date.today().isoformat()

OUTPUT_DIR = "public"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------- HTML TEMPLATE GENERATOR ----------
def generate_html(device, problem, service, speed, year, conn):
    # Build a readable slug for filename
    slug = (f"{problem.lower().replace(' ', '-')}-{device.lower().replace(' ', '-')}"
            f"-{service.lower().replace(' ', '-')}-{speed}mbps-{year}-"
            f"{conn.lower().replace(' ', '-')}.html")
    
    title = f"Fix {problem} on {device} When Streaming {service} at {speed}Mbps in {year} – {conn} vs Wired"
    meta_desc = (
        f"Experiencing {problem} on your {device} while watching {service}? "
        f"Learn how wire‑line data transfer eliminates jitter versus {conn}. "
        f"Get the best Cat8 Ethernet & HDMI 2.1 cables for stable 4K/8K streaming."
    )
    
    # Main content – physics angle
    if conn == "Ethernet":
        intro_problem = (f"When you use {device} to watch {service} and hit {problem.lower()} "
                         f"even at {speed}Mbps, the cause is almost always wireless interference. "
                         f"Jitter, caused by random RF noise and packet collisions, introduces "
                         f"micro‑second timing variations that corrupt UDP streaming buffers.")
        wired_angle = ("With a Cat8 Ethernet cable you get a shielded, twisted‑pair path that "
                       "provides physical‑layer error correction and full‑duplex bandwidth. "
                       "This completely eliminates wireless jitter and delivers "
                       "deterministic latency – essential for 4K/8K DRM‑protected content.")
    else:
        intro_problem = (f"Streaming {service} on your {device} over {conn} often leads to "
                         f"{problem.lower()} because Wi‑Fi uses a shared, collision‑prone medium. "
                         f"Even at {speed}Mbps, bursty interference from neighbouring access points "
                         f"causes packet re‑transmissions that exceed the decoder's buffer tolerance.")
        wired_angle = ("Switching to a wired Ethernet connection removes this variability. "
                       "Data travels over a dedicated Cat8 cable with negligible crosstalk, "
                       "keeping jitter below 1ms and allowing the streaming buffer to stay "
                       "completely full. HDMI 2.1 cables then transport the decoded signal "
                       "losslessly to your display.")
    
    article_body = f"""
    <section class="mb-8">
        <p class="text-lg text-gray-300 mb-4">{intro_problem}</p>
        <p class="text-lg text-gray-300 mb-4">{wired_angle}</p>
        <p class="text-lg text-gray-300">
            To achieve this stability, we recommend using a high‑quality 
            <a href="{AMAZON_CAT8}" class="text-blue-400 hover:underline" target="_blank" rel="nofollow sponsored">Cat8 Ethernet Cable</a> 
            that supports up to 40Gbps and 2000MHz bandwidth, together with an 
            <a href="{AMAZON_HDMI}" class="text-blue-400 hover:underline" target="_blank" rel="nofollow sponsored">HDMI 2.1 Cable</a> 
            capable of 48Gbps for uncompressed 8K60 HDR video.
        </p>
    </section>
    <section class="mb-8">
        <h2 class="text-2xl font-semibold text-purple-300 mb-3">The Physics of Packet Loss vs. Wired Guarantees</h2>
        <p class="text-gray-300 mb-3">
            Wireless signals are subject to multipath fading, absorption, and interference. 
            A single dropped UDP packet forces the application‑layer buffer to request a 
            retransmission, causing visible {problem.lower()}. Wired Ethernet delivers 
            deterministic, contention‑free frames with CRC‑32 error detection at the physical 
            layer, virtually eliminating packet loss.
        </p>
        <p class="text-gray-300">
            When you couple a Cat8 backbone with an HDMI 2.1 cable, the entire pipeline – 
            from ISP to screen – maintains a constant, low‑jitter flow that even the most 
            demanding codecs (AV1, HEVC) require.
        </p>
    </section>
    """
    
    # JSON-LD TechArticle schema
    json_ld = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": title,
        "description": meta_desc,
        "datePublished": TODAY,
        "dateModified": TODAY,
        "author": {
            "@type": "Organization",
            "name": "TimeValue Hardware Guides"
        },
        "publisher": {
            "@type": "Organization",
            "name": "TimeValue Hardware Guides",
            "logo": {
                "@type": "ImageObject",
                "url": "https://yourdomain.com/logo.png"  # replace if desired
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://yourdomain.com/{slug}"
        }
    }
    
    # Full HTML page
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc}">
    <meta name="robots" content="index, follow">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">
        {__import__('json').dumps(json_ld, indent=2)}
    </script>
</head>
<body class="bg-gray-900 text-white font-sans antialiased">
    <header class="bg-black/40 backdrop-blur-sm sticky top-0 z-50 border-b border-gray-800">
        <div class="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
            <a href="/" class="text-xl font-bold text-purple-400">Hardware Streaming Guides</a>
            <nav class="text-sm space-x-4">
                <a href="#" class="hover:text-purple-300">Guides</a>
                <a href="#" class="hover:text-purple-300">About</a>
            </nav>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-4 py-12">
        <nav class="text-sm text-gray-400 mb-6">
            <a href="/" class="hover:text-white">Home</a> / 
            <span>{device} {problem}</span>
        </nav>
        
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-400">
            {title}
        </h1>
        <p class="text-gray-400 text-lg mb-10">Published: {TODAY} – Expert guide for {service} on {device}</p>
        
        {article_body}
        
        <div class="bg-gray-800 rounded-2xl p-6 mt-10 border border-gray-700">
            <h2 class="text-xl font-semibold text-yellow-400 mb-3">Recommended Hardware</h2>
            <ul class="space-y-2 text-gray-300">
                <li>➤ <a href="{AMAZON_CAT8}" target="_blank" rel="nofollow sponsored" class="text-blue-400 hover:underline">Cat8 Ethernet Cable</a> – Shielded, 40Gbps, eliminates jitter</li>
                <li>➤ <a href="{AMAZON_HDMI}" target="_blank" rel="nofollow sponsored" class="text-blue-400 hover:underline">HDMI 2.1 Cable</a> – 48Gbps, 8K60 HDR, eARC</li>
            </ul>
        </div>
    </main>

    <footer class="bg-black/60 border-t border-gray-800 mt-16">
        <div class="max-w-4xl mx-auto px-4 py-6 text-center text-sm text-gray-500">
            <p>As an Amazon Associate I earn from qualifying purchases. Product prices and availability are accurate as of the date/time indicated and are subject to change.</p>
            <p class="mt-2">&copy; {TODAY[:4]} TimeValue Hardware Guides. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>""", slug

# ---------- GENERATE ALL PAGES + SITEMAP ----------
pages = []
for device, problem, service, speed, year, conn in product(devices, problems, services,
                                                            speeds_mbps, years, connections):
    html_content, slug = generate_html(device, problem, service, speed, year, conn)
    filepath = os.path.join(OUTPUT_DIR, slug)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    pages.append(slug)

# Write sitemap.xml
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
base = "https://yourdomain.com/"   # Change to your actual domain after first deploy
for page in pages:
    sitemap += f"  <url><loc>{base}{page}</loc><lastmod>{TODAY}</lastmod></url>\n"
sitemap += "</urlset>"

with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)

print(f"✅ Generated {len(pages)} HTML pages and sitemap.xml in '{OUTPUT_DIR}/'")
