"""Product_page view."""


class ProductView:
    """ProductView class."""

    @staticmethod
    def display_choices(products: list):
        """Display the choices."""
        print()
        for row in products:
            for key, value in row.items():
                print(f"{key} : {value['name']} - {value['nutriscore_id']}")
        print()

    @staticmethod
    def display_input() -> int:
        """Prompt the user asking for a product."""
        return int(input("Sélectionnez le produit : "))
