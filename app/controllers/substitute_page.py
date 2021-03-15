"""Substitute controller."""


from app.views.substitute_page import SubstituteView
from app.models.substitute import Substitute
from app.controllers.product_page import ProductPage


class SubstitutePage:
    """Class SubstitutePage."""

    def __init__(self):
        """Initialise."""
        self.view = SubstituteView()
        self.model_substitute = Substitute()
        self.controller_product = ProductPage()

    def get_input(self, nutriscore: int, category: str) -> str:
        """Prompt the user.

        Ask him whether he wants to save the substitute in the database.
        Return his choice.
        """
        substitutes = self.model_substitute.get_substitute(nutriscore, category)
        for row in substitutes:
            for key, value in row.items():
                self.view.display_choice(value)
        self.view.jump_line()
        user_choice = self.view.save_substitute()
        return user_choice
