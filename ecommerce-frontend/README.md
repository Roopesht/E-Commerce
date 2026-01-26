# E-Commerce Platform

A full-stack e-commerce application built with **FastAPI** backend and **React** frontend.

## Project Overview

This project is a complete e-commerce solution featuring:

- **Backend**: FastAPI with MongoDB database, multiple routers for API endpoints
- **Frontend**: React with component-based architecture
- **Features**: User authentication, product browsing, shopping cart, order management

## Tech Stack

### Backend

- **Framework**: FastAPI
- **Database**: MongoDB
- **Language**: Python
- **Features**: CORS middleware, JWT authentication, RESTful API routing

### Frontend

- **Framework**: React
- **Styling**: CSS
- **Package Manager**: npm

## Project Structure

```
E-Commerce/
├── ecommerce-backend/
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # MongoDB connection configuration
│   ├── models/
│   │   ├── schemas.py       # Pydantic data models
│   │   └── user.py          # User model definitions
│   └── routes/
│       ├── auth.py          # Authentication endpoints
│       ├── products.py      # Product endpoints
│       ├── cart.py          # Shopping cart endpoints
│       └── orders.py        # Order management endpoints
│
└── ecommerce-frontend/
    ├── src/
    │   ├── App.js           # Main React component
    │   ├── components/
    │   │   ├── Login.js     # Login page
    │   │   ├── Register.js  # User registration
    │   │   ├── Products.js  # Product listing
    │   │   ├── ProductDetails.js
    │   │   ├── Cart.js      # Shopping cart
    │   │   └── Orders.js    # Order history
    │   ├── App.css
    │   └── index.js
    └── package.json
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js (v14 or higher)
- MongoDB running locally or connection string configured

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd ecommerce-backend
   ```

2. Install Python dependencies:

   ```bash
   pip install fastapi uvicorn pymongo python-jose passlib python-multipart
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd ecommerce-frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```
   The frontend will open at `http://localhost:3000`

## Available Frontend Scripts

### `npm start`

Runs the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view in your browser.

### `npm test`

Launches the test runner in interactive watch mode.

### `npm run build`

Builds the app for production in the `build` folder.

## API Endpoints

### Authentication Routes (`/auth`)

- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout

### Product Routes

- `GET /products` - Get all products
- `GET /products/{id}` - Get product details

### Cart Routes (`/cart`)

- `GET /cart` - View cart items
- `POST /cart/add` - Add item to cart
- `DELETE /cart/{item_id}` - Remove item from cart

### Order Routes (`/orders`)

- `GET /orders` - Get user orders
- `POST /orders/create` - Create new order

## Features Implemented

- User Authentication & Registration
- Product Catalog Management
- Shopping Cart Functionality
- Order Management
- MongoDB Database Integration
- CORS Support
- RESTful API Design

## Future Enhancements

- Payment gateway integration
- Product search and filtering
- User review and rating system
- Admin dashboard
- Email notifications
- Inventory management

## Troubleshooting

- **MongoDB Connection Error**: Ensure MongoDB is running and connection string is correct
- **CORS Issues**: Backend is configured to accept requests from `http://localhost:3000`
- **Port Already in Use**: Change the port in FastAPI or React configuration if needed

## License

This project is open source and available for learning purposes.
