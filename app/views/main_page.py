"""Main_page view."""


class MainPageView:
    """MainPageView class."""

    @staticmethod
    def select_interface() -> int:
        """Prompt the user and ask for an option."""
        return int(
            input(
                """
1 - Quel aliment souhaitez vous remplacer ?
2 - Retrouver mes aliments substitués.
3 - Quitter le programme.
"""
            )
        )
