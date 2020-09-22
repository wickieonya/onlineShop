# Online Shop Project
A fully featured online shop.
The online shop will enable clients to browse products, add them to the cart, apply discount codes, go through the checkout process, pay with credit card, and obtain an invoice. It will also include a recommendation engine to recommend products to customers, and we will use internationalization to offer the site in multiple languages.

## Building the online shop 
- Create a product catalog
    - create product catalog models
    - register models to the admin site
    - build views
    - create templates
- Build a shopping cart using Django sessions
    - session settings
    - session expiration
    - store cart in sessions
    - create shopping cart views
        - add items to cart
        - template to display cart
        - add products to the cart
        - update product quantities in the cart
- Create custom context processors
    - context processors
    - setting the cart into the request context
- Manage customer orders
    - create order models
    - include order models in admin site
    - create customer orders
- Launch async tasks with Celery
    - Configure Celery with RabbitMQ as our message broker
    - Send asynchronous notifications to customers using Celery
    - Monitor Celery using Flower
        - install Celery
        - install RabbitMQ
        - add Celery to django
        - add async tasks to app
        - monitoring Celery
        
### Managing payments and orders
- Integrate payments with Braintree gateway
    - create Braintree sandbox account
    - install Braintree python module
    - integrate gateway
        - integrate Braintree using hosted fields
    - testing payments
    - going live
- Export orders to csv files
    - add custom actions to the admin site
- Create custom views for the administration site
    - extend admin site with custom views
- Generate PDF invoices dynamically
    - install WeasyPrint
    - generate a pdf template
    - render pdf files
    - send pdf files by email
    
