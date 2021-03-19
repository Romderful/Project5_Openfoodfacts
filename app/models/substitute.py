"""Substitute model."""


from database.install import database


INDEX = 0
KEY = 0


class Substitute:
    """Substitute class."""

    def __init__(self):
        """Initialise."""
        self.cursor = database.cnx.cursor(dictionary=True)

    def get_substitute(self, category: str, nutriscore: int) -> list:
        """Return the substitute in a list."""
        result = []
        substitute = []
        query = """
        SELECT DISTINCT product.name AS ProductName, nutriscore.name AS NutriscoreName,
        product.nutriscore_id, product.store, product.url FROM product
        INNER JOIN product_category ON product.id = product_category.product_id
        INNER JOIN category ON category.id = product_category.category_id
        INNER JOIN nutriscore ON nutriscore.id = product.nutriscore_id
        WHERE category.name = %s
        AND product.nutriscore_id < %s
        LIMIT 1
        """
        ressources = (
            category,
            nutriscore,
        )
        self.cursor.execute(query, (ressources))
        for row in self.cursor:
            result.append(row)
        for index, product in enumerate(result):
            substitute.append(product)
        return substitute

    def get_saved_substitutes(self) -> list:
        """Return the saved substitutes in a list."""
        result = []
        saved_substitutes = []
        query = """
        SELECT product.name AS ProductName, nutriscore.name AS NutriscoreName,
        product.nutriscore_id, product.store, product.url FROM product
        INNER JOIN substitute ON product.id = substitute.substitute_id
        INNER JOIN nutriscore ON nutriscore.id = product.nutriscore_id
        WHERE product.id = substitute.substitute_id
        """
        self.cursor.execute(query)
        for row in self.cursor:
            result.append(row)
        for index, product in enumerate(result):
            saved_substitutes.append(product)
        return saved_substitutes

    def save_substitute(self, substitute: list, product: dict):
        """Save the substitute in the database."""
        substitute_name = substitute[INDEX][KEY]["ProductName"]
        product_name = product["ProductName"]
        query = """
        INSERT INTO substitute (substitute_id, base_id)
        VALUES(
        (SELECT id FROM product WHERE name = %s),
        (SELECT id FROM product WHERE name = %s))
        """
        ressources = (
            substitute_name,
            product_name,
        )
        self.cursor.execute(query, (ressources))
        database.cnx.commit()
