🎮 ASF Config Generator (Versi Aman - Pakai .env)

Skrip Python ini membantu kamu membuat konfigurasi bot ArchiSteamFarm (ASF) secara otomatis, aman, dan hanya dari game Steam yang masih memiliki kartu. Tools ini juga bisa difilter agar hanya memproses game yang sudah diinstal. Cocok untuk farming kartu dengan efisien tanpa membuka game secara nyata.







✅ Fitur Utama

🔐 Tidak menyimpan password

🔒 API Key & Steam ID disimpan di .env

🎯 Memilih hanya game yang masih memiliki kartu (bisa difilter hanya dari game terinstal)

⚙️ File .json konfigurasi dibuat otomatis

🧼 Tidak uninstall game dan farming berjalan di background

📦 Apa yang Dibutuhkan

Python 3.10 atau lebih baru

Download dari: https://www.python.org/downloads/

Centang "Add Python to PATH" saat install

Library Python: python-dotenv
Jalankan ini di terminal:

pip install python-dotenv

Steam API Key dan SteamID64

API Key: https://steamcommunity.com/dev/apikey

Cek SteamID64 kamu: https://steamid.io/

ArchiSteamFarm (ASF)

Download dari: https://github.com/JustArchiNET/ArchiSteamFarm/releases

Ekstrak ke folder terpisah seperti C:/ASF

🚀 Cara Cepat (Tinggal Download & Jalan)

Klik tombol hijau Code > Download ZIP di atas repositori ini, atau klik tombol "⬇️ Download ZIP" di atas, lalu ekstrak file-nya.

Buka terminal di dalam folder hasil ekstrak, lalu install dependensi:

pip install python-dotenv

Buat file .env dengan format seperti:

STEAM_API_KEY=MASUKKAN_API_KEY_KAMU
STEAM_ID=MASUKKAN_STEAM_ID64_KAMU

Jalankan script:

python SafeCardFarmer_Fixed.py

Ikuti instruksi di terminal, dan jalankan ASF untuk mulai farming otomatis!

🗂️ Struktur Folder

asf-config-generator/
├── config/                  ← kosong, akan diisi otomatis
├── .env.example             ← template API key dan ID
├── .gitignore               ← mencegah file sensitif keupload
├── SafeCardFarmer_Fixed.py ← script utama
└── README.md                ← panduan ini

⚠️ Yang Harus Dihindari

❌ Jangan upload file .env

❌ Jangan tulis password/API langsung di script

❌ Jangan upload config/*.json ke GitHub

❌ Jangan upload file .db dari ASF

🤝 Credit

ArchiSteamFarm (ASF) by JustArchi

Script ini dibuat oleh: Luffy x Kael 💡🔥

📬 Butuh Bantuan?

Buka tab "Issues" atau tinggalkan komentar di repo ini.

Selamat farming kartu dengan aman dan efisien! 🚀

