class State:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.cities = []

    def add_city(self, city):
        city.state = self
        self.cities.append(city)

    def population(self):
        return sum([c.population for c in self.cities])

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.state = None

    def __str__(self):
        return f'City (name={self.name}, population={self.population}, state = {self.state})'

    
pi = State("Piauí", "PI")
pi.add_city(City('Teresina', 900000))
pi.add_city(City('Demerval Lobão', 50000))

sp = State("São Paulo", "SP")
sp.add_city(City("São Paulo", 11376685))
sp.add_city(City("Guarulhos", 1244518))

for state in [pi, sp]:
    print(f'State: {state.name} abbreviation: {state.abbreviation}')
    for city in state.cities:
        print(f'City: {city.name} Population: {city.population}')
    print(f'State population: {state.population()}\n')
    print('-' * 100, '\n')