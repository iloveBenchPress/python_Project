def sum_numberss(*args):
    return sum(args)

def average_decorator(func):
    def wrapper(*args):
        result = func(*args)
        return result / len(args)
    return wrapper

sum_numbers = average_decorator(sum_numberss)


result_sum = sum_numberss(2,3,3,4)
print("Сумма чисел ", result_sum)

result_avg = sum_numbers(2,3,3,4)
print("Среднее арифметическое чисел", result_avg)
