# XML Sitemap Generator

Bu proje, Python kullanarak bir **Sitemap XML** dosyası oluşturmak ve bu dosyayı kolayca yönetmek için basit bir araç sağlar. 

## Özellikler
- Belirlediğiniz URL listesinden bir `sitemap.xml` dosyası oluşturur.
- Sitemap dosyasını otomatik olarak belirli bir şablona göre oluşturur.
- **Google Search Console** ve diğer arama motorları için hazır bir sitemap sağlar.
- GitHub ile kolayca paylaşılabilir.

---

## Kullanım

### 1. Gerekli Ortamı Hazırlayın
1. Python'un bilgisayarınızda kurulu olduğundan emin olun (Python 3.6 veya üzeri).
2. Projeyi bilgisayarınıza indirin veya `generate_sitemap.py` dosyasını bir klasöre kaydedin.

---

### 2. URL Listesini Güncelleyin
- `generate_sitemap.py` dosyasının başında bulunan `urls` değişkenine kendi URL'lerinizi ekleyin:
    ```python
    urls = [
        "https://www.orneksite.com/page1.html",
        "https://www.orneksite.com/page2.html",
        "https://www.orneksite.com/page3.html",
    ]
    ```

---

### 3. Script'i Çalıştırın
1. Terminal veya Komut İstemcisi'ni açın.
2. Dosyanın bulunduğu dizine gidin:
    ```bash
    cd <dosyanın_bulunduğu_klasör>
    ```
3. Aşağıdaki komut ile çalıştırın:
    ```bash
    python generate_sitemap.py
    ```

- Çalıştırma sonrası aynı dizinde `sitemap.xml` dosyası oluşturulacaktır.

---

### 4. GitHub Üzerinde Yayınlama
1. GitHub hesabınıza giriş yapın ve bir repository oluşturun.
2. `sitemap.xml` dosyasını repository'ye yükleyin.
3. Dosyanız artık **GitHub** üzerinde barındırılmaktadır.

---

## Google Search Console ile Entegrasyon
1. Google Search Console'a giriş yapın.
2. Sitenizi doğrulayın.
3. `sitemap.xml` dosyanızın GitHub bağlantısını kullanarak yeni bir sitemap ekleyin.

---

## Örnek Kod
```python
urls = [
    "https://www.orneksite.com/page1.html",
    "https://www.orneksite.com/page2.html",
    "https://www.orneksite.com/page3.html",
]

sitemap_start = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

sitemap_end = '''
</urlset>
'''

url_template = '''
    <url>
        <loc>{}</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
'''

sitemap_content = sitemap_start
for url in urls:
    sitemap_content += url_template.format(url)
sitemap_content += sitemap_end

with open("sitemap.xml", "w", encoding="utf-8") as file:
    file.write(sitemap_content)

print("Sitemap XML dosyası oluşturuldu.")
