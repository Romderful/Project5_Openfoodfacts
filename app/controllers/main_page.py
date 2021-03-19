"""Main_page controller."""


from app.views.main_page import MainPageView


class MainPage:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.view = MainPageView()

    def get_command(self) -> int:
        """Return user's interface choice."""
        choice = self.view.get_input()
        choices = {
            1: "goto_categories",
            2: "goto_favorites",
            3: "quit"
        }
        command = choices.get(choice, "")
        return command
