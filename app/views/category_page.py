"""Category_page view."""


class CategoryView:
    """CategoryView class."""

    @staticmethod
    def select_category() -> int:
        """Prompt the user to select a category."""
        return int(input("Sélectionnez la catégorie : "))

    @staticmethod
    def display_choice(key, value):
        """Display the index followed by the ressources."""
        print(f"{key} : {value}")

    @staticmethod
    def jump_line():
        """Line jump."""
        print()
