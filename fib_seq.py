import sys

sys.setrecursionlimit(1000)

fib_cache = {}

def fib(num):
    if num in fib_cache:
        return fib_cache[num]
    if num <= 1:
        return num
    else:
        fib_cache[num] = fib(num-1) + fib(num-2)
        return fib_cache[num]

def main():
    try:
        while True:
            try:
                num = int(input("Enter a number: "))
                print(fib(num))
            except ValueError:
                print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\nGoodbye")

if __name__ == "__main__":
    main()


    