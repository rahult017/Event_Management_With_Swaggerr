# Multi-User Event Management System API

## Overview
The Multi-User Event Management System API enables secure, scalable, and efficient event management for multiple users with distinct roles: admin, event organizer, and attendee. The system offers user and event management features with role-based access control, ensuring security and performance.

---

## Features

### User Management
- **User Registration and Login**: 
  - Secure authentication using JWT or OAuth2.
- **Admin Features**:
  - Create, delete, and manage users.
- **Event Organizer Features**:
  - Create, update, and delete events.
- **Attendee Features**:
  - View and join events.

### Event Management
- **Event Attributes**:
  - Title, description, location, date, time, and maximum attendees.
- **Event Organizer Abilities**:
  - Create, update, and delete events.
- **User Abilities**:
  - View event details and sign up for events.
- **Admin Abilities**:
  - Oversee, modify, or delete any event.

### API Functionalities
- CRUD operations for users and events.
- Event listing and search with filters (e.g., by date, location, availability).
- Role-based access control for secure endpoints.
- Proper error handling and input validation.

### Security Features
- User authentication via JWT or OAuth2.
- Protection against vulnerabilities (SQL injection, XSS, CSRF, etc.).
- Authorization for role-based endpoint access.
- Rate limiting to prevent API abuse.

### Testing and Documentation
- Comprehensive unit tests for core functionalities.
- API documentation generated using Swagger or Redoc.

---

## Installation

### Prerequisites
- Docker
- Docker Compose
- Poetry

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rahult017/Event_Management_With_Swaggerr.git
   cd Event_Management_With_Swaggerr
   ```

2. **Set Up Docker**:
   Create a `.env` file in the project root with the following configuration:
   ```env
   SECRET_KEY=your_jwt_secret_key
   DATABASE_URL=postgres://username:password@db:5432/db_name
   ```

3. **Set Up Poetry**:
   If Poetry is not already installed, install it by running:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

4. **Install Dependencies Using Poetry**:
   Install project dependencies:
   ```bash
   poetry install
   ```

5. **Build Docker Containers**:
   Use Docker Compose to build and start the containers:
   ```bash
   docker-compose up --build
   ```

6. **Apply Migrations**:
   Access the container and run migrations:
   ```bash
   docker-compose exec web poetry run python manage.py migrate
   ```

7. **Access the Application**:
   Open your browser and navigate to `http://localhost:8000/` to access the API.

---

## API Endpoints

### Authentication
- `POST /accounts/register/` - Register a new user.
- `POST /accounts/login/` - Authenticate and retrieve a token.
- `POST /accounts/logout/` - Logout a user.
- `POST /accounts/renew-token/` - Renew authentication token.
- `POST /accounts/verify-token/` - Verify token validity.

### User Management
- `GET /accounts/users/` - List all users (Admin only).
- `POST /accounts/users/` - Create a new user (Admin only).
- `PUT /accounts/users/{id}` - Update a user (Admin only).
- `DELETE /accounts/users/{id}` - Delete a user (Admin only).

### Event Management
- `GET /events/` - List all events with filters.
- `POST /events/` - Create a new event (Event Organizer only).
- `PUT /events/{id}` - Update an event (Event Organizer or Admin).
- `DELETE /events/{id}` - Delete an event (Event Organizer or Admin).
- `POST /events/{id}/join` - Join an event (Attendee only).

---

## Directory Structure
```
project_root/
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
    └── tests.py
├── events/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── poetry.lock
├── requirements.txt
├── manage.py
├── .env
└── README.md
```

---

## Docker Setup

### Dockerfile
```dockerfile
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set the PATH to include Poetry
ENV PATH="/root/.local/bin:$PATH"

# Copy poetry files and install dependencies
COPY pyproject.toml poetry.lock /app/
RUN poetry install

# Copy the current directory contents into the container
COPY . /app/

# Expose port
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    command: poetry run python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: username
      POSTGRES_PASSWORD: password
      POSTGRES_DB: db_name
    ports:
      - "5432:5432"
```

---

## Database Design

### Tables
1. **Users**:
   - id, username, email, password, role (admin, organizer, attendee).
2. **Events**:
   - id, title, description, location, date, time, max_attendees.
3. **Event-User Relationship**:
   - event_id, user_id (for many-to-many relationship).

---

## Bonus Features
- **Email Notifications**:
  - Notify users via email when they join or create an event.
- **Google Maps Integration**:
  - Use Google Maps API for location selection and display.

---

## Testing
Run the test suite:
```bash
docker-compose exec web poetry run pytest
```

---

## Documentation
- Swagger UI: Available at `/`.
- Redoc: Available at `/redoc/`.

---

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add feature-name'`.
4. Push to branch: `git push origin feature-name`.
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.