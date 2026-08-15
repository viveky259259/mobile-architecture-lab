import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRINT_PAGES = ROOT / "src" / "print" / "pages"
PRINT_PDFS = ROOT / "src" / "print" / "pdf"
SITE_PAGES = ROOT / "src" / "site" / "pages"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def generate_deck_dark():
    print("Generating sponsor-deck.pdf (dark)...")
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={PRINT_PDFS / 'sponsor-deck.pdf'}",
        str(SITE_PAGES / "sponsor-deck.html")
    ]
    subprocess.run(cmd, check=True)
    print("✓ sponsor-deck.pdf generated successfully.")


def generate_deck_light():
    print("Generating sponsor-deck-light.pdf (light)...")
    html_path = SITE_PAGES / "sponsor-deck.html"
    temp_html_path = PRINT_PAGES / "sponsor-deck-light.html"

    with html_path.open("r", encoding="utf-8") as f:
        content = f.read()

    # Replace color variables for light mode
    replacements = {
        "--bg:#070A12;": "--bg:#ffffff;",
        "--ink:#F3F7FF;": "--ink:#070A12;",
        "--muted:#A8B4CC;": "--muted:#4b5563;",
        "--faint:#6A7790;": "--faint:#9ca3af;",
        "rgba(255,255,255,.09)": "rgba(0,0,0,.09)",
        "rgba(255,255,255,.14)": "rgba(0,0,0,.14)",
        "rgba(255,255,255,.035)": "rgba(0,0,0,.035)",
        "rgba(255,255,255,.06)": "rgba(0,0,0,.06)"
    }

    for dark, light in replacements.items():
        content = content.replace(dark, light)

    with temp_html_path.open("w", encoding="utf-8") as f:
        f.write(content)

    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={PRINT_PDFS / 'sponsor-deck-light.pdf'}",
        str(temp_html_path)
    ]
    try:
        subprocess.run(cmd, check=True)
        print("✓ sponsor-deck-light.pdf generated successfully.")
    finally:
        if temp_html_path.exists():
            temp_html_path.unlink()


if __name__ == "__main__":
    generate_deck_dark()
    generate_deck_light()
    print("Sponsorship deck PDFs successfully updated!")
