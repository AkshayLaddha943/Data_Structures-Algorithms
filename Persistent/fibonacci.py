def fibonacci(limit):
    a = 0
    b = 1
    
    print("Fibonacci series: ", a,b)
    for i in range(2, limit):
        c = a+b
        a = b
        b = c
        print(c)

def fibonacci_recursion(n):
    if (n<=1):
        return n
    else:
        return (fibonacci_recursion(n-1)+fibonacci_recursion(n-2))

if __name__ == "__main__":
    print(fibonacci(7))