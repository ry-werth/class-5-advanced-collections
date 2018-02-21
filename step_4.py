from data import products_string
from step_1 import transform_products_to_list


def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    
    customers = {}
    
    for product in products_list:
        invoice_id = product[0]
        customer_id = product[-2]
        price = float(product[-3])
        amount = int(product[3])
        
        customers.setdefault(customer_id,{})
        customers[customer_id].setdefault(invoice_id, 0)
        customers[customer_id][invoice_id] += round(price*amount, 2)
        
    print(customers)
    return customers
        
calculate_total_per_invoices(products_string)
