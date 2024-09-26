# django_order_management

## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **PostgreSQL**: An open-source relational database management system that provides robust features and extensibility.
- **Docker & Docker Compose**: Containerization technologies for application deployment and management.

## Model Relationships


### Order
**Fields:**
- `order_number`: Unique order number, using UUID.
- `total_price`: Total price of the order, automatically calculated.
- `created_time`: Order creation time.

**Relationships:**
- Many-to-many relationship with `Product` through `OrderItem`.

### Product
**Fields:**
- `name`: Product name.
- `price`: Product price.
- `stock_quantity`: Stock quantity.
- `created_time`: Product creation time.

**Relationships:**
- Many-to-many relationship with `Order` through `OrderItem`.

### OrderItem
**Fields:**
- `order`: Related order.
- `product`: Related product.
- `quantity`: Purchase quantity.
- `unit_price`: Unit price, default to product price.

**Relationships:**
- Acts as an intermediary connecting `Order` and `Product`.

## API Endpoints
This project provides a primary API endpoint for importing orders. For details, refer to `api/views.py`:

### import_order API
- **Method**: POST
- **URL**: /api/import_order/
- **Function**: Imports order data into the system.
- **Authentication**: Uses `token_required` decorator to ensure the request contains a valid authorization token.
- **Transaction Handling**: Uses `@transaction.atomic` to ensure data consistency.
- **Response**:
  - On success: Returns `message`, `order_id`, and `total_price`.
  - On failure: Returns an error message.

## Token Authentication
To ensure the security of the API, a custom `token_required` decorator is used to validate the authorization token in the request:

