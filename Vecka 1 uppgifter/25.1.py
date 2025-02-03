import math

def fare_cost(base_fare, distance_km):
    distance_cost = distance_km *1000/140
    rounded_distance_cost = math.floor(distance_cost)
    print(rounded_distance_cost)
    return base_fare + rounded_distance_cost


print(fare_cost(4, 10))