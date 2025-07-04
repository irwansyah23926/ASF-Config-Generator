# 🎮 ASF Config Generator (Versi Aman - .env Protected)

Skrip Python untuk membuat konfigurasi ArchiSteamFarm dengan aman, tanpa menyimpan password, dan API key kamu dilindungi.

---

## ✅ Fitur

- 🔐 Tidak menyimpan password
- 🌱 API Key dan SteamID dibaca dari `.env` (tidak diupload)
- ⚙️ JSON config dibuat otomatis
- 📁 Output ke folder `config/`

---

## 📦 Cara Pakai

1. Buat file `.env` dari contoh:
   ```bash
   cp .env.example .env
   ```
   Lalu isi:
   ```
   STEAM_API_KEY=isi_api_key_anda
   STEAM_ID=isi_steam_id64_anda
   ```

2. Jalankan skrip:
   ```bash
   python asf_config_generator.py
   ```

3. Masukkan username dan password Steam (password tidak disimpan)

---

## 📁 Struktur Folder

```
asf-config-generator-safe/
├── config/                  ← kosong, tempat output JSON
├── .env.example             ← template .env (tidak sensitif)
├── .gitignore               ← mencegah file sensitif keupload
├── asf_config_generator.py ← script utama
└── README.md                ← panduan
```

---

## ⚠️ Jangan Lakukan Ini

- ❌ Upload `.env` ke GitHub
- ❌ Tulis API key atau SteamID langsung di script
- ❌ Simpan password di file apa pun

---

## 🤝 Credit

- ASF oleh JustArchi: https://github.com/JustArchiNET/ArchiSteamFarm
- Script ini dibuat oleh Irwansyah untuk konfigurasi pribadi yang aman
