from datetime import datetime
from myapp.models.recipe import Recipe

class Category:
    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.recipes = dict()
        self.recipe_ids_names = dict()
        self.date_added = datetime.now().strftime('%y-%m-%d %H:%M:%S')
        self.date_modified = datetime.now().strftime('%y-%m-%d %H:%M:%S')

    def create_recipe(self, recipe_id, name, description):
        name = name.strip() .title()
        if name and name in self.recipes:
            return False

        recipe = Recipe(recipe_id, name, description, self.category_id)
        self.recipes[recipe.name] = recipe
        self.recipe_ids_names[recipe.recipe_id] = recipe.name
        return True

    def delete_recipe(self, recipe_id):
        if recipe_id not in self.recipe_ids_names:
            return False
        recipe_name = self.recipe_ids_names[recipe_id]
        del self.recipes[recipe_name]
        del self.recipe_ids_names[recipe_id]
        self.date_modified = datetime.now().strftime('%y-%m-%d %H:%M:%S')
        return True

    def edit_recipe(self, recipe_id, name, description):
        if recipe_id not in self.recipe_ids_names:
            return False

        name = name.title()
        for old_id, old_name in self.recipe_ids_names.items():
            if old_name == name and old_id != recipe_id:
                return False

        recipe = self.recipes[self.recipe_ids_names[recipe_id]]
        recipe.name = name
        recipe.description = description
        self.date_modified = datetime.now.strftime('%y-%m-%d %H:%M:%S')
        return True
