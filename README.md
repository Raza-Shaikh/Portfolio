# 🚀 Portfolio Website - Mohd Raza Amin Shaikh

A professional, responsive portfolio website built with Django showcasing my skills, projects, and experience as a **Python/Django Developer**.

![Portfolio Preview](https://img.shields.io/badge/Django-4.2.23-green) ![Python](https://img.shields.io/badge/Python-3.9+-blue) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 📱 **Responsive Design**: Professional, mobile-first design that works on all devices
- 🎨 **Modern UI**: Clean, professional dark theme with smooth animations and hover effects
- 🛠️ **Skills Showcase**: Interactive skills section with proficiency levels and categories
- 💼 **Project Portfolio**: Detailed project cards with technology tags and GitHub/live links
- 📧 **Contact Form**: Fully functional contact form with email notifications via Gmail SMTP
- 🔧 **Admin Panel**: Easy content management through Django admin interface
- 📄 **Resume Download**: Direct PDF resume download functionality
- 🔍 **SEO Friendly**: Optimized for search engines with proper meta tags

## 🛠️ Tech Stack

- **Backend**: Django 4.2.23, Python 3.9+
- **Frontend**: HTML5, CSS3, JavaScript ES6, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Email**: Gmail SMTP integration
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)
- **Deployment**: WhiteNoise for static files, Gunicorn for WSGI

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Raza-Shaikh/Portfolio.git
   cd Portfolio
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv portfolio_env
   portfolio_env\Scripts\activate

   # Linux/Mac
   python3 -m venv portfolio_env
   source portfolio_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create admin user (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - 🌐 **Portfolio**: http://127.0.0.1:8000/
   - ⚙️ **Admin Panel**: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
Portfolio/
├── 📁 portfolio_site/          # Main Django project settings
│   ├── settings.py            # Configuration & environment variables
│   ├── urls.py               # Main URL routing
│   └── wsgi.py               # WSGI application
├── 📁 portfolio/              # Main portfolio app
│   ├── models.py             # Database models (Project, Skill, Contact, etc.)
│   ├── views.py              # View functions and class-based views
│   ├── forms.py              # Django forms for contact
│   ├── admin.py              # Admin panel configuration
│   └── urls.py               # App-specific URL patterns
├── 📁 templates/              # HTML templates
│   ├── base.html             # Base template with navigation
│   └── portfolio/            # App-specific templates
├── 📁 static/                 # Static files
│   ├── css/style.css         # Custom CSS styles
│   ├── js/main.js            # JavaScript functionality
│   ├── images/               # Images and icons
│   └── resume/               # Resume PDF files
├── 📁 media/                  # User uploaded files (project images)
├── 📄 requirements.txt        # Python dependencies
├── 📄 manage.py              # Django management script
└── 📄 README.md              # Project documentation
```

## ⚙️ Configuration & Customization

### 📝 Adding Your Content
1. **Access the admin panel**: Navigate to `/admin/` and login
2. **Add Skills**: Create your technical skills with proficiency levels
3. **Add Projects**: Upload your portfolio projects with descriptions and links
4. **Add Experience**: Include your work experience and education
5. **Update Contact Info**: Modify templates with your personal information

### 🎨 Styling Customization
- **Colors**: Update CSS variables in `static/css/style.css`
- **Fonts**: Modify Google Fonts imports in `base.html`
- **Layout**: Customize Bootstrap classes and custom CSS
- **Animations**: Adjust CSS transitions and JavaScript interactions

### Email Configuration
Update email settings in `settings.py` for production:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## Deployment

The application is ready for deployment on platforms like:
- Heroku
- DigitalOcean
- AWS
- Vercel

Remember to:
- Set `DEBUG = False` in production
- Configure proper database settings
- Set up static file serving
- Configure email settings

## Contact

- **Email**: raza.shaikh.work@gmail.com
- **GitHub**: https://github.com/Raza-Shaikh
- **LinkedIn**: https://www.linkedin.com/in/raza-shaikh-962b48279/

## License

This project is open source and available under the [MIT License](LICENSE).
