"""Main_page controller."""


from app.views.menu import MainPageView


class MainPage:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.menu_view = MainPageView()

    def get_input(self) -> int:
        """Return user's interface choice."""
        user_choice = None
        while user_choice not in range(3):
            try:
                user_choice = self.menu_view.select_interface()
            except ValueError:
                pass
            else:
                return user_choice
