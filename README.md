# Todo Application

This is a simple Todo application built with Django. It allows users to create, update, and delete tasks.

## Features

- Create new tasks
- Update existing tasks
- Delete tasks

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Git**: Version control system to clone the repository.
- **Python**: Make sure you have Python 3.6 or higher installed.
- **pip**: Python package installer.
- **Django**: Web application framework.

## Installation

Follow these steps to get the application running on your local machine.

### Clone the Repository

1. Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux).
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

    ```bash
    git clone https://github.com/atrebyy/Todo.git
    ```

4. Navigate into the project directory:

    ```bash
    cd Todo
    ```

### Set Up a Virtual Environment

It's recommended to use a virtual environment to manage your dependencies. Follow these steps:

1. Create a virtual environment:

    ```bash
    python -m venv env
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source env/bin/activate
        ```

### Apply Database Migrations

1. Run the following command to apply the database migrations:

    ```bash
    python manage.py migrate
    ```

### Run the Development Server

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to:

    ```
    http://127.0.0.1:[port]
    ```

You should see the Todo application running.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
