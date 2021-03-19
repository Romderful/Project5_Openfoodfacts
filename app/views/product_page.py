"""Product_page view."""


class ProductView:
    """ProductView class."""

    def __init__(self, products: list):
        self.products = products

    def display(self):
        """Display the choices."""
        print()
        for row in self.products:
            for key, value in row.items():
                print(f"{key} : {value['ProductName']} - {value['NutriscoreName']}")
        print()

    def get_input(self) -> int:
        """Prompt the user asking for a product."""
        return int(input("Sélectionnez le produit : "))
