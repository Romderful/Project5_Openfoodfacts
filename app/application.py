"""Application."""


from app.controllers.main_page import MainPage
from app.controllers.category_page import CategoryPage
from app.controllers.product_page import ProductPage
from app.controllers.substitute_page import SubstitutePage

from app.views.category_page import CategoryView
from app.views.product_page import ProductView
from app.views.substitute_page import SubstituteView


class Application:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.running = True
        self.controller = MainPage()

    def run(self):
        """Run the app."""
        while self.running:
            self.controller.view.display()
            command = self.controller.get_command()
            self.update(command)

    def update(self, command: str):
        """Update the program."""
        if command == "quit":
            self.running = False
        if command == "goto_categories":
            self.controller = CategoryPage()
        if command.startswith("goto_category_"):
            category_index = int(command.replace("goto_category_", ""))
            self.controller = ProductPage(category_index)
        if command.startswith("goto_product_"):
            product_index = int(command.replace("goto_product_", ""))
            self.controller = SubstitutePage(product_index)

