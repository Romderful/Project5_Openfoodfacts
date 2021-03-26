"""Application."""


from app.controllers.category import CategoryPage
from app.controllers.product import ProductPage
from app.controllers.substitute import SubstitutePage
from app.controllers.menu import MainPage
from app.views.category import CategoryView
from app.views.product import ProductView
from app.views.substitute import SubstituteView


class Application:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.running = True

    def run(self):
        """Run the app."""
        while self.running:
            menu_controller = MainPage()
            user_choice = menu_controller.get_input()

            if user_choice == 1:
                category_controller = CategoryPage()
                CategoryView.display_choices(category_controller.categories)
                category = category_controller.get_input()

                product_controller = ProductPage(category)
                ProductView.display_choices(product_controller.products)
                product = product_controller.get_input()

                substitute_controller = SubstitutePage(
                    category, product["nutriscore_id"]
                )
                if SubstituteView.display_choices(substitute_controller.substitute):
                    substitute_controller.get_input(product)

            elif user_choice == 2:
                substitute_view = SubstituteView()
                substitute_view.display_saved_substitutes()

            elif user_choice == 3:
                self.running = False
