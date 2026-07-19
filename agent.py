import json
from datetime import datetime

# טעינת הגדרות
with open("config.json", "r") as file:
    config = json.load(file)

print("🤖 Nautica Agent התחיל לעבוד")
print("זמן בדיקה:", datetime.now().strftime("%d/%m/%Y %H:%M"))

print("\nכללי המעקב:")
for rule in config["rules"]:
    print(rule)

print("\nדרישת מלאי:", config["stock_required"])
