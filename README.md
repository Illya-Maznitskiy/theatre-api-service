# Theatre API Service


## Description
This API is designed for a local theater, allowing visitors to make online reservations, choose seats, and manage bookings. It includes endpoints for user registration, login, and access to theater data such as plays, performances, and genres.


## Technologies Used
- Python
- Django ORM
- Django
- DRF
- Docker


## Setup
To install the project locally on your computer, execute the following commands in a terminal:
```bash
git clone https://github.com/Illya-Maznitskiy/theatre-api-service.git
cd theatre-api-service
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py runserver
```


## Docker Setup
To set up and run the project using [Docker](https://www.docker.com/get-started/), follow these steps:

- Use `http://localhost:8001/` URL to visit the service when it starts.

1. **Ensure Docker is Running**:
    ```text
    Make sure Docker Desktop is installed and running on your system.
    ```

2. **Build the Docker Images**:
    ```bash
    docker-compose build
    ```

3. **Start the Services**:
    ```bash
    docker-compose up
    ```

4. **Stop the Services**:
    ```bash
    docker-compose down
    ```


## Docker Configuration
### _Dockerfile_
Configures the Django app environment, installs dependencies, sets the working directory, and manages media file permissions

### _docker-compose.yml_
This file sets up the Docker services, including the Django application and PostgreSQL database:

### _Environment Variables .env_
These variables configure the PostgreSQL database connection.


## API Endpoints

### User API
- **URL:** `/api/user/register/`
- **URL:** `/api/user/login/`
- **URL:** `/api/user/me/`

### Theatre API
- **URL:** `/api/theatre/theatre-halls/`
- **URL:** `/api/theatre/plays/`
- **URL:** `/api/theatre/performances/`
- **URL:** `/api/theatre/actors/`
- **URL:** `/api/theatre/genres/`
- **URL:** `/api/theatre/reservations/`
- **URL:** `/api/theatre/tickets/`


## Commands to test the project:
You can use the following commands to run written tests and check the code style using flake8:
```
python manage.py test
flake8
```


## Screenshots:
_There are examples how to use the project with DRF API interface in browser with a [ModHeader](https://modheader.com/docs/using-modheader/modify-request-headers) extension
 (alternatively, [Postman](https://learning.postman.com/docs/introduction/overview/) or similar services can be used)_

### User registration example:
This screenshot shows the form where new users can create an account.
![User Registration](images/user_register.png)

### User login by page:
Here’s a demonstration of the login page where users receive their tokens.
![User Login Page](images/user_login.png)

### User login by ModHeader:
Use the ModHeader extension to send the token and allow access to other pages.
![User Login by Header](images/using_modheader.png)

### Theatre API Overview:
If you correctly use the authentication token, you'll have access to the Theatre API.
![Theatre API](images/theatre_api.png)

## Database structure:
![Database Structure](images/db_structure.jpg)
