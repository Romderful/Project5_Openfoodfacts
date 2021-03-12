"""Product model."""


import random

from database.install import database

# Rather return than using instance vars (products)


class Product:
    """Product class."""

    def __init__(self):
        """Initialise."""
        self.cursor = database.cnx.cursor(dictionary=True)
        self.products = []

    def get_products(self, user_choice, products_number=11):
        """Get a list of products."""
        result = []
        query = """
        SELECT DISTINCT product.name FROM product
        INNER JOIN product_category ON product.id = product_category.product_id
        INNER JOIN category ON category.id = product_category.category_id
        WHERE category.name = %s
        """
        category_name = (user_choice,)
        self.cursor.execute(query, (category_name))
        for row in self.cursor:
            result.append(row["name"])
        random.shuffle(result)
        for index, product in enumerate(result[:products_number]):
            self.products.append({index: product})
