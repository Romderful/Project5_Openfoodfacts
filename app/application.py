"""Application."""

from app.controllers.category_page import CategoryPage
from app.controllers.product_page import ProductPage
from app.controllers.substitute_page import SubstitutePage


class Application:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.category_controller = CategoryPage()
        self.product_controller = ProductPage()
        self.substitute_controller = SubstitutePage()

    def run(self):
        """Run the app."""
        category = self.category_controller.get_input()
        nutriscore = self.product_controller.get_input(category)
        self.substitute_controller.get_input(category, nutriscore)
