"""Product model."""


import random

from database.install import database


MAX_PRODUCTS = 10


class Product:
    """Product class."""

    def __init__(self):
        """Initialise."""
        self.cursor = database.cnx.cursor(dictionary=True)

    def get_products(self, category: str) -> list:
        """Return a list of products."""
        result = []
        products = []
        query = """
        SELECT DISTINCT product.name, product.nutriscore_id FROM product
        INNER JOIN product_category ON product.id = product_category.product_id
        INNER JOIN category ON category.id = product_category.category_id
        WHERE category.name = %s
        """
        category_name = (category,)
        self.cursor.execute(query, (category_name))
        for row in self.cursor:
            result.append(row)
        random.shuffle(result)
        for index, product in enumerate(result[:MAX_PRODUCTS]):
            products.append({index: product})
        return products
