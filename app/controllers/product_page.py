"""Product controller."""


from app.views.product_page import ProductView
from app.models.product import Product


class ProductPage:
    """Class ProductPage."""

    def __init__(self):
        """Initialise."""
        self.nutriscore = 0
        self.view = ProductView()
        self.model_product = Product()

    def get_input(self, category: str):
        """Prompt the user.

        Ask him to pick a product.
        """
        products = self.model_product.get_products(user_choice=category)
        for row in products:
            for key, value in row.items():
                self.view.display_choice(key, value)
        self.view.jump_line()
        user_choice = self.view.select_product()
        self.nutriscore = products[user_choice][user_choice]["nutriscore_id"]
        self.view.jump_line()
