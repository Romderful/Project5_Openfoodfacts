"""Product controller."""


from app.views.product_page import ProductView
from app.models.product import Product


MAX_PRODUCTS = 10


class ProductPage:
    """Class ProductPage."""

    def __init__(self):
        """Initialise."""
        self.view = ProductView()
        self.model_product = Product()

    def get_input(self, category: str):
        """Prompt the user.

        Ask him to pick a product and return his choice.
        """
        products = self.model_product.get_products(category)
        for row in products:
            for key, value in row.items():
                self.view.display_choice(key, value)
        self.view.jump_line()
        user_choice = None
        while user_choice not in range(MAX_PRODUCTS):
            try:
                user_choice = self.view.select_product()
                product_choice = products[user_choice][user_choice]
            except ValueError:
                pass
            except IndexError:
                pass
            else:
                self.view.jump_line()
                return product_choice
