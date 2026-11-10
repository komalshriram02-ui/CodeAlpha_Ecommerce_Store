# CodeAlpha E-commerce Store

A full stack e-commerce web application built with **Django** and **PostgreSQL** as part of the CodeAlpha Full Stack Development internship (Task 1).

## Features

- User registration, login and logout
- Product listing with images, search and category filter
- Product details page with stock status
- User-wise shopping cart (add, remove, increase/decrease quantity)
- Checkout with delivery address and Cash on Delivery payment
- Order processing: stock reduces on order, order history per user
- Order cancellation (stock is restored)
- Admin panel to manage products, categories and order status


## Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Django Templates


## Setup Instructions

1. Clone the repository

   ```
   git clone https://github.com/komalshriram02-ui/CodeAlpha_EcommerceStore.git
   cd CodeAlpha_EcommerceStore
   ```

2. Create and activate a virtual environment

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies

   ```
   pip install django psycopg2-binary pillow
   ```

4. Create a PostgreSQL database named `ecommerce_db` and update the database settings in `config/settings.py`

5. Run migrations

   ```
   python manage.py migrate
   ```

6. Create an admin user

   ```
   python manage.py createsuperuser
   ```

7. Start the server

   ```
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/ in your browser.

## Author

Komal Shriram