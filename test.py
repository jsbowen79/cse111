def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end):
        if (i%2 == 1):
            total += i
    return total
print (sum_of_odd_numbers(10))
