# Tree Menu Project

This project implements a flexible, database-driven tree menu system using Django.

## Features

- Tree-like menu structure
- Database-driven menu items
- Expandable/collapsible menu items
- Multiple menus support
- Efficient database queries
- Responsive design using Bootstrap
- Docker support for easy deployment

## Setup

1. Clone the repository:
   `git clone https://github.com/ulugkhujayev/menu_project.git`
   `cd menu_project`

2. Create `.env`:
   `SECRET_KEY =secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=db
DB_PORT=5432
`

3. Build and run the Docker containers:
   `cd docker`
   `docker-compose up --build`

4. Create a superuser:
   `docker-compose exec web python manage.py createsuperuser`

5. Visit `http://localhost:8000/admin/` to add menu items.

6. Visit `http://localhost:8000/` to see the menu in action.

## Running Tests

`docker-compose exec web pytest`
