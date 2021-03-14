"""Product controller."""


from app.views.product_page import ProductView
from app.models.product import Product
from app.controllers.category_page import CategoryPage


class ProductPage:
    """Class ProductPage."""

    def __init__(self):
        """Initialise."""
        self.nutriscore = 0
        self.view = ProductView()
        self.model_product = Product()
        self.controller_category = CategoryPage()

    def get_input(self, category: str):
        """Prompt the user.

        Ask him to pick a product.
        """
        products = self.model_product.get_products(
            user_choice=category, products_number=10
        )
        for row in products:
            for key, value in row.items():
                self.view.display_choice(key, value)
        self.view.jump_line()
        user_choice = self.view.select_product()
        self.view.jump_line()
        self.nutriscore = products[user_choice][user_choice]["nutriscore_id"]
