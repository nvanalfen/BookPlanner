class BaseCategory:
    def __init__(self):
        self.title = ""
        self.entities = set()

class Category(BaseCategory):
    def __init__(self):
        super().__init__()

        self.description = ""
        self.super_category = None
        self.sub_categories = set()