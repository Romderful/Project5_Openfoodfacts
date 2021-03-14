"""Product model."""


import random

from database.install import database


class Product:
    """Product class."""

    def __init__(self):
        """Initialise."""
        self.cursor = database.cnx.cursor(dictionary=True)

    def get_products(self, user_choice: str) -> list:
        """Get a list of products."""
        result = []
        products = []
        query = """
        SELECT DISTINCT product.name, product.nutriscore_id FROM product
        INNER JOIN product_category ON product.id = product_category.product_id
        INNER JOIN category ON category.id = product_category.category_id
        WHERE category.name = %s
        LIMIT 10
        """
        category_name = (user_choice,)
        self.cursor.execute(query, (category_name))
        for row in self.cursor:
            result.append(row)
        random.shuffle(result)
        for index, product in enumerate(result):
            products.append({index: product})
        return products
