# Magento Login Automation

This project provides a Behavior-Driven Development (BDD) test suite for automating the login flow on the Magento Software Testing Board demo site. It uses **Behave** and **Selenium** to execute end-to-end scenarios and generates an Excel report of test results.

---

## 📦 Project Structure

- **features/**: contains your Gherkin feature files, step definitions, and page objects.  
- **requirements.txt**: Python dependencies.  
- **README.md**: this file.

---

## 🚀 Prerequisites

- Python 3.7+  
- Google Chrome installed 

---

## ⚙️ Setup

1. **Clone or copy** this repository.  
2. **Create and activate** a virtual environment:

   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # Windows CMD
   venv\Scripts\activate.bat
3. **Install dependencies**.  
pip install -r requirements.txt

3. **Execute the BDD suite with Behave**.  

behave
