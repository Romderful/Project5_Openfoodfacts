"""Category_page view."""


class CategoryView:
    """CategoryView class."""

    def __init__(self, categories):
        """Init the categories."""
        self.categories = categories

    def display(self):
        """Display the choices."""
        print()
        for row in self.categories:
            for key, value in row.items():
                print(f"{key} : {value}")
        print()

    def get_input(self) -> int:
        """Prompt the user asking for a category."""
        return int(input("Sélectionnez la catégorie : "))
