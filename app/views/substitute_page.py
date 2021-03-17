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
                print(
                    f"""
{value['name']}
Nutriscore : {value['nutriscore_id']}
Magasin : {value['store']}
URL : {value['url']}
                    """
                )

    @staticmethod
    def display_choices(substitute: list):
        """Display the substitute."""
        for row in substitute:
            for key, value in row.items():
                print(
                    f"""
{value['name']}
Nutriscore : {value['nutriscore_id']}
Magasin : {value['store']}
URL : {value['url']}
                    """
                )

    @staticmethod
    def display_input() -> str:
        """Prompt the user and ask him whether he wants to save or not."""
        return input("Souhaitez vous sauvegarder le substitut ? (yes / no) : ")
