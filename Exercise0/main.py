
people_nb = int(input("How many people need a ride?"))
taxi_capacity = int(input("How many people fit in one taxi?"))

taxiNb = people_nb // taxi_capacity
plus_one_taxi = 0

if people_nb % taxi_capacity:
    plus_one_taxi = 1

print("Number of taxis needed: " + str(plus_one_taxi + taxiNb))
