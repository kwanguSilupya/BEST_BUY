from products import Product
from store import Store

def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)

    # Get all active products
    products = store.get_all_products()
    print("Active products:")
    for product in products:
        print(product.show())

    # Get total quantity in the store
    print("\nTotal quantity in store:", store.get_total_quantity())

    # Place an order
    order_cost = store.order([(products[0], 1), (products[1], 2)])
    print("\nOrder cost:", order_cost, "dollars")

    # Add a new product
    new_product = Product("Samsung Galaxy S23", price=800, quantity=300)
    store.add_product(new_product)
    print("\nAdded new product:", new_product.show())

    # Remove a product
    store.remove_product(products[1])
    print("\nRemoved a product. Remaining products:")
    for product in store.get_all_products():
        print(product.show())

if __name__ == "__main__":
    main()