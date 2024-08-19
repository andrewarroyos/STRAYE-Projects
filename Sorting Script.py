# Andrew Arroyos
# Sort orders for STRAYE INTERNATIONAL
# August 11, 2024

import csv

# Function to read CSV file
def read_orders(file_name):
    orders = []
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            orders.append(row)
    return orders


# Function for sorting the orders
def sort_orders(orders):    
    orders.sort(key=lambda x: (int(x['Name'].split('-')[-1])))
    
    # Logans List
    logans = [] 
    logan_puffs = []
    v2s = []

    # Gowers list
    gowers = []
    
    # Mystery list
    mystery = []

    # Doubles list
    doubles = []
    name_counts = {}  # Dictionary to store the count of each name


    # Conditions for sorting orders
    for order in orders:

        # Checking duplicate order numbers
        order_name = order['Name']
        if order_name in name_counts:
            name_counts[order_name] += 1
        else:
            name_counts[order_name] = 1

        # Now, let's find the names that appear more than once
        duplicates = [name for name, count in name_counts.items() if count > 1]
        if duplicates and order['Lineitem name'] != "SHIP SAFE":
            doubles.append(order)

        if order['Lineitem name'] != "SHIP SAFE" and order['Lineitem name'].split()[0] == "LOGAN" and order['Lineitem name'].split()[1] != "PUFF" and "v2" not in order['Lineitem name']:
            logans.append(order)

        if "v2" in order['Lineitem name']:
            v2s.append(order)

        elif order['Lineitem name'] != "SHIP SAFE" and order['Lineitem name'].split()[1] == "PUFF":
            logan_puffs.append(order)

        elif "GOWER" in order['Lineitem name']:
            gowers.append(order)

        elif "MYSTERY" in order['Lineitem name']:
            mystery.append(order)

    return logans, logan_puffs, v2s, gowers, mystery, doubles


# Function to print orders
def print_orders(orders, title):
    print(f"\n\n--- {title} ---")
    for order in orders:
        print(f"Order ID: {order['Name']}, Product: {order['Lineitem name']}")


# Function to generate a sorted report
def generate_sorted_report(orders, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Name','Email','Financial Status','Paid at','Fulfillment Status','Fulfilled at','Accepts Marketing','Currency','Subtotal','Shipping','Taxes','Total','Discount Code','Discount Amount','Shipping Method','Created at','Lineitem quantity','Lineitem name','Lineitem price','Lineitem compare at price','Lineitem sku','Lineitem requires shipping','Lineitem taxable','Lineitem fulfillment status','Billing Name','Billing Street','Billing Address1','Billing Address2','Billing Company','Billing City','Billing Zip','Billing Province','Billing Country','Billing Phone','Shipping Name','Shipping Street','Shipping Address1','Shipping Address2','Shipping Company','Shipping City','Shipping Zip','Shipping Province','Shipping Country','Shipping Phone','Notes','Note Attributes','Cancelled at','Payment Method','Payment Reference','Refunded Amount','Vendor','Outstanding Balance','Employee','Location','Device ID','Id','Tags','Risk Level','Source','Lineitem discount','Tax 1 Name','Tax 1 Value','Tax 2 Name','Tax 2 Value','Tax 3 Name','Tax 3 Value','Tax 4 Name','Tax 4 Value','Tax 5 Name','Tax 5 Value','Phone','Receipt Number','Duties','Billing Province Name','Shipping Province Name','Payment ID','Payment Terms Name','Next Payment Due At','Payment References']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for order in orders:
            writer.writerow({
                'Name': order['Name'],
                'Email': order['Email'],
                'Lineitem quantity': order['Lineitem quantity'],
                'Lineitem name': order['Lineitem name'], })


# main
file_name = 'STRAYE_ORDERS.csv'
orders = read_orders(file_name)

logans, logan_puffs, v2s, gowers, mystery, doubles = sort_orders(orders)

# Print both lists
print_orders(logans, "Logan List: ")
print_orders(logan_puffs, "Logan Puff List: ")
print_orders(v2s, "All V2 shoes: ")
print_orders(gowers, "Gower Shoes: ")
print_orders(mystery, "Mystery Shoes: ")
print_orders(doubles, "Doubles: ")




# Generate CSV reports
generate_sorted_report(logans, 'logans.csv')
generate_sorted_report(logan_puffs, 'logan_puffs.csv')
generate_sorted_report(v2s, 'v2s.csv')
generate_sorted_report(gowers, 'gowers.csv')
generate_sorted_report(mystery, 'mysterys.csv')
generate_sorted_report(doubles, 'doubles.csv')