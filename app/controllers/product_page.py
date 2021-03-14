"""Product controller."""


from app.views.product_page import ProductView
from app.models.product import Product
from app.controllers.category_page import CategoryPage


class ProductPage:
    """Class ProductPage."""

    def __init__(self):
        """Initialise."""
        self.view = ProductView()
        self.model_product = Product()
        self.controller_category = CategoryPage()

    def get_input(self, category):
        """Prompt the user.

        Return his choice.
        """
        products = self.model_product.get_products(
            user_choice=category, products_number=11
        )
        for row in products:
            for key, value in row.items():
                self.view.display_choice(key, value)
        self.view.jump_line()
        user_choice = self.view.select_product()
        return user_choice
