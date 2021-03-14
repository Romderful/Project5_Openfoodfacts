"""Product_page view."""


class ProductView:
    """ProductView class."""

    @staticmethod
    def select_product() -> int:
        """Prompt the user to select a product."""
        return int(input("Sélectionnez le produit : "))

    @staticmethod
    def display_choice(key, value):
        """Display the index related to the product / category."""
        print(f"{key} : {value}")

    @staticmethod
    def jump_line():
        """Line jump."""
        print()
