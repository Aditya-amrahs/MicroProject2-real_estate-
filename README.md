# 🏠 Real Estate API

A modern, fast, and scalable REST API for managing real estate properties, built with **FastAPI** and **SQLAlchemy**. This microproject provides endpoints for property listings, user authentication, favorites, and inquiries.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135.2-green.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.48-red.svg)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Testing](#-testing)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Property Management**: Create, read, update, and delete real estate properties
- **User Authentication**: Simple registration and login system
- **Favorites System**: Users can add/remove properties to/from favorites
- **Inquiry System**: Send inquiries about properties
- **Database Integration**: Uses SQLAlchemy with SQLite for data persistence
- **Auto-generated API Docs**: Interactive Swagger UI at `/docs`
- **Docker Support**: Containerized deployment
- **Comprehensive Testing**: Pytest suite for reliability

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone [<repository-url>](https://github.com/Aditya-amrahs/MicroProject2-real_estate-.git)
   cd MicroProject2-real_estate
   ```

2. **Run with Docker** (Recommended)
   ```bash
   docker build -t real-estate-api .
   docker run -p 8000:8000 real-estate-api
   ```

3. **Visit the API**
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

## 📦 Installation

### Prerequisites

- Python 3.11+
- pip
- (Optional) Docker

### Local Development

1. **Create a virtual environment**
   ```bash
   python -3.11 -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python -m app.main
   ```

The API will be available at `http://127.0.0.1:8000`.

### Docker Deployment

```bash
# Build the image
docker build -t real-estate-api .

# Run the container
docker run -p 8000:8000 real-estate-api
```

## 🛠 Usage

### Starting the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### API Documentation

Once running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Example API Calls

#### Register a User
```bash
curl -X POST "http://localhost:8000/register" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com", "password": "password123"}'
```

#### Login
```bash
curl -X POST "http://localhost:8000/login" \
     -H "Content-Type: application/json" \
     -d '{"email": "john@example.com", "password": "password123"}'
```

#### Create a Property
```bash
curl -X POST "http://localhost:8000/properties/" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Beautiful Apartment",
       "description": "A lovely 2-bedroom apartment",
       "price": 250000,
       "location": "Downtown",
       "property_type": "apartment",
       "bedrooms": 2,
       "bathrooms": 1
     }'
```

## 📚 API Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /login` - Login user

### Properties
- `GET /properties/` - List all properties (paginated)
- `GET /properties/{id}` - Get property details
- `POST /properties/` - Create a new property
- `PUT /properties/{id}` - Update a property
- `DELETE /properties/{id}` - Delete a property

### Favorites
- `POST /favorites` - Add property to favorites

### Inquiries
- `POST /inquiries` - Send inquiry about a property

### Root
- `GET /` - Health check endpoint

## 🧪 Testing

Run the test suite using pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_properties.py
```

Test files:
- `test_auth.py` - Authentication tests
- `test_properties.py` - Property CRUD tests
- `test_inquiries.py` - Inquiry tests

## 📁 Project Structure

```
MicroProject2(real_estate)/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   ├── data.py          # Initial data seeding
│   └── routes/
│       ├── auth.py      # Authentication routes
│       ├── properties.py # Property management routes
│       ├── favorites.py  # Favorites routes
│       └── inquiries.py  # Inquiry routes
├── tests/
│   ├── test_auth.py
│   ├── test_properties.py
│   ├── test_inquiries.py
│   └── test_inq/        # Additional inquiry tests
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


Made with ❤️
