"""Application."""

from app.controllers.category_page import CategoryPage
from app.controllers.product_page import ProductPage


class Application:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.category_controller = CategoryPage()
        self.product_controller = ProductPage()

    def run(self):
        """Run the app."""
        category = self.category_controller.get_input()
        self.product_controller.get_input(category)
