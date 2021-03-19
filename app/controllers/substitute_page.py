"""Substitute controller."""


from app.models.substitute import Substitute
from app.views.substitute_page import SubstituteView

"""
On est ici !
COncrètement, il faudrait 2 choses:
- ne prendre que l'index du produit de base dans init
- notament utile pour afficher ses détails, avant d'afficher les substituts (et leurs détails)

- pas besoin de la catégorie : pourquoi ?
- on souhaite un algo qui soit non pas le plus proche de la catégorie choisie, mais
le plus proche du produit choisie
Comment ? en utilisant la catégorie du produit qui possède le moins de produits.
Pourquoi ? Parce que c'est forcément la catégorie la plus spécialisée.

Du coup, plus besoin de catégorie, et pour le nutriscore, il fera déjà parti du produit de base.


Pour la suite:
- reprendre cette classe et sa vue selon notre façon de procéder (s'aider des autres classes)
- créer un vrai controller favorite et vue favorite
- bien entendu, toujours vérifier et mettre à jour la méthode update de l'application à force d'ajouts
"""


class SubstitutePage:
    """Class SubstitutePage."""

    def __init__(self, category: str, nutriscore: int):
        """Initialise."""
        self.substitute_model = Substitute()
        self.substitute = self.substitute_model.get_substitute(category, nutriscore)

    def get_command(self, product: dict) -> str:
        """Return user's choice, if 'yes', save substitute."""
        user_choice = None
        while user_choice not in ["oui", "non"]:
            user_choice = SubstituteView.display_input()
            if user_choice == "oui":
                self.substitute_model.save_substitute(self.substitute, product)
        return user_choice
