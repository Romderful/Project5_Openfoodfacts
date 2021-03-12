"""Main page controller."""


from app.views.console_view import ConsoleView
from app.models.category import Category
from app.models.product import Product

# One controller per model


class MainPage:
    """MainPage class."""

    def __init__(self):
        """Initialise."""
        self.state = 0  # chaine de caractère
        self.category_name = ""
        self.view = ConsoleView()
        self.model_category = Category()
        self.model_product = Product()

    def get_category_input(self):
        """Prompt the user.

        Return his choice.
        """
        if self.state == 1:
            for row in self.model_category.categories:
                for key, value in row.items():
                    self.view.display_choice(key, value)
            self.view.jump_line()
            user_choice = self.view.select_category()
            self.category_name = self.model_category.categories[user_choice][
                user_choice
            ]

        elif self.state == 2:
            self.get_product_input()

    def get_product_input(self):
        """Prompt the user.

        Return his choice.
        """
        self.model_product.get_products(self.category_name)
        for row in self.model_product.products:
            for key, value in row.items():
                self.view.display_choice(key, value)
        self.view.jump_line()
        self.user_choice = self.view.select_product()

    def update(self):
        """Update the controller."""
        self.state += 1
        self.get_category_input()
        self.view.jump_line()
