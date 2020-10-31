class House:
    def __init__(self):
        self._represantation =''
        pass
    def create_walls(self, color):
        self._represantation+= f"{color} walls"
    def backyard(self, size):
        self._representation+= f"Your backyard is {size}"
    def roof(self, color):
        self._represantation+= f"{color} roof"
    def __repr__(self):
        return f"house has: {self._represantation}"


    @staticmethod
    def build(config):
        house = House()
        for key, value in config.items():
            if value == None:
                continue
            if key ==  "walls":
                house.create_walls((value))
            elif key == "backyard":
                house.create_backyard(value)
            elif key == "roof":
                house.create_roof(value)
        return house

config= {'walls': 'white', "backyard":'big'}
print(config['walls'])
print(config.keys())
print(config.items())
home = House.build(config)

for key in config.keys():
    print(key, ':', config[key])

for key, value in config.items():
    print(key, ':', value)
h = House()
h.create_walls('white')
print(h)