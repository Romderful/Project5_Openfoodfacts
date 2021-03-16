"""Substitute controller."""


from app.views.substitute_page import SubstituteView
from app.models.substitute import Substitute


class SubstitutePage:
    """Class SubstitutePage."""

    def __init__(self, category: str, nutriscore: int):
        """Initialise."""
        self.model_substitute = Substitute()
        self.substitute = self.model_substitute.get_substitute(category, nutriscore)

    def get_input(self, product: dict) -> str:
        """Return user's choice, if 'yes', save substitute."""
        user_choice = None
        while user_choice not in ["yes", "no"]:
            user_choice = SubstituteView.display_input()
            if user_choice == "yes":
                self.model_substitute.save_substitute(self.substitute, product)
        return user_choice
