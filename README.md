# Django Blog API

Welcome to the Django Blog API project! This project provides a backend API for a blogging platform developed using Django Rest Framework (DRF). It is designed to store and serve blog posts and related data.

## Table of Contents

-   [Project Overview](#project-overview)
-   [Features](#features)
-   [Getting Started](#getting-started)
-   [API Endpoints](#api-endpoints)
-   [License](#license)

## Project Overview

This Django Blog API project serves as the backend for a blog platform. It includes user authentication, blog post creation, retrieval, updating, and deletion. It's built using Django and Django Rest Framework for building robust RESTful APIs.

## Features

-   **User Authentication**: Users can register, log in, and log out.
-   **Blog Posts**: Create, read, update, and delete blog posts.
-   **Permissions**: User-specific permissions for creating, editing, and deleting posts.
-   **Database**: PostgreSQL is used as the database for data storage.

## Getting Started

To get started with this project on your local machine, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/zzedddd/drf-blog-api.git
    cd drf-blog-api
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

The API endpoints provided by this project include:

### Retrieve Blog Posts

-   **Endpoint**: `GET /api/blog/`
-   **Description**: Retrieve a list of all blog posts (randomised).
-   **Authentication**: Not required.

-   **Endpoint**: `GET /api/blog/home/`
-   **Description**: Retrieve a list of all blog posts, created by the authenticated user.
-   **Authentication**: Required (user must be logged in).

-   **Endpoint**: `GET /api/<slug:pk>/`
-   **Description**: Retrieve a specific blog post. Pk is the primary key of the post which is a UUID.
-   **Authentication**: Required (user must be logged in).

### Create, Update, and Delete Blog Posts

-   **Endpoint**: `POST /api/blog/create/`
-   **Description**: Create a new blog post.
-   **Authentication**: Required (user must be logged in).

-   **Endpoint**: `PUT api/blog/update/`
-   **Description**: Update a specific blog post.
-   **Authentication**: Required (user must be the author of the post).

-   **Endpoint**: `DELETE api/blog/delete/`
-   **Description**: Delete a specific blog post.
-   **Authentication**: Required (user must be the author of the post).

### User Authentication

-   **Endpoint**: `POST /api/accounts/register`
-   **Description**: Register a new user account.
-   **Authentication**: Not required.

-   **Endpoint**: `POST /api/accounts/login`
-   **Description**: Log in as a registered user.
-   **Authentication**: Not required.

-   **Endpoint**: `POST /api/accounts/logout`
-   **Description**: Log out the authenticated user.
-   **Authentication**: Required (user must be logged in).

-   **Endpoint**: `GET /api/accounts/home`
-   **Description**: Retrieve information about the authenticated user.
-   **Authentication**: Required (user must be logged in).

## License

This project is licensed under the [MIT License](LICENSE).
