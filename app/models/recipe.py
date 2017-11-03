class Recipe:
    def __init__(self, name, recipe_id, description, category_id):
        self.name = name
        self.recipe_id = recipe_id
        self.description = description
        self.category_id = category_id
        self.procedures = []  # list of procedures
        self.ingredients = []  # list of ingredients

    def add_procedure(self, procedure):
        if procedure.strip().capitalize() in self.procedures:
            return False
        self.procedures.append(procedure)
        return True

    def remove_procedure(self, procedure):
        try:
            self.procedures.remove(procedure)
            return True
        except ValueError:
            return False

    def add_ingredient(self, ingredient):
        if ingredient.strip().lower() in self.ingredients:
            return False
        self.ingredients.append(ingredient)
        return True

    def remove_ingredient(self, ingredient):
        try:
            self.ingredients.remove(ingredient)
            return True
        except ValueError:
            return False
