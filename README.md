# E-Commerce Website

An e-commerce web application built primarily with **Django**. The project provides the backend, database management, user functionality, product management, shopping cart, and payment-related functionality, with **Bootstrap** used for responsive frontend styling.

## 🚀 Features

* User registration and authentication
* User account management
* Product management
* Product browsing
* Shopping cart functionality
* Payment processing
* Media/image handling for products
* Responsive UI using Bootstrap
* SQLite database for development
* Environment variables for configuration

## 🛠️ Technologies Used

### Backend

* **Python**
* **Django**
* **SQLite**

### Frontend

* **HTML**
* **CSS**
* **Bootstrap**
* **Django Templates**

### Other Tools

* Git & GitHub
* `.env` environment variables
* Draw.io for database/ER diagram

## 📁 Project Structure

```text
E-COMMERCE_WEBSITE/
│
├── cart/                  # Shopping cart functionality
├── ecommerce_main/        # Main Django project configuration
├── payments/              # Payment-related functionality
├── products/              # Product management and product-related logic
├── resource/              # Project resources
├── static/                # Static CSS, JavaScript, and other assets
├── templates/             # HTML templates
├── user/                  # User authentication and account functionality
├── media/                 # Uploaded media/product images
│
├── .env                   # Environment variables
├── .gitignore             # Git ignored files
├── db.sqlite3             # SQLite development database
├── manage.py               # Django management utility
├── ER_diagram.drawio      # Database ER diagram
├── notes.md               # Development notes
└── README.md              # Project documentation
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <https://github.com/adan-shahid/ecommerce_website>
cd ecommerce_website
```

### 2. Create a virtual environment

```bash
python -m venv ecommerce_env
```

Activate the virtual environment.

**Windows:**

```bash
ecommerce_env\Scripts\activate
```

**Linux/macOS:**

```bash
source ecommerce_env/bin/activate
```

### 3. Install dependencies

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install Django manually:

```bash
pip install django
```

## 🔐 Environment Variables

Create a `.env` file in the root directory and add the required environment variables.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

If your payment system or other services require additional credentials, add them to the `.env` file as well.

> Never commit your `.env` file or secret credentials to GitHub.

## 🗄️ Database Setup

Run Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

## ▶️ Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/index/
```

Open the address in your browser to access the application.

## 🖥️ Admin Panel

Django's built-in admin panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials created during setup.

## 💳 Payments

The project contains a dedicated `payments` Django app for handling payment-related functionality.

Payment configuration may require credentials or API keys stored in environment variables. Make sure these values are configured before testing payment functionality.

## 🎨 Frontend

The frontend is implemented using **Django Templates**, HTML, CSS, and **Bootstrap**.

Bootstrap is primarily used to provide:

* Responsive layouts
* Navigation components
* Forms
* Buttons
* Cards
* Product layouts
* Mobile-friendly styling

The application therefore does not rely on a separate frontend framework such as React or Vue.

## 🛒 Main Django Apps

### `products`

Responsible for product-related functionality such as storing and displaying product information.

### `cart`

Handles shopping-cart functionality and manages products selected by the user.

### `user`

Handles user-related functionality such as authentication and account management.

### `payments`

Contains the payment-related logic of the application.

### `ecommerce_main`

Contains the main Django project configuration, including settings, URL configuration, and other project-level configuration.


## 🔒 Security

The project uses Django's built-in security mechanisms and environment variables for sensitive configuration.

Important practices include:

* Keeping `SECRET_KEY` outside the source code
* Keeping payment credentials in environment variables
* Excluding sensitive files using `.gitignore`
* Using Django's authentication system
* Using Django's built-in CSRF protection

## 🔮 Future Improvements

Possible future improvements include:

* Product search and filtering
* Product reviews and ratings
* Wishlist functionality
* Order history and tracking
* Advanced payment integration
* Email notifications
* PostgreSQL for production
* REST API using Django REST Framework
* Automated testing
* Deployment using a cloud platform
* Improved frontend design

## 👨‍💻 Author

**Adan Shahid**

This project was developed as a practical full-stack web development project using Django and Bootstrap.
