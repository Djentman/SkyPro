speed = int(input())
weight = int(input())


def f(speed=1, weight=3):
    return 3 * (speed + weight) ** 3 + 275 * weight**2 - 127 * speed - 41


print(f(speed, weight))
print(f())
