cities = []
city_population = []

while True:
    city = input("give the name of a city: ")
    if city == "stop":
        break
    cities.append(city)

for city in cities:
    city_population.append((city, len(city)))

def sortFunc(e):
    return e[1]

cities_sorted = sorted(city_population, key=sortFunc, reverse=True)

for city, population in cities_sorted:
    print(f"{city} => {population * 1000000}")