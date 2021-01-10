def square(x):
    return x*x
    
def search(f,y):
    x = 0
    while True:
        if f(x) == y:
            return x
        x += 1
        
def inverse(f):
    def i_function(y):
        return search(f,y)
    return i_function
 
sqrt = inverse(square)
 
 
#print(search(lamda x: square(x)))
print(sqrt(256))