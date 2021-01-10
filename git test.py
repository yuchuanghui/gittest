def square(x):
    return x**2
    
def search(y):
    x = 0
    while True:
        if x**2 == y:
            return x
        x += 1

print(search(square(2)))
