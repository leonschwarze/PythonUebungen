cars = 100
spaceInACar = 4
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
averagePassengersPerCar = passengers / carsDriven

print("There are ", cars, "cars available.")
print("Still, there are only ", drivers, "drivers available.")
print("Today, we can transport", carpoolCapacity, "people.")
print("This means putting ", averagePassengersPerCar, "passengers in each car.")
