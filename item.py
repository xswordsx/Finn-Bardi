class Item:

    def __init__(self, name, description, stats, equippable_on, img_path=None):
        self._name = name
        self._description = description
        self._stats = stats
        self._equippable_on = equippable_on
        self._img_path = img_path

