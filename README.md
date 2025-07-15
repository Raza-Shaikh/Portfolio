# Portfolio Website - Mohd Raza Amin Shaikh

A professional, responsive portfolio website built with Django showcasing my skills, projects, and experience as a Python/Django Developer.

## Features

- **Responsive Design**: Professional, mobile-first design that works on all devices
- **Modern UI**: Clean, professional interface with smooth animations and hover effects
- **Skills Showcase**: Interactive skills section with proficiency levels and categories
- **Project Portfolio**: Detailed project cards with technology tags and links
- **Contact Form**: Functional contact form with email notifications
- **Admin Panel**: Easy content management through Django admin
- **SEO Friendly**: Optimized for search engines

## Tech Stack

- **Backend**: Django 4.2.23, Python 3.9
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)

## Featured Projects

### 1. Plagiarism Checker
- **Tech Stack**: Python, Flask, Scikit-learn, HTML/CSS
- **Features**: Multi-format file support (.txt, .docx, .pdf), TF-IDF + Cosine Similarity, NLP processing
- **GitHub**: https://github.com/Raza-Shaikh/Plagiarism-Checker

### 2. E-commerce Store
- **Tech Stack**: Python, Django, HTML/CSS, JavaScript, Bootstrap
- **Features**: User authentication, product catalog, shopping cart, order management
- **GitHub**: https://github.com/Raza-Shaikh/e-commerce-store

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Raza-Shaikh/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv portfolio_env
   portfolio_env\Scripts\activate  # Windows
   # or
   source portfolio_env/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Portfolio: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
portfolio/
├── portfolio_site/          # Main project settings
├── portfolio/               # Portfolio app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Django forms
│   ├── admin.py            # Admin configuration
│   └── urls.py             # URL patterns
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── media/                  # User uploaded files
└── requirements.txt        # Python dependencies
```

## Customization

### Adding Content
1. Access the admin panel at `/admin/`
2. Add your skills, projects, experience, and education
3. Update contact information in templates

### Styling
- Modify `static/css/style.css` for custom styling
- Update color scheme in CSS variables
- Customize animations and transitions

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
