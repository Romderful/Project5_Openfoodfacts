"""Substitute_page view."""


class SubstituteView:
    """SubstituteView class."""

    @staticmethod
    def save_substitute() -> int:
        """Prompt the user to select a product."""
        return input("Souhaitez vous sauvegarder le substitut ? (yes / no) : ")

    @staticmethod
    def display_choice(value):
        """Display the index followed by the ressources."""
        print(
            f"""
{value['name']}
Nutriscore : {value['nutriscore_id']}
Magasin : {value['store']}
URL : {value['url']}
            """
        )
        print(30 * "-")

    @staticmethod
    def jump_line():
        """Line jump."""
        print()
