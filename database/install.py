"""Implement database with data."""


import mysql.connector
import requests
import os

from dotenv import load_dotenv


NAME = "generic_name"
STORE = "stores"
URL = "url"
GRADE = "nutrition_grades"
CATEGORIES = "categories"


class Database:
    """Managing openfoodfacts database."""

    def __init__(self):
        """Initialise."""
        load_dotenv()
        self.max_products = 0
        self.valid_products = []
        self.grades = ["a", "b", "c", "d", "e"]
        self.cnx = mysql.connector.connect(
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            charset=os.getenv("CHARSET"),
        )

    def get_data(self, page: int) -> dict:
        """Get the data from openfoodfacts by requesting the API."""
        response = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl",
            {
                "action": "process",
                "tagtype_0": "categories",
                "tagtype_1": "countries",
                "tag_contains_1": "france",
                "page_size": 50,
                "page": page,
                "json": 1,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data

    def get_valid_products(self, data: dict):
        """Append a dict containing all the product ressources required to a list.

        Filter the data by len.
        """
        for index, product in enumerate(data["products"]):
            try:
                new_product = {
                    NAME: product[NAME],
                    STORE: product[STORE],
                    URL: product[URL],
                    GRADE: product[GRADE],
                    CATEGORIES: product[CATEGORIES],
                }
            except KeyError:
                pass
            else:
                if (
                    len(product[NAME]) in range(1, 51)
                    and len(product[STORE]) in range(1, 51)
                    and len(product[URL]) in range(1, 101)
                ):
                    self.valid_products.append(new_product)

    def add_nutriscore(self):
        """Implement the database with the nutriscore values."""
        for grade in self.grades:
            self.cnx.cursor().execute(
                """
                INSERT INTO nutriscore (name)
                VALUES (%(nutrition_grades)s)
                """,
                {GRADE: grade},
            )
            self.cnx.commit()

    def add_product(self):
        """Implement the database with the product values."""
        for product in self.valid_products:
            cursor = self.cnx.cursor()
            query = """
            INSERT IGNORE INTO product (name, store, url, nutriscore_id)
            VALUES(%s, %s, %s,(
            SELECT id FROM nutriscore
            WHERE name = %s))
            """
            ressources = (
                product[NAME],
                product[STORE],
                product[URL],
                product[GRADE],
            )
            cursor.execute(query, (ressources))
            self.cnx.commit()

    def add_category(self):
        """Implement the database with the category values."""
        for product in self.valid_products:
            categories = product[CATEGORIES].split(",")
            for category in categories:
                cursor = self.cnx.cursor()
                query = """
                INSERT IGNORE INTO category (name)
                VALUES(%s)
                """
                ressources = (category.strip(),)
                cursor.execute(query, (ressources))
                self.cnx.commit()

    def add_product_category(self):
        """Implement the database with the categories ids and the products ids."""
        for product in self.valid_products:
            categories = product[CATEGORIES].split(",")
            for category in categories:
                cursor = self.cnx.cursor()
                query = """
                INSERT IGNORE INTO product_category (category_id, product_id)
                VALUES(
                (SELECT id FROM category
                WHERE name = %s),
                (SELECT id FROM product
                WHERE name = %s))
                """
                ressources = (
                    category.strip(),
                    product[NAME],
                )
                cursor.execute(query, (ressources))
                self.cnx.commit()


database = Database()


def main():
    """Make the program work."""
    user_choice = int(input("How many products do you want to add ? : "))
    my_database = Database()
    my_database.max_products = user_choice
    my_database.add_nutriscore()
    page = 1
    while len(my_database.valid_products) <= my_database.max_products:
        data = my_database.get_data(page)
        my_database.get_valid_products(data)
        page += 1
    my_database.valid_products = my_database.valid_products[: my_database.max_products]
    my_database.add_product()
    my_database.add_category()
    my_database.add_product_category()


if __name__ == "__main__":
    main()
