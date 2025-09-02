# Flask Portfolio Website

This is a **portfolio website** built entirely with **Flask** (no React).  
It showcases my profile, projects, and contact details with a clean layout.

---

## 🚀 Features
- Flask backend with multiple routes
- Simple, clean design with `styles.css`
- Resume download option
- Responsive navigation bar
- Sections: Home, About, Projects, Contact

## 🛠️ Tech Stack
- **Flask** – Python web framework
- **HTML + CSS** – Frontend templates
- **Gunicorn** – Production server
- **GitHub + Render/Heroku** – Deployment

---

## 📂 Project Structure
```bash
portfolio_flask/
├── app.py # Flask entrypoint
├── requirements.txt # Dependencies
├── static/ # Static files (CSS, favicon, resume)
│ ├── styles.css
│ ├── favicon.ico
│ └── Thakur_Suryaveer_Resume.pdf
└── templates/ # HTML templates
├── base.html
├── index.html
├── about.html
├── projects.html
└── contact.html
```

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/suryaveer-infobeans/portfolio.git
cd portfolio
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the app
```bash
python app.py
```
```bash
Visit: http://127.0.0.1:5000
```

## 🚀 Deployment

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
gunicorn app:app
```
## 📜 License

This project is open-source under the MIT License.