Panacea
Purpose
Panacea is a full-stack e-commerce web application designed to allow users to purchase medication and skincare products online. The platform enables user account management, product browsing, cart handling, and checkout functionalities. The system is built using React with Tailwind CSS for the frontend and Python for the backend, and integrates a database-backed API for item management.

User System
1. User Registration
Create: Users can register by providing their personal details.

Fields: username, email, password, date_of_birth, address

Constraints: Email must be unique. Password must meet security criteria (e.g., min length, complexity).

2. Login / Authentication
Read: Authenticates users and returns session or JWT token.

Input: email, password

Output: Auth token and user data

Security: Tokens should expire and support refresh functionality.

3. Logout
Delete: Invalidates the current session or token.

4. Delete Account
Delete: Allows the user to permanently delete their account.

Effect: Removes or anonymizes associated data such as cart and order history.

Cart System
1. Add Item to Cart
Create: Adds a selected product to the user’s cart.

Input: user_id, item_id, quantity

Constraints: Item must be in stock.

2. View Cart
Read: Retrieves current cart items.

Output: List of items, quantities, total price (with discounts applied).

3. Checkout
Delete (Cart contents): Completes the transaction and clears the cart.

Effect: Deducts stock from inventory and creates an order record.

Item System (Products)
1. Add New Item (Admin Function)
Create: Adds a new product to the database.

Fields:

name: string

description: string (e.g., dosage info, usage instructions, warnings)

price: float

discount: float (percentage or fixed)

stock: integer

category: enum (medication, skincare)

requires_prescription: boolean

ingredients: string (optional for skincare)

instructions: string (optional)

2. View Items
Read: Publicly accessible endpoint to fetch product listings.

Supports: Filtering by category, price range, or prescription requirement.
