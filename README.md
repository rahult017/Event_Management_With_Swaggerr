# Multi-User Event Management System API

## Overview
The Multi-User Event Management System API is designed to facilitate the creation, management, and participation in events for multiple users with distinct roles: admin, event organizer, and attendee. This system prioritizes security, scalability, and performance.

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

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rahult017/Event_Management_With_Swaggerr.git
   cd Event_Management_With_Swaggerr
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install poetry
   poetry install
   ```

4. **Configure Environment Variables**:
    - Please check .env.sample for more details.
   - Create a `.env` file in the project root with the following:
     ```env
     SECRET_KEY=your_jwt_secret_key
     DATABASE_URL=your_database_url
     ```

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Application**:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Authentication
- `POST /accounts/register` - Register a new user.
- `POST /accounts/login` - Authenticate and retrieve a token.

### User Management
- `GET /users` - List all users (Admin only).
- `POST /users` - Create a new user (Admin only).
- `PUT /users/{id}` - Update a user (Admin only).
- `DELETE /users/{id}` - Delete a user (Admin only).

### Event Management
- `GET /events` - List all events with filters.
- `POST /events` - Create a new event (Event Organizer only).
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
├── requirements.txt
├── manage.py
├── .env
└── README.md
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
pytest
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
