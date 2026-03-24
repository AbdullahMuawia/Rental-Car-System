# Rental Car Backend System

## Overview

This project is a backend system for managing a car rental service, built using FastAPI. It supports user authentication, vehicle management, and booking operations with real-world constraints such as time-based availability and dynamic pricing.

---

## Features

* JWT-based authentication (register and login)
* Vehicle management
* Booking system with:

  * Conflict detection to prevent overlapping bookings
  * Dynamic price calculation based on booking duration
  * Booking cancellation
* Availability system:

  * Check availability for a specific vehicle and date range
  * Retrieve all available vehicles within a given date range

---

## Key Concepts Implemented

* RESTful API design
* Dependency injection using FastAPI
* JWT authentication and authorization
* Time-based availability logic using date range conflict detection
* Relational database design with PostgreSQL
* ORM usage with SQLAlchemy
* Data validation using Pydantic

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn

---

## How to Run

### 1. Clone the repository

git clone https://github.com/AbdullahMuawia/Rental-Car-System.git
cd Rental-Car-System

### 2. Create a virtual environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the application

uvicorn app.main:app --reload

---

## API Endpoints

### Authentication

* POST /auth/register
* POST /auth/login

### Vehicles

* GET /vehicles
* GET /vehicles/available
* GET /vehicles/{id}/availability

### Bookings

* POST /bookings
* GET /bookings/me
* DELETE /bookings/{id}

---

## API Documentation

Interactive API documentation is available at:
http://127.0.0.1:8000/docs

---

## Future Improvements

* Pagination for vehicle listings
* Role-based access control (admin vs user)
* Query optimization to avoid N+1 problems
* Payment integration
* Docker-based deployment

---

## Author

Abdullah Muawia
