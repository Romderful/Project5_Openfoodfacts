"""Category controller."""


from app.models.category import Category
from app.views.category_page import CategoryView


MAX_CATEGORIES = 10


class CategoryPage:
    """Class CategoryPage."""

    def __init__(self):
        """Initialise."""
        self.model = Category()
        self.categories = self.model.get_categories()

        self.view = CategoryView(self.categories)

    def get_command(self) -> str:
        """Return user's category choice."""
        choice = self.view.get_input()
        choices = {num: f"goto_category_{num}" for num in range(1, len(self.categories) + 1)}
        command = choices.get(command, "")
        return command
