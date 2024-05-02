import random

class City:
    def __init__(self, name):
        self.name = name

class TSPBoardGame:
    def __init__(self, city_names):
        self.cities = [City(name) for name in city_names]
        self.routes = []
        self.current_city = None

    def add_route(self, city1, city2):
        self.routes.append((city1, city2))

    def start_game(self):
        random.shuffle(self.cities)
        self.current_city = self.cities[0]

    def play_turn(self):
        print("Current City:", self.current_city.name)
        print("Possible Cities to Visit:")
        for city in self.cities:
            if city != self.current_city:
                print(city.name)
        destination = input("Select a city to visit: ")
        destination_city = next((city for city in self.cities if city.name == destination), None)
        if destination_city:
            self.add_route(self.current_city, destination_city)
            self.current_city = destination_city
        else:
            print("Invalid city selected. Please try again.")

    def print_route(self):
        print("Route:")
        for route in self.routes:
            print(route[0].name, "->", route[1].name)

# Example Usage
cities = ["City A", "City B", "City C", "City D"]
game = TSPBoardGame(cities)
game.start_game()

while len(game.routes) < len(cities) - 1:
    game.play_turn()

print("Game Over")
game.print_route()


# import itertools
# import math

# class City:
#     def __init__(self, name, x, y):
#         self.name = name
#         self.x = x
#         self.y = y

# def calculate_distance(city1, city2):
#     return math.sqrt((city2.x - city1.x)**2 + (city2.y - city1.y)**2)

# def calculate_total_distance(route):
#     total_distance = 0
#     for i in range(len(route) - 1):
#         total_distance += calculate_distance(route[i], route[i + 1])
#     return total_distance

# def find_optimal_route(cities):
#     optimal_route = None
#     min_distance = float('inf')
#     for perm in itertools.permutations(cities):
#         distance = calculate_total_distance(perm)
#         if distance < min_distance:
#             min_distance = distance
#             optimal_route = perm
#     return optimal_route

# def main():
#     cities = []
#     num_cities = int(input("Enter the number of cities: "))
    
#     for i in range(num_cities):
#         name = input("Enter city name: ")
#         x = float(input("Enter x-coordinate: "))
#         y = float(input("Enter y-coordinate: "))
#         city = City(name, x, y)
#         cities.append(city)
    
#     optimal_route = find_optimal_route(cities)
    
#     print("Optimal Route:")
#     for city in optimal_route:
#         print(city.name)
    
#     total_distance = calculate_total_distance(optimal_route)
#     print("Total Distance:", total_distance)

# if __name__ == "__main__":
#     main()
