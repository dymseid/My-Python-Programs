# class Station:
#     def __init__(self, name, lines):
#         self.name = name
#         self.lines = lines

# class MiniMetroGame:
#     def __init__(self):
#         self.stations = []
#         self.lines = {}

#     def add_station(self, station_name, lines):
#         station = Station(station_name, lines)
#         self.stations.append(station)
#         for line in lines:
#             if line not in self.lines:
#                 self.lines[line] = []
#             self.lines[line].append(station)

#     def play_game(self):
#         while True:
#             print("Current Stations:")
#             for station in self.stations:
#                 print(f"{station.name} - {', '.join(station.lines)}")
#             print("")

#             action = input("Enter 'a' to add a station or 'q' to quit: ")

#             if action == 'a':
#                 station_name = input("Enter station name: ")
#                 lines = input("Enter station lines (separated by commas): ").split(",")
#                 self.add_station(station_name, lines)
#                 print("Station added successfully!")
#             elif action == 'q':
#                 print("Game over. Final stations:")
#                 for station in self.stations:
#                     print(f"{station.name} - {', '.join(station.lines)}")
#                 break
#             else:
#                 print("Invalid action. Please try again.")

# # Example Usage
# game = MiniMetroGame()
# game.play_game()

class City:
    def __init__(self, name):
        self.name = name

class TSPGame:
    def __init__(self):
        self.cities = []

    def add_city(self, city_name):
        city = City(city_name)
        self.cities.append(city)

    def solve_puzzle(self):
        if len(self.cities) < 3:
            print("Not enough cities to solve the puzzle.")
            return
        
        print("Possible cities:")
        for city in self.cities:
            print(city.name)
        print("")
        
        start_city = input("Enter the starting city: ")
        start_city = next((city for city in self.cities if city.name == start_city), None)
        
        if not start_city:
            print("Invalid starting city. Please try again.")
            return

        print("Solving TSP puzzle from", start_city.name)
        remaining_cities = self.cities[:]
        remaining_cities.remove(start_city)
        current_city = start_city

        while remaining_cities:
            print("Current City:", current_city.name)
            print("Remaining Cities:")
            for city in remaining_cities:
                print(city.name)

            next_city = input("Enter the next city: ")
            next_city = next((city for city in remaining_cities if city.name == next_city), None)

            if not next_city:
                print("Invalid city. Please try again.")
                continue

            remaining_cities.remove(next_city)
            current_city = next_city

        print("Puzzle solved!")

# Example Usage
game = TSPGame()

num_cities = int(input("Enter the number of cities: "))

for i in range(num_cities):
    city_name = input(f"Enter city {i+1} name: ")
    game.add_city(city_name)

game.solve_puzzle()
