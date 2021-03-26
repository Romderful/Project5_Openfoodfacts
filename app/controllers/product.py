"""Product controller."""


from app.models.product import Product
from app.views.product import ProductView


class ProductPage:
    """Class ProductPage."""

    def __init__(self, category: str):
        """Initialise."""
        self.product_model = Product()
        self.products = self.product_model.get_products(category)

    def get_input(self) -> dict:
        """Return user's product choice."""
        user_choice = None
        while user_choice not in range(len(self.products)):
            try:
                user_choice = ProductView.display_input()
                product_choice = self.products[user_choice][user_choice]
            except ValueError:
                pass
            except IndexError:
                pass
            else:
                return product_choice
