


temp = 29
is_raining = False

if temp < 28 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

is_sunny = True

if temp >= 28 and is_sunny:
    print("It's HOT outside")
    print("It is SUNNY")
elif temp < 28 and is_raining:
    print("Its cold and raining")

if temp >= 28 and not is_sunny:
    print("It's HOT outside")
    print("It is not SUNNY")
elif temp < 28 and not is_raining:
    print("Its cold and not raining")