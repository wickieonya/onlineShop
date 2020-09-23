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
        - GTK error that keeps coming up
        - `WHERE libcairo-2.dll` 
        - It should respond with the path\to\recently\installed\gtk\binaries\libcairo-2.dll, for example:
        `C:\Program Files\GTK2-Runtime Win64\bin\libcairo-2.dll`
        - The proper folder name of interes is `C:\Program Files\GTK2-Runtime Win64\bin`
        - Execute the following command to set it to the environment
            - `SET PROPER_GTK_FOLDER=C:\Program Files\GTK2-Runtime Win64\bin`
            - `SET PATH=%PROPER_GTK_FOLDER%;%PATH%`
           This puts the appropriate GTK at the beginning of the `PATH` and its files are the first found when WeasyPrint requires them.
    - generate a pdf template
    - render pdf files
    - send pdf files by email
    
### Adding coupon system to online shop
- Create coupon system to apply discounts
- Add internationalization
- Use Rosetta to manage translations
- Translate models using `django-parler`
- Build product recommendation engine
