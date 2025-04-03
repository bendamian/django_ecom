# GeoShop Backend (Django REST API)

This is the backend for **GeoShop**, a full-stack e-commerce web app built using Django and Django REST Framework. It provides APIs for handling products, categories, and cart functionality.

## 📦 Features

- Django 5.x with Django REST Framework
- Custom product models with image and category support
- RESTful API endpoints for frontend consumption
- CORS support for Vue.js frontend
- Media file handling (images)
- Slug-based routing for product detail pages

## 🔧 Setup

1. **Clone the repo**:

   ```bash
   git clone https://github.com/yourusername/geoshop-backend.git
   cd geoshop-backend
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

## 🗂️ Project Structure

- `config/` – Django settings and base project configuration
- `product/` – App containing models, serializers, and API views
- `media/` – Uploaded product images
- `requirements.txt` – Python dependencies

## 🔐 Environment Variables

Make sure to set up your `.env` file (or environment variables) with the following:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`

## 🌐 API Endpoints

- `GET /api/v1/latest-products/` – Latest products
- `GET /api/v1/products/<category_slug>/<product_slug>/` – Product details

## 📷 Media Files

Uploaded images are stored in the `media/` directory and served using Django's development server (in dev mode).

---

© 2025 GeoShop. Built with ❤️ using Django.

---

# GeoShop Frontend (Vue 3 + Vite)

This is the frontend for **GeoShop**, a sleek e-commerce SPA built using Vue.js 3 with Vite. It consumes the Django REST API to display products, categories, and allow cart functionality.

## ⚙️ Features

- Vue 3 + Vite for blazing-fast development
- Vue Router for dynamic routing
- Axios for API requests
- Bulma CSS framework
- Reusable components: ProductCard, ProductImage, etc.
- Fully responsive layout

## 💪 Project Setup

1. **Clone the repo**:

   ```bash
   git clone https://github.com/yourusername/geoshop-frontend.git
   cd geoshop-frontend
   ```

2. **Install dependencies**:

   ```bash
   yarn install
   ```

3. **Run development server**:

   ```bash
   yarn dev
   ```

## 📂 Project Structure

- `src/components/` – Reusable Vue components
- `src/views/` – Route-based views like Home, Product, Cart
- `src/router/` – Vue Router configuration
- `src/assets/` – Images and styles
- `main.js` – Entry point for Vue app

## 🔗 API Configuration

Make sure Axios is configured to point to your Django backend:

```js
axios.defaults.baseURL = 'http://127.0.0.1:8000';
```

You may also want to configure CORS on the Django backend to allow requests from `http://localhost:5173`.

## 📸 Product Images

Product thumbnails and full-size images are handled via the backend. A placeholder is shown if no image is available.

## 🚀 Deployment

To build the app for production:

```bash
yarn build
```

Then serve the `dist/` directory using your preferred hosting solution.

---

© 2025 GeoShop. Built with ⚡ Vue 3 and ❤️.


