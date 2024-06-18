# Django Application Setup

This guide will help you set up and run the Django application from the repository on your local machine.

## Prerequisites

- **Git**: Version control system to clone the repository.
- **Python**: Programming language required to run Django.
- **pip**: Package installer for Python.
- **Django**: Python web framework used by the application.

## Installation Steps

### Windows

1. Open PowerShell as Administrator.
2. Copy and paste the following script into PowerShell and press Enter:

    ```powershell
    # Check if Git is installed, if not, install it
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        Write-Host "Git is not installed. Installing Git..."
        winget install --id Git.Git -e --source winget
    }

    # Clone the repo if it doesn't exist
    if (-not (Test-Path -Path "./your-repo-name")) {
        Write-Host "Cloning repository..."
        git clone https://github.com/your-username/your-repo-name.git
    }

    # Navigate into the repo directory
    Set-Location ./your-repo-name

    # Check if Python is installed, if not, install it
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Write-Host "Python is not installed. Installing Python..."
        winget install --id Python.Python.3 -e --source winget
    }

    # Check if pip is installed, if not, install it
    if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
        Write-Host "pip is not installed. Installing pip..."
        python -m ensurepip --upgrade
    }

    # Check if Django is installed, if not, install it
    if (-not (python -c "import django" 2>$null)) {
        Write-Host "Django is not installed. Installing Django..."
        pip install django
    }

    # Run database migrations
    Write-Host "Running database migrations..."
    python manage.py migrate

    # Start the Django development server
    Write-Host "Starting the Django development server..."
    Start-Process "python" "manage.py runserver"

    # Open the web browser to the server address
    Start-Process "http://127.0.0.1:8000"
    ```

### macOS/Linux

1. Open Terminal.
2. Copy and paste the following script into the terminal and press Enter:

    ```bash
    #!/bin/bash

    # Check if Git is installed, if not, install it
    if ! command -v git &> /dev/null
    then
        echo "Git is not installed. Installing Git..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install git
        else
            sudo apt-get update
            sudo apt-get install git -y
        fi
    fi

    # Clone the repo if it doesn't exist
    if [ ! -d "./your-repo-name" ]; then
        echo "Cloning repository..."
        git clone https://github.com/your-username/your-repo-name.git
    fi

    # Navigate into the repo directory
    cd your-repo-name

    # Check if Python is installed, if not, install it
    if ! command -v python3 &> /dev/null
    then
        echo "Python is not installed. Installing Python..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install python
        else
            sudo apt-get update
            sudo apt-get install python3 python3-venv python3-pip -y
        fi
    fi

    # Check if pip is installed, if not, install it
    if ! command -v pip3 &> /dev/null
    then
        echo "pip is not installed. Installing pip..."
        python3 -m ensurepip --upgrade
    fi

    # Check if Django is installed, if not, install it
    if ! python3 -c "import django" &> /dev/null
    then
        echo "Django is not installed. Installing Django..."
        pip3 install django
    fi

    # Run database migrations
    echo "Running database migrations..."
    python3 manage.py migrate

    # Start the Django development server
    echo "Starting the Django development server..."
    python3 manage.py runserver &

    # Open the web browser to the server address
    sleep 5
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open "http://127.0.0.1:8000"
    else
        xdg-open "http://127.0.0.1:8000"
    fi
    ```

### Running the Application

After following the installation steps, your Django application should be running on your local machine. Open your web browser and go to `http://127.0.0.1:8000` to view the application.

If you encounter any issues, please check the console output for error messages and follow the instructions to resolve them.
