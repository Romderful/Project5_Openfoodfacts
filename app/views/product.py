"""Product_page view."""


class ProductView:
    """ProductView class."""

    @staticmethod
    def display_choices(products: list):
        """Display the choices."""
        print()
        for row in products:
            for key, value in row.items():
                print(
                    f"{key}: {value['ProductName']} | score: {value['NutriscoreName']}"
                )
        print()

    @staticmethod
    def display_input() -> int:
        """Prompt the user and ask for a product."""
        return int(input("Sélectionnez le produit : "))
