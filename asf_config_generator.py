import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ---------------------------- ENV ----------------------------
STEAM_API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")

# ---------------------------- INPUT ----------------------------
BOT_NAME = "MyMainBot"
steam_username = input("Masukkan username Steam kamu: ")
steam_password = input("Masukkan password Steam kamu (tidak akan disimpan): ")

# ---------------------------- KONFIG ----------------------------
config = {
    "AutoStart": True,
    "Enabled": True,
    "SteamLogin": steam_username,
    "SteamPassword": steam_password,
    "SteamMasterClanID": 0,
    "SteamOwnerID": STEAM_ID,
    "GamesPlayedWhileFarming": [],
    "FarmingOrder": 0,
    "CustomGamePlayedWhileFarming": "",
    "UseLoginKeys": True,
    "SteamParentalPIN": "0",
    "TradingPreferences": 0,
    "ConnectionTimeout": 60,
    "OnlineStatus": 1,
    "BotBehaviour": 0
}

# ---------------------------- SIMPAN ----------------------------
config_dir = os.path.join("config")
os.makedirs(config_dir, exist_ok=True)

config_path = os.path.join(config_dir, f"{BOT_NAME}.json")
with open(config_path, "w") as f:
    json.dump(config, f, indent=4)

print(f"✅ Konfigurasi bot '{BOT_NAME}' berhasil dibuat di folder 'config/'.")
print("🔐 Catatan: Password hanya dipakai saat login pertama dan tidak disimpan ulang!")
