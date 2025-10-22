# django-test-37

Django REST API Project được tạo tự động bởi **Dev Portal**.

## 📋 Thông tin Project

- **Project Name:** django-test-37
- **App Name:** api
- **Django Version:** 4.2.7
- **DRF Version:** 3.14.0

## 🚀 Models

- **User**: userget/

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/quanmbl4255142/django-test-37.git

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## 🐳 Docker

```bash
# Build image
docker build -t django-test-37 .

# Run container
docker run -p 8000:8000 django-test-37
```

## 🔗 API Endpoints

- GET/POST `/api/userget/` - List/Create User
- GET/PUT/DELETE `/api/userget/<id>/` - Detail/Update/Delete User
- GET `/api/health/` - Health check

## 📝 License

MIT License
