🎮 ASF Config Generator (Versi Aman - Pakai .env)

Skrip Python ini membantu kamu membuat konfigurasi bot ArchiSteamFarm (ASF) secara otomatis, aman, dan hanya dari game Steam yang sudah terinstal dan masih memiliki kartu. Cocok untuk farming kartu dengan efisien tanpa membuka game secara nyata.





✅ Fitur Utama

🔐 Tidak menyimpan password

🔒 API Key & Steam ID disimpan di .env

🎯 Hanya farming dari game yang sudah diinstal dan punya kartu tersisa

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

🚀 Cara Menjalankan

Clone atau download repo ini

git clone https://github.com/namamu/asf-config-generator.git
cd asf-config-generator

Buat file .env dari template .env.example

STEAM_API_KEY=MASUKKAN_API_KEY_KAMU
STEAM_ID=MASUKKAN_STEAM_ID64_KAMU

Jalankan script:

python SafeCardFarmer_Fixed.py

Masukkan:

Username Steam kamu

Password Steam (hanya dipakai login pertama oleh ASF)

File konfigurasi akan otomatis dibuat di folder config/

Jalankan ASF seperti biasa dan farming otomatis dimulai 🎮

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

Script ini dibuat oleh: Irwansyah (luffy) 💡🔥

📬 Butuh Bantuan?

Buka tab "Issues" atau tinggalkan komentar di repo ini.

Selamat farming kartu dengan aman dan efisien! 🚀

