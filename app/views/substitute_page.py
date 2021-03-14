"""Substitute_page view."""


class SubstituteView:
    """SubstituteView class."""

    @staticmethod
    def select_substitute() -> int:
        """Prompt the user to select a product."""
        return int(input("Sélectionnez le substitut : "))

    @staticmethod
    def display_choice(key, value):
        """Display the index followed by the ressources."""
        print(
            f"""
{key} : {value['name']}
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
