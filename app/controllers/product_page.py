"""Product controller."""


from app.models.category import Category
from app.models.product import Product
from app.views.product_page import ProductView


MAX_PRODUCTS = 10


class ProductPage:
    """Class ProductPage."""

    def __init__(self, category_index: int):
        """Initialise."""
        category = Category().get_categories()[category_index]

        self.product_model = Product()
        self.products = self.product_model.get_products(category)

        self.view = ProductView(self.products)

    def get_command(self) -> dict:
        """Return user's product choice."""
        user_choice = self.view.get_input()
        choices = {num: f"goto_product_{num}" for num in range(1, len(self.products) + 1)}
        command = choices.get(command, "")
        return command
