class House:
    def __init__(self):
        self._representation = ''
        pass

    def create_walls(self, color):
        self._representation += f" {color} walls"

    def create_backyard(self, size):
        self._representation += f" {size} backyard"

    def create_roof(self, color):
        self._representation += f"{color} roof"

    def __repr__(self):
        return f"house has: {self._representation}"

    @staticmethod
    def build(config):
        house = House()
        for key, value in config.items():
            if value == None:
                continue
            if key == "walls":
                house.create_walls((value))
            elif key == "backyard":
                house.create_backyard(value)
            elif key == "roof":
                house.create_roof(value)
        return house


config = {'walls': 'white', "backyard": 'big'}
home = House.build(config)
print(home)
