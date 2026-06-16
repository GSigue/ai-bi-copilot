import os

EXPECTED_FILES = [
    # API
    "app/api/main.py",

    # Core
    "app/core/schema.py",
    "app/core/db.py",

    # AI
    "app/ai/llm_engine.py",
    "app/ai/prompt_templates.py",

    # Analytics
    "app/analytics/charts.py",

    # Enrichment
    "app/enrichment/weather.py",
    "app/enrichment/calendar.py",
    "app/enrichment/build_features.py",

    # Scripts
    "scripts/seed_db.py",

    # Root
    "requirements.txt",
    "README.md",
    ".env",
]

print("\n🔍 AI BI Copilot Project Audit\n")

missing = []

for item in EXPECTED_FILES:
    if os.path.exists(item):
        print(f"✅ {item}")
    else:
        print(f"❌ {item}")
        missing.append(item)

print("\n" + "=" * 50)

if not missing:
    print("🎉 ALL REQUIRED FILES EXIST")
else:
    print(f"⚠️ Missing {len(missing)} file(s):\n")

    for item in missing:
        print(f"   - {item}")

print("\nAudit Complete.")