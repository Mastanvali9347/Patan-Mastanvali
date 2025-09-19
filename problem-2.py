def generate_series(a:int):
    series=[]
    for i in range(1,a+1):
        series.append(2*i-1)
    return series

a = int(input("enter a value: "))
print(", ".join(map(str, generate_series(a))))