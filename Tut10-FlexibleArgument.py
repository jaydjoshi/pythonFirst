def add(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add(10))
print(add(10, 20))
print(add(10, 20, 30, 40, 50))
print(add("Can", "you", "add", "this?"))
