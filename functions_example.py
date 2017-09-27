import sys

def fibonacci(num):
    previous = 0
    current = 1
    for _ in range(num): 
        sum = previous + current
        print(sum)
        previous = current 
        current = sum

if __name__ == "__main__":
    num = sys.argv[1:]
    fibonacci(int(num[0]))
