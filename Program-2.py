def generate(a):
    series = []
    for i in range(1, a*2, 2):
        series.append(i)
    return series

#Example
input = 7
output = generate(input)
print(output)
