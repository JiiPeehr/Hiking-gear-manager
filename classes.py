# classes

import os

class Item:
    def __init__(self, name: str, category: str, weight: str):
        self.name = name
        self.category = category
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.category}, {self.weight}g"
    
    def __repr__(self):
        return f"{self.name}, {self.category}, {self.weight}g"
    
    def __eq__(self, other):
        return self.name == other.name and self.category == other.category and self.weight == other.weight
    
    # getter for name
    @property
    def name(self):
        return self._name

    # setter for name
    @name.setter
    def name(self, value):
        self._name = value

    # getter for category
    @property
    def category(self):
        return self._category
    
    # setter for category
    @category.setter
    def category(self, value):
        self._category = value

    # getter for weight
    @property
    def weight(self):
        return self._weight
    
    # setter for weight
    @weight.setter
    def weight(self, value):
        self._weight = value

class BaseInventory:
    def __init__(self, items: list[Item]=None):
        if items is None:
            self.items = self.load_file()
        else:
            self.items = items
    

    def load_file(self):
        items = []
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'baseitems.txt')
        try:
            with open(file_path, "r") as file:
                for line in file:
                    name, category, weight = line.strip().split(",")
                    item = Item(name, category, weight)
                    items.append(item)
        except FileNotFoundError:
            pass
        return items

    def save_file(self, items: list[Item]):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'baseitems.txt')
        with open(file_path, "w") as file:
            for item in items:
                file.write(f"{item.name},{item.category},{item.weight}\n")

    def get_items(self):
        return self.items
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

    def remove_all_items(self):
        self.items.clear()
    
    def __str__(self):
        return "\n".join([str(item) for item in self.items])
    
    def __repr__(self):
        return "\n".join([str(item) for item in self.items])
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __iter__(self):
        return iter(self.items)
    
class PackedInventory(BaseInventory):
    def __init__(self):
        super().__init__()

    def load_file(self):
        items = []
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'packeditems.txt')
        try:
            with open(file_path, "r") as file:
                for line in file:
                    name, category, weight = line.strip().split(",")
                    item = Item(name, category, weight)
                    items.append(item)
        except FileNotFoundError:
            pass
        return items
    
    def save_file(self, items: list[Item]):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'packeditems.txt')
        with open(file_path, "w") as file:
            for item in items:
                file.write(f"{item.name},{item.category},{item.weight}\n")
    
    def pack_item(self, item):
        self.add_item(item)
    
    def unpack_item(self, item):
        self.remove_item(item)
