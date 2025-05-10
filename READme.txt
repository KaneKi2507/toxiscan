ToxiScanWebsite - Toxic Content Detection System
------------------------------------------------

This is a beginner-friendly project that detects toxic or inappropriate content 
in text and images using machine learning models. It has a Python Flask backend 
and a simple HTML frontend admin panel.


If the instructions followed are correctly, the website will run smoothly, as we have checked on other devices as well!

Requirements:
- Python 3.10+
- pip install flask
pip install pytesseract
pip install pillow
pip install numpy
pip install opencv-python

- install the following as well

🔹 Tesseract OCR Engine for Windows
This is the actual software that does the OCR work — pytesseract is just a Python wrapper around it.

🔹 ✅ Steps to Install:
Go to this link (best Windows version with updated language packs):
👉 https://github.com/UB-Mannheim/tesseract/wiki

Download the .exe installer from there.
Example: tesseract-ocr-w64-setup-5.3.1.20230401.exe

Run the installer. During installation:

Remember the path where it's installed, e.g.
C:\Program Files\Tesseract-OCR\tesseract.exe

------------------------------------------------

Steps to Run the Project:

1. Go to the 'ToxiScanWebsite' folder.
2. Open the 'backend' folder.
3. Open the terminal (Ctrl + ` or right-click -> Open in Terminal).
4. Make sure in the terminal, the 'backend' folder is open from the 'ToxiScanWebsite' folder.
5. In terminal, Run the backend by typing: python app.py
6. Wait for "Running on http://127.0.0.1:5000" to confirm it's running.

6. Go back to the 'ToxiScanWebsite' folder.
7. Open the 'frontend' folder.
8. Double-click 'index.html' to open it in your browser.

How to Use:
- Upload text or image files through the admin panel.
- The backend will process them and return results.
- Admin can allow/ban/delete content.

------------------------------------------------

Made by Team: Null Pointers
Parth Sarthi 
Ayush Kumar Thakur
Tejash Poddar
Priyanshi Gupta
Shreya Sharma
