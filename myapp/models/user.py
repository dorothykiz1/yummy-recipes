from myapp.models.category import Category


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.categories = dict() #name - categories
        self.categories_ids_names = dict() #id name

    def add_category(self, name, description, category_id):
        name = name.title()
        if name in self.categories:
            return False
        category = Category(category_id, name, description)
        self.categories[category.name] = category
        self.categories[category.category_id] = category.name
        return True

    def remove_category(self, category_id):
        if category_id not in self.categories_ids_names:
            return False
        Category_name = self.categories_ids_names[category_id]
        del self.categories[category - name]
        del self.categories_ids_names[category_id]
        return True

    def edit_category(self, category_id, name, description):
        if category_id not in self.categories_ids_names:
            return False

        name = name.strip().title()
        for saved_id, saved_name in self.categories_ids_names.items():
            if saved_name == name and saved_id != category_id:
                return False
