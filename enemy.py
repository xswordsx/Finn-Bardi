class Enemy:

    def __init__(name, stats, img_path, loot):
        self._name = name
        self._stats = stats
        self._img_path = img_path
        self._loot = loot
        self._current_hp = -1

    def inflict_damage(self):
        # Returns damage, that it can inflict
        pass

    def take_damage(self):
        # Takes some damage
        pass

    def is_alive(self):
        return self._current_hp > 0
