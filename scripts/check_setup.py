import os

EXPECTED_STRUCTURE = [
    "app",
    "app/api",
    "app/core",
    "app/ai",
    "app/analytics",
    "app/enrichment",
    "data",
    "scripts",
    "tests",
    "requirements.txt",
    "README.md",
    ".env"
]

def check_structure():
    print("\n🔍 Checking project structure...\n")

    missing = []

    for path in EXPECTED_STRUCTURE:
        if not os.path.exists(path):
            missing.append(path)
            print(f"❌ Missing: {path}")
        else:
            print(f"✅ Found: {path}")

    print("\n------------------------")

    if not missing:
        print("🎉 PROJECT STRUCTURE IS PERFECTLY ALIGNED")
    else:
        print("⚠️ Some items are missing. Fix before continuing.")
        print("\nMissing items:")
        for m in missing:
            print(f" - {m}")

if __name__ == "__main__":
    check_structure()