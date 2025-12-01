def fibonacci_sequence(n):
    fib = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        while len(fib) < n:
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib)
        return fib

print(f"{fibonacci_sequence(10)}")
