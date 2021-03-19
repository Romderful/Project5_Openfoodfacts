"""Substitute controller."""


from app.models.substitute import Substitute
from app.views.substitute_page import SubstituteView


class SubstitutePage:
    """Class SubstitutePage."""

    def __init__(self, category: str, nutriscore: int):
        """Initialise."""
        self.substitute_model = Substitute()
        self.substitute = self.substitute_model.get_substitute(category, nutriscore)

    def get_input(self, product: dict) -> str:
        """Return user's choice, if 'yes', save substitute."""
        user_choice = None
        while user_choice not in ["oui", "non"]:
            user_choice = SubstituteView.display_input()
            if user_choice == "oui":
                self.substitute_model.save_substitute(self.substitute, product)
        return user_choice
