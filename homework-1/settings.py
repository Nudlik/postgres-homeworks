import os


PASSWORD = os.getenv('POSTGRES_PASSWORD')

PATH_TO_CUSTOMERS = os.path.join(os.path.dirname(__file__), 'north_data', 'customers_data.csv')
PATH_TO_EMPLOYEES = os.path.join(os.path.dirname(__file__), 'north_data', 'employees_data.csv')
PATH_TO_ORDERS = os.path.join(os.path.dirname(__file__), 'north_data', 'orders_data.csv')

LST_TABLES = [
    ('customers', PATH_TO_CUSTOMERS),
    ('employees', PATH_TO_EMPLOYEES),
    ('orders', PATH_TO_ORDERS),
]
