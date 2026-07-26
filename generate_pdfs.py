import os
import subprocess

def generate_invoice():
    print("Generating invoice-measure-inc.pdf...")
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        "--print-to-pdf=/Users/vivekyadav/Documents/events/mal/invoice-measure-inc.pdf",
        "/Users/vivekyadav/Documents/events/mal/invoice-measure-inc.html"
    ]
    subprocess.run(cmd, check=True)
    print("✓ invoice-measure-inc.pdf generated successfully.")

def generate_deck_dark():
    print("Generating sponsor-deck.pdf (dark)...")
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        "--print-to-pdf=/Users/vivekyadav/Documents/events/mal/sponsor-deck.pdf",
        "/Users/vivekyadav/Documents/events/mal/sponsor-deck.html"
    ]
    subprocess.run(cmd, check=True)
    print("✓ sponsor-deck.pdf generated successfully.")

def generate_deck_light():
    print("Generating sponsor-deck-light.pdf (light)...")
    html_path = "/Users/vivekyadav/Documents/events/mal/sponsor-deck.html"
    temp_html_path = "/Users/vivekyadav/Documents/events/mal/sponsor-deck-light.html"
    
    with open(html_path, "r", encoding="utf-8") as f:
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
        
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        "--print-to-pdf=/Users/vivekyadav/Documents/events/mal/sponsor-deck-light.pdf",
        temp_html_path
    ]
    try:
        subprocess.run(cmd, check=True)
        print("✓ sponsor-deck-light.pdf generated successfully.")
    finally:
        if os.path.exists(temp_html_path):
            os.remove(temp_html_path)

if __name__ == "__main__":
    generate_invoice()
    generate_deck_dark()
    generate_deck_light()
    print("All PDFs successfully updated!")
