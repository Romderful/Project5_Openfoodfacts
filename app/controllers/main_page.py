"""Main_page controller."""

from app.controllers.category_page import CategoryPage
from app.controllers.product_page import ProductPage
from app.controllers.substitute_page import SubstitutePage
from app.models.substitute import Substitute
from app.views.main_page import MainPageView
from app.views.substitute_page import SubstituteView


class MainPage:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.category_controller = CategoryPage()
        self.product_controller = ProductPage()
        self.substitute_controller = SubstitutePage()
        self.substitute_model = Substitute()
        self.substitute_view = SubstituteView()
        self.main_page_view = MainPageView()

    def get_input(self) -> bool:
        """Prompt the user and return a bool."""
        try:
            user_choice = self.main_page_view.select_interface()
        except ValueError:
            pass
        else:
            if user_choice == 1:
                category = self.category_controller.get_input()
                product = self.product_controller.get_input(category)
                substitute = self.substitute_controller.get_input(
                    category, product["nutriscore_id"]
                )
                self.substitute_model.save_substitute(substitute, product)
            elif user_choice == 2:
                saved_substitutes = self.substitute_model.get_saved_substitutes()
                for row in saved_substitutes:
                    for key, value in row.items():
                        self.substitute_view.display_choice(value)
            elif user_choice == 3:
                return False
            return True
