"""Category model."""


import random

from database.install import database

# Rather return than using instance vars (categories)


class Category:
    """Catgory class."""

    def __init__(self):
        """Initialise."""
        self.cursor = database.cnx.cursor(dictionary=True)
        self.categories = []
        self.get_categories(categories_number=11)

    def get_categories(self, categories_number):
        """Get a list of categories."""
        result = []
        query = "SELECT name FROM category"
        self.cursor.execute(query)
        for row in self.cursor:
            result.append(row["name"])
        random.shuffle(result)
        for index, category in enumerate(result[:categories_number]):
            self.categories.append({index: category})
