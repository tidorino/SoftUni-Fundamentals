class Zoo:
    __animal = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animal += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == 'bird':
            result += f"Birds in {self.name}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animal}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
number_animals = int(input())

for numb in range(number_animals):
    info_animal = input().split(" ")
    specie = info_animal[0]
    type_animal = info_animal[1]
    zoo.add_animal(specie, type_animal)

info = input()
print(zoo.get_info(info))



