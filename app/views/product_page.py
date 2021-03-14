"""Product_page view."""


class ProductView:
    """ProductView class."""

    @staticmethod
    def select_product() -> int:
        """Prompt the user to select a product."""
        return int(input("Sélectionnez le produit : "))

    @staticmethod
    def display_choice(key, value):
        """Display the index followed by the ressources."""
        print(f"{key} : {value['name']}\n    Nutriscore : {value['nutriscore_id']}")
        print(30 * "-")

    @staticmethod
    def jump_line():
        """Line jump."""
        print()
