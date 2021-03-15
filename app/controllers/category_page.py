"""Category controller."""


from app.views.category_page import CategoryView
from app.models.category import Category


class CategoryPage:
    """Class CategoryPage."""

    def __init__(self):
        """Initialise."""
        self.view = CategoryView()
        self.model_category = Category()

    def get_input(self) -> str:
        """Prompt the user.

        Ask him to pick a category and return his choice.
        """
        categories = self.model_category.get_categories()
        for row in categories:
            for key, value in row.items():
                self.view.display_choice(key, value)
        self.view.jump_line()
        user_choice = None
        while user_choice not in range(10):
            try:
                user_choice = self.view.select_category()
                category_choice = categories[user_choice][user_choice]
            except ValueError:
                pass
            except IndexError:
                pass
            else:
                self.view.jump_line()
                return category_choice
