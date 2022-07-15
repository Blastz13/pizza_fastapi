# Installation and launch

**Installation**

You can clone this application:

```bash 
git clone https://github.com/Blastz13/pizza_fastapi.git
```

Next, you need to install the necessary libraries:

```bash
poetry install
poetry update
```
You need to set variables in the environment: 

`JWT_SECRET` — Secret JWT key

`JWT_ALGORITHM` — Encryption algorithm method

`PIZZA_USER` — Database username

`PIZZA_PASSWORD` — Database password

`PIZZA_HOST` — Database host

`PIZZA_PORT` — Database port

`PIZZA_NAME` — Database name

**Launch**

Change directory from web app, create and apply migrations:

```bash
cd pizza_fastapi
alembic revision --autogenerate -m 'Initial'
alembic upgrade head
```

Now you can start the server:

```bash
uvicorn main:app --reload
```

### License

Copyright © 2021 [Blastz13](https://github.com/Blastz13/).