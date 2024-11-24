# Sitemap URL listesi
urls = [
    "https://www.ebubekirbastama.com.tr/LinkAcici.html",
    "https://www.ebubekirbastama.com.tr/ebs_makale_dizay.html",
    "https://www.ebubekirbastama.com.tr/ebstemplatematching.html",

]

# Sitemap XML formatının başlangıcı
sitemap_start = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

# Sitemap XML formatının sonu
sitemap_end = '''
</urlset>
'''

# URL'leri XML formatına dönüştürme
url_template = '''
    <url>
        <loc>{}</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
'''

# Sitemap içeriği
sitemap_content = sitemap_start
for url in urls:
    sitemap_content += url_template.format(url)

sitemap_content += sitemap_end

# XML dosyasını kaydetme
with open("sitemap.xml", "w", encoding="utf-8") as file:
    file.write(sitemap_content)

print("Sitemap XML dosyası oluşturuldu.")
