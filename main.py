class Cat:
    view = 'domestic'
    species = "smooth-haired"

    def __init__(self, species, age, color):
        self.species = species
        self.age = age
        self.color = color
        print('Создался объект')



an1 = Cat(species='Asian', age=7, color="grey")
an2 = Cat(species='European', age=10, color="ginger")

print(an1.species)
print(an1.age)
print(an1.color)
print(an2.species)
print(an2.age)
print(an2.color)



