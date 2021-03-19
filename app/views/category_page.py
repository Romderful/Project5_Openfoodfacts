"""Category_page view."""


class CategoryView:
    """CategoryView class."""

    def __init__(self, categories):
        """Init the categories."""
        self.categories = categories

    def display(self):
        """Display the choices."""
        print()
        for index, row in enumerate(self.categories, start=1):
            print(f"{index} : {row}")
        print()

    def get_input(self) -> int:
        """Prompt the user asking for a category."""
        return int(input("Sélectionnez la catégorie : "))
