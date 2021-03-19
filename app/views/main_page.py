"""Main_page view."""


class MainPageView:
    """MainPageView class."""

    def display(self):
        """Prompt the user asking for an option."""
        print("1 - Quel aliment souhaitez vous remplacer ?")
        print("2 - Retrouver mes aliments substitués.")
        print("3 - Quitter le programme.")

    def get_input(self):
        return int(input())
