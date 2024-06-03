def func(index, n, string, c):
    if index == n:
        return c 
    if string[index] in "aeiou":
        c += 1 
    func(index + 1, n, string, c) 

string = "aei"  
c = 0
print(func(0, 3, string, c))
