# Dockerfile
FROM python:3.11-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Gerekli dosyaları kopyala
COPY . /app

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Botu çalıştır
CMD ["python", "bot.py"]
