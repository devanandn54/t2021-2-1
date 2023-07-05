def generate(a):
    series = []
    for i in range(1, a+1, 2):
        series.append(i)
    return series
#Example
input = 4
output = generate(input)
print(output)
