product_list ={}


def add_product(product_list):
    product_name = input ("Enter product name: ")
    product_quantity = input ("Enter product quantity: ")
    if product_name in product_list:
        product_list[product_name] += product_quantity
    else:
        product_list[product_name] = product_quantity

    print(product_name,product_quantity,"unit")

def show_product(product_list):
    for key in product_list.keys():
        print(product_list[key] + " : " + product_list[key])

add_product(product_list)
add_product(product_list)
add_product(product_list)
show_product(product_list)