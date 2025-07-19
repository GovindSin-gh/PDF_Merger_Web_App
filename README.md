# 📎 PDF Merger Web App

A lightweight, fully functional PDF Merger web application built using **Python**, **Streamlit**, and **pypdf**.

This app allows users to upload multiple PDFs, merge them in-browser, and download the final combined file — all in a clean, minimal interface.

---

## 🚀 Live Demo

👉 [Try it here on Streamlit Cloud](https://pdfmergerwebapp.streamlit.app/)

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** – for building the web UI
- **pypdf** – for PDF file merging
- **io.BytesIO** – for in-memory file operations
- **Streamlit Cloud** – for deployment
- **GitHub** – version control and project management

---

## 📦 Features

- Upload multiple PDFs
- Automatically merge them in the order uploaded
- Download the final merged PDF
- Clean UI with no Streamlit branding
- Fully browser-based (no files stored on server)

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YourUsername/pdf-merger.git
cd pdf-merger

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
