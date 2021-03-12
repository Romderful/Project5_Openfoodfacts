"""Application."""

from app.controllers.main_page import MainPage


class Application:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.controller = MainPage()
        self.running = True

    def run(self):
        """Run the app."""
        # while self.running:
        for _ in range(2):
            self.controller.update()
