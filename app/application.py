"""Application."""


from app.controllers.category_page import CategoryPage
from app.controllers.product_page import ProductPage
from app.controllers.substitute_page import SubstitutePage
from app.controllers.main_page import MainPage
from app.views.category_page import CategoryView
from app.views.product_page import ProductView
from app.views.substitute_page import SubstituteView


class Application:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.running = True

    def run(self):
        """Run the app."""
        while self.running:
            main_page_controller = MainPage()
            user_choice = main_page_controller.get_input()

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
                SubstituteView.display_choices(substitute_controller.substitute)
                substitute_controller.get_input(product)

            elif user_choice == 2:
                substitute_view = SubstituteView()
                substitute_view.display_saved_substitutes()

            elif user_choice == 3:
                self.running = False
