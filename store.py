from typing import List, Tuple
from products import Product  # Assuming `Product` is defined in a file named `products.py`

class Store:
    def __init__(self, products: List[Product]):
        """
        Initializes the Store with a list of products.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a product to the store.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Returns all active products in the store.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order from a shopping list of (Product, quantity) tuples.
        Returns the total cost of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price