def count(numbers):
    multiples = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count_dict = {n: 0 for n in multiples}

    for num in numbers:
        for multiple in multiples:
            if num % multiple == 0:
                count_dict[multiple] += 1

    return count_dict
#Example
input = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count(input)
print(output)
