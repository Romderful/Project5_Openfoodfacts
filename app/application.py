"""Application."""


from app.controllers.main_page import MainPage


class Application:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.controller_main_page = MainPage()

    def run(self):
        """Run the app."""
        running = True
        while running:
            if not self.controller_main_page.get_input():
                running = False
