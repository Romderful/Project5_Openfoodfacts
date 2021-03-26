"""Category_page view."""


class CategoryView:
    """CategoryView class."""

    @staticmethod
    def display_choices(categories: list):
        """Display the choices."""
        print()
        for row in categories:
            for key, value in row.items():
                print(f"{key}: {value}")
        print()

    @staticmethod
    def display_input() -> int:
        """Prompt the user and ask for a category."""
        return int(input("Sélectionnez la catégorie : "))
