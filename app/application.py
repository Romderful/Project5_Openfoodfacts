"""Application."""

from app.controllers.category_page import CategoryPage
from app.controllers.product_page import ProductPage
from app.controllers.substitute_page import SubstitutePage
from app.models.substitute import Substitute


class Application:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.category_controller = CategoryPage()
        self.product_controller = ProductPage()
        self.substitute_controller = SubstitutePage()
        self.substitute_model = Substitute()

    def run(self):
        """Run the app."""
        category = self.category_controller.get_input()
        product = self.product_controller.get_input(category)
        substitute = self.substitute_controller.get_input(
            category, product["nutriscore_id"]
        )
        self.substitute_model.save_substitute(substitute, product)
