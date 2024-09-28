eCommerce Website
This project is a basic eCommerce website built using Python (Flask or Django). The website allows users to browse products, add them to a shopping cart, and proceed to a simple checkout process. It also includes features like user authentication, product management, and order tracking.

Features
1. Web Development (Python Backend)
Framework: Built using either Flask or Django.
Templates: Includes templates for the home page, product listings, shopping cart, and checkout.
Routing: Set up clean URL routes for products, cart, user login, registration, and checkout

2. Product Management
Product Model:
Name: The product's name.
Description: Brief product description.
Price: Product price.
Image: Product image.
Stock: Number of items available in stock.
Features:
List Products: Display a list of all products on the home page. Each listing shows the product name, price, and a "View Details" button.
View Product Details: Click on a product to view detailed information, including the description, price, stock, and a larger image.

3. Shopping Cart
Add to Cart: Users can add products to their shopping cart from the product details page.
View Cart: Display the contents of the shopping cart, showing product names, quantities, and total price.
Update Cart: Users can update the quantity of items in their cart or remove items.

4. User Authentication
User Registration: Allows users to create an account.
User Login/Logout: Users can log in and out of the application.
Authentication: Only logged-in users can proceed to checkout and place orders.
Personalized Greeting: Display a personalized greeting on the home page when the user is logged in.

5. Checkout Process
Shipping Details: Collect shipping information (address, phone number, etc.).
Order Summary: Show a summary of items in the cart, total price, and shipping details.
Place Order: Save the order in the database and reduce stock based on the purchase.

6. Order Management
Order Model:
User: The user who placed the order.
Products: A list of products in the order.
Total Price: The total price of the order.
Shipping Address: The delivery address for the order.
Order Date: The date the order was placed.
My Orders Page: Allow users to view their past orders.

7. Enhancements (Optional)
Product Categories: Implement product categories and allow users to filter products by category.
Search: Add a search bar to search for products by name or description.
Payment Gateway Simulation: Integrate a mock payment system to complete the checkout process.
Getting Started
Prerequisites
Python 3.x
Flask or Django (Choose your preferred framework)
SQLite or any other database
Basic HTML, CSS, and JavaScript knowledge

Prerequisites
Python 3.x
Flask or Django (Choose your preferred framework)
SQLite or any other database
Basic HTML, CSS, and JavaScript knowledge
