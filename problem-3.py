def generate_series(a: int):
    if a % 2 == 0:
        a -= 1
    series = [i for i in range(1, a + 1, 2)] 
    return series

a = int(input("Enter a value: "))
print(", ".join(map(str, generate_series(a))))
