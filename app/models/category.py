"""Category model."""


import random

from database.install import database


class Category:
    """Catgory class."""

    def __init__(self):
        """Initialise."""
        self.cursor = database.cnx.cursor(dictionary=True)
        self.get_categories()

    def get_categories(self) -> list:
        """Get a list of categories."""
        result = []
        categories = []
        query = """
        SELECT DISTINCT category.name FROM category
        INNER JOIN product_category ON category.id = product_category.category_id
        INNER JOIN product ON product.id = product_category.product_id
        WHERE product.name > 9
        LIMIT 10
        """
        self.cursor.execute(query)
        for row in self.cursor:
            result.append(row["name"])
        random.shuffle(result)
        for index, category in enumerate(result):
            categories.append({index: category})
        return categories
