# Placibo - Advanced Form Management System

Placibo is a robust, scalable form management platform built with Django and Django REST Framework. It allows users to create dynamic forms, share them with others, and collect submissions with integrated file upload support powered by AWS S3.

## 🚀 Features

- **Dynamic Form Creation**: Build custom forms with flexible JSON-based data structures.
- **User Sharing**: Share forms with specific users for collaborative management or submission.
- **Secure File Submissions**: Integrated support for file uploads directly to AWS S3.
- **Scalable Architecture**: Utilizes Redis for caching/tasks and PostgreSQL for reliable data storage.
- **Docker Ready**: Simplified development environment using Docker Compose.
- **Clean Code**: Maintained with Ruff for high-quality linting and formatting.

## 🛠️ Tech Stack

- **Backend**: [Django 6.0](https://www.djangoproject.com/) & [Django REST Framework](https://www.django-rest-framework.org/)
- **Database**: PostgreSQL (Production), SQLite (Development default)
- **Infrastructure**: Redis, AWS S3
- **Dev Tools**: Docker, Pipenv, Ruff

## 📦 Getting Started

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Pipenv (`pip install pipenv`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/placibo.git
   cd placibo/gforms
   ```

2. **Install dependencies**:
   ```bash
   pipenv install --dev
   ```

3. **Set up environment variables**:
   Create a `.env` file in the `gforms/` directory (refer to `.env.example` if available) and add your configurations:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   AWS_ACCESS_KEY_ID=your-key
   AWS_SECRET_ACCESS_KEY=your-secret
   AWS_STORAGE_BUCKET_NAME=your-bucket
   ```

4. **Start Infrastructure Services**:
   Use Docker to spin up PostgreSQL and Redis:
   ```bash
   docker-compose up -d
   ```

5. **Run Migrations**:
   ```bash
   pipenv run python manage.py migrate
   ```

6. **Start the Development Server**:
   ```bash
   pipenv run python manage.py runserver
   ```

## 🐳 Docker Usage

The project includes a `docker-compose.yml` that sets up:
- **Redis**: Port `6379`
- **PostgreSQL**: Port `5432` (Username: `postgres`, DB: `postgres`)

To stop the services:
```bash
docker-compose down
```

## ☁️ Deployment

The project is configured for deployment on AWS EC2. Ensure your `ALLOWED_HOSTS` in `settings.py` includes your instance IP and that your `.pem` key is securely stored for SSH access.

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
*Built with ❤️ for efficient data collection.*
