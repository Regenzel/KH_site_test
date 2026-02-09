# Kingdom Hearts Wiki - Flask Web Application

An interactive web application built with **Flask** and **HTML/CSS** that allows you to explore information about the Kingdom Hearts saga, access a game catalog, and discover upcoming releases.

## 🎮 Features

- **Homepage** with general information about the saga
- **Game catalog** with images and expandable details
- **Detailed information** about the saga and its narrative
- **Discover upcoming** Kingdom Hearts releases
- **Responsive design** that adapts to different screen sizes
- **Intuitive navigation** between sections

## 📋 Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package manager)
- A modern web browser

## 🚀 Installation

### 1. Clone or download the repository

```bash
git clone <repository-url>
cd Reto6_Flask_HTML
```

### 2. Create a virtual environment (recommended)

**On Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Usage

### Run the application

**On Windows:**
```bash
python main.py
```

**On macOS/Linux:**
```bash
python3 main.py
```

The application will be available at `http://localhost:5000`

### Available routes

- `/` - Homepage
- `/all_games` - Complete game catalog
- `/saga_info` - Detailed saga information
- `/whats_next` - Upcoming releases

## 📦 Main dependencies

- **Flask 3.1.2** - Minimal web framework for Python
- **Jinja2** - HTML template engine
- **Werkzeug** - WSGI utilities

See `requirements.txt` for the complete version of all dependencies.

## 📝 License

This project is open source. Feel free to use, modify, and distribute it.

## 👤 Author

Developed as an educational project on Flask and web development.
