"""Substitute_page view."""


from app.models.substitute import Substitute


class SubstituteView:
    """SubstituteView class."""

    def __init__(self):
        """Initialise."""
        self.substitute_model = Substitute()
        self.saved_substitutes = self.substitute_model.get_saved_substitutes()

    def display_saved_substitutes(self):
        """Display the saved substitutes."""
        for row in self.saved_substitutes:
            for key, value in row.items():
                print(f"{value['ProductName']}")
                print(f"Nutriscore : {value['NutriscoreName']}")
                print(f"Magasin : {value['store']}")
                print(f"URL : {value['url']}")

    @staticmethod
    def display(substitute: list):
        """Display the substitute."""
        for row in substitute:
            for key, value in row.items():
                print(
                    f"""
{value['ProductName']}
Nutriscore : {value['NutriscoreName']}
Magasin : {value['store']}
URL : {value['url']}
                    """
                )

    @staticmethod
    def get_input() -> str:
        """Prompt the user and ask him whether he wants to save or not."""
        return input("Souhaitez vous sauvegarder le substitut ? (oui / non) : ").lower()
