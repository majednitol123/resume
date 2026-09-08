import subprocess
import os
import shutil

PROJECT_DIR = "/Users/majedurrahman/coding/resume"
OUTPUT_PDF = os.path.join(PROJECT_DIR, "Md_Majedur_Rahman_Resume.pdf")
DOWNLOADS_DIR = "/Users/majedurrahman/Downloads"
DOWNLOADS_PDF = os.path.join(DOWNLOADS_DIR, "Md_Majedur_Rahman_Resume.pdf")
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def generate_pdf():
    print("Generating PDF using Google Chrome headless...")
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT_PDF}",
        f"file://{PROJECT_DIR}/index.html"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(OUTPUT_PDF) and os.path.getsize(OUTPUT_PDF) > 0:
        print(f"Success! Generated {OUTPUT_PDF} ({os.path.getsize(OUTPUT_PDF)} bytes)")
        try:
            shutil.copy2(OUTPUT_PDF, DOWNLOADS_PDF)
            print(f"Copied to Mac Downloads folder: {DOWNLOADS_PDF}")
        except Exception as e:
            print(f"Could not copy to Downloads: {e}")
        return True
    else:
        print(f"Failed to generate PDF: {res.stderr}")
        return False

if __name__ == "__main__":
    generate_pdf()
